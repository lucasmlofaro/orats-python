"""Specifications associated with an underlying asset.
"""

import datetime

from pydantic import Field

from .response import OratsResponse


class Ticker(OratsResponse):
    """Ticker symbol data duration definitions.
    """
    min_date: datetime.date = Field(..., alias="min")
    max_date: datetime.date = Field(..., alias="max")


class DailyPrice(OratsResponse):
    """Daily price definitions.
    """
    trade_date: datetime.date = Field(..., alias="tradeDate")
    open: float = Field(..., alias="open")
    high: float = Field(..., alias="hiPx")
    low: float = Field(..., alias="loPx")
    close: float = Field(..., alias="clsPx")
    unadjusted_open: float = Field(..., alias="unadjOpen")
    unadjusted_high: float = Field(..., alias="unadjHiPx")
    unadjusted_low: float = Field(..., alias="unadjLoPx")
    unadjusted_close: float = Field(..., alias="unadjClsPx")
    updated_at: datetime.datetime = Field(..., alias="updatedAt")


class DividendHistory(OratsResponse):
    """Dividend History definitions.
    """
    ex_dividend_date: datetime.date = Field(..., alias="exDate")
    dividend_amount: float = Field(..., alias="divAmt")
    dividend_frequency: int = Field(..., alias="divFreq")
    declared_date: datetime.date = Field(..., alias="declaredDate")


class EarningsHistory(OratsResponse):
    """Earnings history definitions.
    """
    earnings_date: datetime.date = Field(..., alias="earnDate")
    time_of_day_announced: int = Field(..., alias="anncTod")
    updated_at: datetime.date = Field(..., alias="updatedAt")


class StockSplitHistory(OratsResponse):
    """Stock split history definitions.
    """
    split_date: datetime.date = Field(..., alias="splitDate")
    divisor: float
