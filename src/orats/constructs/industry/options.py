"""Higher level constructs for option contracts."""

import datetime
from typing import Any, Dict, List, Optional, Sequence, Union

from pydantic import PrivateAttr

from orats.constructs.api import data as api_constructs
from orats.constructs.common import IndustryConstruct
from orats.constructs.industry.assets import Asset
from orats.constructs.industry.common import bounds, group_by_ticker
from orats.endpoints.data import endpoints, request as req


class OptionsAnalyzer:
    def __init__(self, token: str = None):
        self._token = token

    def option_chains(
        self,
        tickers: Sequence[str],
        trade_date: datetime.date = None,
        min_delta: float = None,
        max_delta: float = None,
        min_days_to_expiration: int = None,
        max_days_to_expiration: int = None,
    ):
        endpoint = endpoints.StrikesEndpoint(self._token)
        request = req.StrikesRequest(
            tickers=tickers,
            trade_date=trade_date,
            expiration_range=bounds(min_days_to_expiration, max_days_to_expiration),
            delta_range=bounds(min_delta, max_delta),
        )
        response = endpoint(request)
        return [OptionsChain(strikes=strikes) for strikes in group_by_ticker(response)]

    def volatility_surfaces(
        self,
        tickers: Sequence[str],
        trade_date: datetime.date = None,
        forecast: bool = False,
    ):
        endpoint: Union[
            endpoints.MoniesImpliedEndpoint, endpoints.MoniesForecastEndpoint
        ]
        if forecast:
            endpoint = endpoints.MoniesForecastEndpoint(self._token)
        else:
            endpoint = endpoints.MoniesImpliedEndpoint(self._token)

        request = req.MoniesRequest(
            tickers=tickers,
            trade_date=trade_date,
        )
        response = endpoint(request)
        return [
            VolatilitySurface(monies=monies) for monies in group_by_ticker(response)
        ]


class Quote(IndustryConstruct):
    price: float
    size: float
    iv: Optional[float] = None


class Greeks(IndustryConstruct):
    delta: float
    gamma: float
    theta: float
    vega: float
    rho: float
    phi: float


class Option(IndustryConstruct):
    underlying: Asset
    expiration: datetime.date
    strike: float
    price: Optional[float] = None
    spot: Optional[float] = None
    volume: Optional[int] = None
    open_interest: Optional[int] = None
    iv: Optional[float] = None
    greeks: Optional[Greeks] = None
    bid: Optional[Quote] = None
    offer: Optional[Quote] = None


class CallOption(Option):
    @classmethod
    def from_strike(cls, strike: api_constructs.Strike):
        return cls(
            underlying=Asset(ticker=api_constructs.Ticker(ticker=strike.ticker)),
            expiration=strike.expiration_date,
            strike=strike.strike,
            price=strike.call_value,
            spot=strike.spot_price,
            volume=strike.call_volume,
            open_interest=strike.call_open_interest,
            iv=strike.iv,
            greeks=Greeks(
                delta=strike.delta,
                gamma=strike.gamma,
                theta=strike.theta,
                vega=strike.vega,
                rho=strike.rho,
                phi=strike.phi,
            ),
            bid=Quote(
                price=strike.call_bid_price,
                size=strike.call_bid_size,
                iv=strike.call_bid_iv,
            ),
            offer=Quote(
                price=strike.call_ask_price,
                size=strike.call_ask_size,
                iv=strike.call_ask_iv,
            ),
        )


class PutOption(Option):
    @classmethod
    def from_strike(cls, strike: api_constructs.Strike):
        return cls(
            underlying=Asset(ticker=api_constructs.Ticker(ticker=strike.ticker)),
            expiration=strike.expiration_date,
            strike=strike.strike,
            price=strike.put_value,
            spot=strike.spot_price,
            volume=strike.put_volume,
            open_interest=strike.put_open_interest,
            iv=strike.iv,
            greeks=Greeks(
                delta=strike.delta - 1,
                gamma=strike.gamma,
                theta=strike.theta,
                vega=strike.vega,
                rho=strike.rho,
                phi=strike.phi,
            ),
            bid=Quote(
                price=strike.put_bid_price,
                size=strike.put_bid_size,
                iv=strike.put_bid_iv,
            ),
            offer=Quote(
                price=strike.put_ask_price,
                size=strike.put_ask_size,
                iv=strike.put_ask_iv,
            ),
        )


class OptionsChain(IndustryConstruct):
    """
    `Greeks are the same for Calls and Puts
    <https://blog.orats.com/option-greeks-are-the-same-for-calls-and-puts>`_
    """

    strikes: Sequence[api_constructs.Strike]
    _expirations: List[datetime.date] = PrivateAttr([])
    _calls: Dict[datetime.date, List[Option]] = PrivateAttr({})
    _puts: Dict[datetime.date, List[Option]] = PrivateAttr({})

    def __init__(self, **data: Any):
        self._group_by_expiration()
        super().__init__(**data)

    def __iter__(self):
        yield from (
            (self._calls[expiration], self._puts[expiration])
            for expiration in self._expirations
        )

    def _group_by_expiration(self):
        self._calls, self._puts = {}, {}
        for strike in self.strikes:
            expiration = strike.expiration_date

            call = CallOption.from_strike(strike)
            if expiration not in self._calls:
                self._calls[expiration] = []
            self._calls[expiration].append(call)

            put = PutOption.from_strike(strike)
            if expiration not in self._puts:
                self._puts[expiration] = []
            self._puts[expiration].append(put)

    def calls(self):
        return self._calls

    def puts(self):
        return self._puts


class VolatilitySurface(IndustryConstruct):
    monies: Sequence[api_constructs.Money]
    _expirations: List[datetime.date] = PrivateAttr([])
    _slices: Dict[datetime.date, List[api_constructs.Money]] = PrivateAttr({})

    def __init__(self, **data: Any):
        self._group_by_expiration()
        super().__init__(**data)

    def _group_by_expiration(self):
        for money in self.monies:
            expiration = money.expiration_date
            self._expirations.append(expiration)
            if expiration not in self._slices:
                self._slices[expiration] = []
            self._slices[expiration].append(money)
        return self._slices

    def slice(self, expiration: datetime.date):
        return self._slices[expiration]
