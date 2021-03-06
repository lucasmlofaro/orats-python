"""ORATS Data API.

Primary features include

* historical options data
* historical volatilities
* greeks
* bid/ask quotes
* 100+ indicators

See the `product page`_ and `API docs`_.

.. _product page: https://orats.com/data-api/
.. _API docs: https://docs.orats.io/datav2-api-guide/
"""
import json
from typing import Any, Iterable, Generic, Mapping, Sequence, Type, TypeVar, Callable

import httpx

from orats.common import get_token
from orats.constructs.api import data as api_constructs
from orats.endpoints.data import request as req, response as res
from orats.endpoints.data.cache import RequestCache
from orats.errors import InsufficientPermissionsError
from orats.sandbox.api.data import FakeDataApi


def _handle_response(response: httpx.Response) -> Mapping[str, Any]:
    if response.status_code == 403:
        raise InsufficientPermissionsError
    return response.json()


def _get(url, params) -> Mapping[str, Any]:
    response = httpx.get(
        url=url,
        params=params,
    )
    return _handle_response(response)


def _post(url, params, body) -> Mapping[str, Any]:
    response = httpx.post(
        url=url,
        json=body,
        params=params,
    )
    return _handle_response(response)


Req = TypeVar("Req", bound=req.DataApiRequest)
Res = TypeVar("Res", bound=api_constructs.DataApiConstruct)


class DataApiEndpoint(Generic[Req, Res]):
    """An endpoint handles a request and relays the response."""

    _base_url = "https://api.orats.io/datav2"
    _resource: str
    # This is a workaround to get access to the specific construct type
    _response_type: Type[Res]
    # Set this to true in subclasses that always use the historical prefix
    _is_historical: bool = False
    # Point this to the corresponding data generator
    _data_generator: Callable[[Req], Sequence[Res]]
    _cache = RequestCache()

    def __init__(self, token: str = None, mock: bool = False):
        """Initializes an API endpoint for a specified resource.

        Args:
          token:
            The authentication token provided to the user.
        """
        self._token = token or get_token()
        self._mock = mock

    def __call__(self, request: Req) -> Sequence[Res]:
        """Handles a request and relays the response.

        Args:
          request:
            Data API request object.

        Returns:
          One or more Data API response objects.
        """
        if self._mock:
            return self._data_generator(request)  # type: ignore

        key = self._key(*request.dict().values())
        if key in self._cache:
            return self._cache[key]

        response = res.DataApiResponse[self._response_type](  # type: ignore
            **self._get(request)
        )
        data = response.data or ()
        self._cache[key] = data
        return data

    def _key(self, *components):
        return f"{self._resource}-{'-'.join([str(c) for c in components])}"

    def _url(self, historical: bool = False) -> str:
        resource = self._resource
        if historical:
            resource = f"hist/{resource}"

        return "/".join((self._base_url, resource))

    def _update_params(self, params: Mapping[str, Any]) -> Mapping[str, Any]:
        updated_params = dict(token=self._token)
        for key, param in params.items():
            if param is None:
                continue
            if not isinstance(param, str) and isinstance(param, Iterable):
                param = ",".join([str(v) for v in param])
            updated_params[key] = param
        return updated_params

    def _get(self, request: Req) -> Mapping[str, Any]:
        is_historical = self._is_historical
        if not is_historical and isinstance(request, req.DataHistoryApiRequest):
            is_historical = request.trade_date is not None

        params = self._update_params(request.dict(by_alias=True))
        return _get(
            url=self._url(historical=is_historical),
            params=params,
        )


class TickersEndpoint(DataApiEndpoint[req.TickersRequest, api_constructs.Ticker]):
    """Retrieves the duration of available data for various assets.

    If no underlying asset is specified, the result will be a list
    of all available ticker symbols. Each symbol is accompanied by
    a start (min) and end (max) date for which data is available.
    See the corresponding `Tickers`_ endpoint.
    """

    _resource = "tickers"
    _response_type = api_constructs.Ticker
    _data_generator = FakeDataApi().tickers


class StrikesEndpoint(DataApiEndpoint[req.StrikesRequest, api_constructs.Strike]):
    """Retrieves strikes data for the given asset(s).

    See the corresponding `Strikes`_ and `Strikes History`_ endpoints.
    """

    _resource = "strikes"
    _response_type = api_constructs.Strike
    _data_generator = FakeDataApi().strikes


