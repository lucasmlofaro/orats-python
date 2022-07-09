"""Specifications associated with volatility.
"""

import datetime

from pydantic import Field

from .response import OratsResponse


class HistoricalVolatility(OratsResponse):
    """Historical volatility definitions.

    See corresponding `Historical Volatility`_ response object.
    """

    trade_date: datetime.date = Field(..., alias="tradeDate")
    hv_1_day: float = Field(..., alias="orHv1d")
    hv_5_day: float = Field(..., alias="orHv5d")
    hv_10_day: float = Field(..., alias="orHv10d")
    hv_20_day: float = Field(..., alias="orHv20d")
    hv_30_day: float = Field(..., alias="orHv30d")
    hv_60_day: float = Field(..., alias="orHv60d")
    hv_90_day: float = Field(..., alias="orHv90d")
    hv_100_day: float = Field(..., alias="orHv100d")
    hv_120_day: float = Field(..., alias="orHv120d")
    hv_252_day: float = Field(..., alias="orHv252d")
    hv_500_day: float = Field(..., alias="orHv500d")
    hv_1000_day: float = Field(..., alias="orHv1000d")
    close_to_close_hv_1_day: float = Field(..., alias="clsHv5d")
    close_to_close_hv_5_day: float = Field(..., alias="clsHv10d")
    close_to_close_hv_10_day: float = Field(..., alias="clsHv20d")
    close_to_close_hv_20_day: float = Field(..., alias="clsHv30d")
    close_to_close_hv_30_day: float = Field(..., alias="clsHv60d")
    close_to_close_hv_60_day: float = Field(..., alias="clsHv90d")
    close_to_close_hv_90_day: float = Field(..., alias="clsHv100d")
    close_to_close_hv_100_day: float = Field(..., alias="clsHv120d")
    close_to_close_hv_120_day: float = Field(..., alias="clsHv252d")
    close_to_close_hv_252_day: float = Field(..., alias="clsHv500d")
    close_to_close_hv_500_day: float = Field(..., alias="clsHv1000d")
    hv_ex_earnings_1_day: float = Field(..., alias="orHvXern5d")
    hv_ex_earnings_5_day: float = Field(..., alias="orHvXern10d")
    hv_ex_earnings_10_day: float = Field(..., alias="orHvXern20d")
    hv_ex_earnings_20_day: float = Field(..., alias="orHvXern30d")
    hv_ex_earnings_30_day: float = Field(..., alias="orHvXern60d")
    hv_ex_earnings_60_day: float = Field(..., alias="orHvXern90d")
    hv_ex_earnings_90_day: float = Field(..., alias="orHvXern100d")
    hv_ex_earnings_100_day: float = Field(..., alias="orHvXern120d")
    hv_ex_earnings_120_day: float = Field(..., alias="orHvXern252d")
    hv_ex_earnings_252_day: float = Field(..., alias="orHvXern500d")
    hv_ex_earnings_500_day: float = Field(..., alias="orHvXern1000d")
    hv_ex_earnings_1000_day: float = Field(..., alias="clsHvXern5d")
    close_to_close_hv_ex_earnings_1_day: float = Field(..., alias="clsHvXern10d")
    close_to_close_hv_ex_earnings_5_day: float = Field(..., alias="clsHvXern20d")
    close_to_close_hv_ex_earnings_10_day: float = Field(..., alias="clsHvXern30d")
    close_to_close_hv_ex_earnings_20_day: float = Field(..., alias="clsHvXern60d")
    close_to_close_hv_ex_earnings_30_day: float = Field(..., alias="clsHvXern90d")
    close_to_close_hv_ex_earnings_60_day: float = Field(..., alias="clsHvXern100d")
    close_to_close_hv_ex_earnings_90_day: float = Field(..., alias="clsHvXern120d")
    close_to_close_hv_ex_earnings_100_day: float = Field(..., alias="clsHvXern252d")
    close_to_close_hv_ex_earnings_120_day: float = Field(..., alias="clsHvXern500d")
    close_to_close_hv_ex_earnings_252_day: float = Field(..., alias="clsHvXern1000d")


class IvRank(OratsResponse):
    """IV Rank definitions.

    See corresponding `IV Rank`_ response object.
    """

    trade_date: datetime.date = Field(..., alias="tradeDate")
    iv: float = Field(..., alias="iv")
    iv_rank_1_month: float = Field(..., alias="ivRank1m")
    iv_percentile_1_month: float = Field(..., alias="ivPct1m")
    iv_rank_1_year: float = Field(..., alias="ivRank1y")
    iv_percentile_1_year: float = Field(..., alias="ivPct1y")
    updated_at: datetime.datetime = Field(..., alias="updatedAt")
