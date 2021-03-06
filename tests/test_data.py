import datetime

import pytest

from orats.constructs.api import data as constructs
from orats.endpoints.data import api, endpoints, request as req
from tests.fixtures import fake_api_response


@pytest.fixture(autouse=True)
def data_api(monkeypatch):
    monkeypatch.setattr(endpoints, "_get", fake_api_response)
    monkeypatch.setattr(endpoints, "_post", fake_api_response)


class TestDataApi:
    _api = api.DataApi("demo")

    def test_tickers(self):
        request = req.TickersRequest(ticker="IBM")
        endpoint = self._api.tickers

        assert endpoint._url().endswith("tickers")

        tickers = endpoint(request)
        assert len(tickers) == 1

        ticker = tickers[0]
        assert isinstance(ticker, constructs.Ticker)
        assert isinstance(ticker.ticker, str)
        assert isinstance(ticker.max_date, datetime.date)
        assert isinstance(ticker.min_date, datetime.date)

    def test_strikes(self):
        endpoint = self._api.strikes
        request = req.StrikesRequest(
            tickers=("IBM",),
            expiration_range="30,",
            delta_range="0.30,0.45",
        )

        is_historical = request.trade_date is not None
        url = endpoint._url(historical=is_historical)
        assert url.endswith("strikes")
        assert "hist" not in url

        strikes = endpoint(request)
        for strike in strikes:
            assert isinstance(strike, constructs.Strike)

    def test_strikes_history(self):
        endpoint = self._api.strikes
        request = req.StrikesRequest(
            tickers=("IBM", "AAPL"),
            trade_date=datetime.date(2022, 7, 5),
            expiration_range="30,",
            delta_range="0.30,0.45",
        )

        is_historical = request.trade_date is not None
        assert endpoint._url(historical=is_historical).endswith("hist/strikes")

        strikes = endpoint(request)
        for strike in strikes:
            assert isinstance(strike, constructs.Strike)

    def test_strikes_by_options(self):
        endpoint = self._api.strikes_by_options
        requests = [
            req.StrikesByOptionsRequest(
                ticker="IBM",
                expiration_date=datetime.date(2022, 6, 17),
                strike=50,
            ),
            req.StrikesByOptionsRequest(
                ticker="IBM",
                expiration_date=datetime.date(2022, 6, 17),
                strike=55,
            ),
        ]

        for request in requests:
            is_historical = request.trade_date is not None
            url = endpoint._url(historical=is_historical)
            assert url.endswith("strikes/options")
            assert "hist" not in url

        strikes = endpoint(*requests[:-1])
        for strike in strikes:
            assert isinstance(strike, constructs.Strike)
        strikes = endpoint(*requests)
        for strike in strikes:
            assert isinstance(strike, constructs.Strike)

    def test_strikes_history_by_options(self):
        endpoint = self._api.strikes_by_options
        requests = [
            req.StrikesByOptionsRequest(
                ticker="IBM",
                trade_date=datetime.date(2022, 6, 6),
                expiration_date=datetime.date(2022, 6, 17),
                strike=50,
            ),
            req.StrikesByOptionsRequest(
                ticker="IBM",
                trade_date=datetime.date(2022, 6, 6),
                expiration_date=datetime.date(2022, 6, 17),
                strike=55,
            ),
        ]

        for request in requests:
            is_historical = request.trade_date is not None
            assert endpoint._url(historical=is_historical).endswith(
                "hist/strikes/options"
            )

        strikes = self._api.strikes_by_options(*requests[:-1])
        for strike in strikes:
            assert isinstance(strike, constructs.Strike)
        strikes = self._api.strikes_by_options(*requests)
        for strike in strikes:
            assert isinstance(strike, constructs.Strike)

    def test_monies_implied(self):
        request = req.MoniesRequest(
            tickers=("IBM",),
        )
        monies = self._api.monies_implied(request)
        for money in monies:
            assert isinstance(money, constructs.MoneyImplied)

    def test_monies_implied_history(self):
        request = req.MoniesRequest(
            tickers=("IBM",),
            trade_date=datetime.date(2022, 7, 5),
        )
        monies = self._api.monies_implied(request)
        for money in monies:
            assert isinstance(money, constructs.MoneyImplied)

    def test_monies_forecast(self):
        request = req.MoniesRequest(
            tickers=("IBM",),
        )
        monies = self._api.monies_forecast(request)
        for money in monies:
            assert isinstance(money, constructs.MoneyForecast)

    def test_monies_forecast_history(self):
        request = req.MoniesRequest(
            tickers=("IBM",),
            trade_date=datetime.date(2022, 7, 5),
        )
        monies = self._api.monies_forecast(request)
        for money in monies:
            assert isinstance(money, constructs.MoneyForecast)

    def test_summaries(self):
        request = req.SummariesRequest(
            tickers=("IBM",),
        )
        summaries = self._api.summaries(request)
        for summary in summaries:
            assert isinstance(summary, constructs.Summary)

    def test_summaries_history(self):
        request = req.SummariesRequest(
            tickers=("IBM",),
            trade_date=datetime.date(2022, 7, 5),
        )
        summaries = self._api.summaries(request)
        for summary in summaries:
            assert isinstance(summary, constructs.Summary)

    def test_core_data(self):
        request = req.CoreDataRequest(
            tickers=("IBM",),
        )
        core_data = self._api.core_data(request)
        for core in core_data:
            assert isinstance(core, constructs.Core)

    def test_core_data_history(self):
        request = req.CoreDataRequest(
            tickers=("IBM",),
            trade_date=datetime.date(2022, 7, 5),
        )
        core_data = self._api.core_data(request)
        for core in core_data:
            assert isinstance(core, constructs.Core)

    def test_daily_price(self):
        request = req.DailyPriceRequest(
            tickers=("IBM",),
        )
        daily_price = self._api.daily_price(request)
        for price in daily_price:
            assert isinstance(price, constructs.DailyPrice)

    def test_historical_volatility(self):
        request = req.HistoricalVolatilityRequest(
            tickers=("IBM",),
        )
        historical_volatility = self._api.historical_volatility(request)
        for vol in historical_volatility:
            assert isinstance(vol, constructs.HistoricalVolatility)

    def test_dividend_history(self):
        request = req.DividendHistoryRequest(ticker="IBM")
        dividend_history = self._api.dividend_history(request)
        for dividend in dividend_history:
            assert isinstance(dividend, constructs.DividendHistory)

    def test_earnings_history(self):
        request = req.EarningsHistoryRequest(ticker="IBM")
        earnings_history = self._api.earnings_history(request)
        for earnings in earnings_history:
            assert isinstance(earnings, constructs.EarningsHistory)

    def test_stock_split_history(self):
        request = req.StockSplitHistoryRequest(ticker="IBM")
        stock_split_history = self._api.stock_split_history(request)
        for stock_split in stock_split_history:
            assert isinstance(stock_split, constructs.StockSplitHistory)

    def test_iv_rank(self):
        request = req.IvRankRequest(
            tickers=("IBM",),
        )
        iv_rank = self._api.iv_rank(request)
        for iv in iv_rank:
            assert isinstance(iv, constructs.IvRank)

    def test_iv_rank_history(self):
        request = req.IvRankRequest(
            tickers=("IBM",),
            trade_date=datetime.date(2022, 7, 5),
        )
        iv_rank = self._api.iv_rank(request)
        for iv in iv_rank:
            assert isinstance(iv, constructs.IvRank)