class StrikesByOptionsEndpoint(
    DataApiEndpoint[req.StrikesByOptionsRequest, api_constructs.Strike]
):
    """Retrieves strikes data by ticker, expiry, and strike.

    See the corresponding `Strikes by Options`_ and
    `Strikes History by Options`_ endpoints.
    """

    _resource = "strikes/options"
    _response_type = api_constructs.Strike
    _data_generator = FakeDataApi().strikes_by_options

    def __call__(
        self,
        *requests: req.StrikesByOptionsRequest,
    ) -> Sequence[api_constructs.Strike]:
        """Makes a call to the appropriate API endpoint.

        Passing a single request will use the GET request method,
        while passing a sequence will use the POST request method.

        Args:
          requests:
            StrikesByOption request object.

        Returns:
          A list of strikes for each specified asset.
        """
        if self._mock:
            return self._data_generator(*requests)  # type: ignore

        if len(requests) == 1:
            return super().__call__(requests[0])
        else:
            response = res.DataApiResponse[self._response_type](  # type: ignore
                **self._post(requests)
            )
            return response.data or ()

    def _post(
        self, requests: Sequence[req.StrikesByOptionsRequest]
    ) -> Mapping[str, Any]:
        body = [json.loads(request.json(by_alias=True)) for request in requests]
        return _post(url=self._url(), body=body, params=self._update_params({}))


class MoniesImpliedEndpoint(
    DataApiEndpoint[req.MoniesRequest, api_constructs.MoneyImplied]
):
    """Retrieves monthly implied data for monies.

    See the corresponding `Monies`_ and `Monies History`_ endpoints.
    """

    _resource = "monies/implied"
    _response_type = api_constructs.MoneyImplied
    _data_generator = FakeDataApi().monies_implied


class MoniesForecastEndpoint(
    DataApiEndpoint[req.MoniesRequest, api_constructs.MoneyForecast]
):
    """Retrieves monthly forecast data for monies.

    See the corresponding `Monies`_ and `Monies History`_ endpoints.
    """

    _resource = "monies/forecast"
    _response_type = api_constructs.MoneyForecast
    _data_generator = FakeDataApi().monies_forecast


class SummariesEndpoint(DataApiEndpoint[req.SummariesRequest, api_constructs.Summary]):
    """Retrieves SMV Summary data.

    See the corresponding `Summaries`_ and `Summaries History`_ endpoints.
    """

    _resource = "summaries"
    _response_type = api_constructs.Summary
    _data_generator = FakeDataApi().summaries


class CoreDataEndpoint(DataApiEndpoint[req.CoreDataRequest, api_constructs.Core]):
    """Retrieves Core data.

    See the corresponding `Core Data`_ and `Core Data History`_ endpoints.
    """

    _resource = "cores"
    _response_type = api_constructs.Core
    _data_generator = FakeDataApi().core_data


class DailyPriceEndpoint(
    DataApiEndpoint[req.DailyPriceRequest, api_constructs.DailyPrice]
):
    """Retrieves end of day daily stock price data.

    See the corresponding `Daily Price`_ endpoint.
    """

    _resource = "dailies"
    _response_type = api_constructs.DailyPrice
    _is_historical = True
    _data_generator = FakeDataApi().daily_price


class HistoricalVolatilityEndpoint(
    DataApiEndpoint[
        req.HistoricalVolatilityRequest, api_constructs.HistoricalVolatility
    ]
):
    """Retrieves historical volatility data.

    See the corresponding `Historical Volatility`_ endpoint.
    """

    _resource = "hvs"
    _response_type = api_constructs.HistoricalVolatility
    _is_historical = True
    _data_generator = FakeDataApi().historical_volatility


class DividendHistoryEndpoint(
    DataApiEndpoint[req.DividendHistoryRequest, api_constructs.DividendHistory]
):
    """Retrieves dividend history data.

    See the corresponding `Dividend History`_ endpoint.
    """

    _resource = "divs"
    _response_type = api_constructs.DividendHistory
    _is_historical = True
    _data_generator = FakeDataApi().dividend_history


class EarningsHistoryEndpoint(
    DataApiEndpoint[req.EarningsHistoryRequest, api_constructs.EarningsHistory]
):
    """Retrieves earnings history data.

    See the corresponding `Earnings History`_ endpoint.
    """

    _resource = "earnings"
    _response_type = api_constructs.EarningsHistory
    _is_historical = True
    _data_generator = FakeDataApi().earnings_history


class StockSplitHistoryEndpoint(
    DataApiEndpoint[req.StockSplitHistoryRequest, api_constructs.StockSplitHistory]
):
    """Retrieves stock split history data.

    See the corresponding `Stock Split History`_ endpoint.
    """

    _resource = "splits"
    _response_type = api_constructs.StockSplitHistory
    _is_historical = True
    _data_generator = FakeDataApi().stock_split_history


class IvRankEndpoint(DataApiEndpoint[req.IvRankRequest, api_constructs.IvRank]):
    """Retrieves IV rank data.

    See the corresponding `IV Rank`_ and `IV Rank History`_ endpoints.
    """

    _resource = "ivrank"
    _response_type = api_constructs.IvRank
    _data_generator = FakeDataApi().iv_rank
