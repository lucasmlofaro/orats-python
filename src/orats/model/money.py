"""Money-ness Specification.
"""
import datetime

from pydantic import BaseModel, Field

from .response import OratsResponse


class MoneyImplied(OratsResponse):
    """Monthly implied money definitions.

    See corresponding `Monies`_ response object.
    """

    trade_date: datetime.date = Field(..., alias="tradeDate")
    expiration_date: datetime.date = Field(..., alias="expirDate")
    underlying_price: float = Field(..., alias="stockPrice")
    spot_price: float = Field(..., alias="spotPrice")
    risk_free_rate: float = Field(..., alias="riskFreeRate")
    yield_rate: float = Field(..., alias="yieldRate")
    residual_yield_rate: float = Field(..., alias="residualYieldRate")
    residual_rate_slope: float = Field(..., alias="residualRateSlp")
    residual_r2: float = Field(..., alias="residualR2")
    confidence: float
    market_width: float = Field(..., alias="mwVol")
    iv_100_delta: float = Field(..., alias="vol100")
    iv_95_delta: float = Field(..., alias="vol95")
    iv_90_delta: float = Field(..., alias="vol90")
    iv_85_delta: float = Field(..., alias="vol85")
    iv_80_delta: float = Field(..., alias="vol80")
    iv_75_delta: float = Field(..., alias="vol75")
    iv_70_delta: float = Field(..., alias="vol70")
    iv_65_delta: float = Field(..., alias="vol65")
    iv_60_delta: float = Field(..., alias="vol60")
    iv_55_delta: float = Field(..., alias="vol55")
    iv_50_delta: float = Field(..., alias="vol50")
    iv_45_delta: float = Field(..., alias="vol45")
    iv_40_delta: float = Field(..., alias="vol40")
    iv_35_delta: float = Field(..., alias="vol35")
    iv_30_delta: float = Field(..., alias="vol30")
    iv_25_delta: float = Field(..., alias="vol25")
    iv_20_delta: float = Field(..., alias="vol20")
    iv_15_delta: float = Field(..., alias="vol15")
    iv_10_delta: float = Field(..., alias="vol10")
    iv_5_delta: float = Field(..., alias="vol5")
    iv_0_delta: float = Field(..., alias="vol0")
    atm_iv: float = Field(..., alias="atmiv")
    slope: float
    derivative: float = Field(..., alias="deriv")
    fit: float
    iv: float = Field(..., alias="calVol")
    unadjusted_iv: float = Field(..., alias="unadjVol")
    earnings_effect: float = Field(..., alias="earnEffect")
    updated_at: datetime.datetime = Field(..., alias="updatedAt")


class MoneyForecast(BaseModel):
    """Monthly forecast money definitions.

    See corresponding `Monies`_ response object.
    """

    underlying_symbol: str = Field(..., alias="ticker")
    trade_date: datetime.date = Field(..., alias="tradeDate")
    expiration_date: datetime.date = Field(..., alias="expirDate")
    underlying_price: float = Field(..., alias="stockPrice")
    risk_free_rate: float = Field(..., alias="riskFreeRate")
    iv_100_delta: float = Field(..., alias="vol100")
    iv_95_delta: float = Field(..., alias="vol95")
    iv_90_delta: float = Field(..., alias="vol90")
    iv_85_delta: float = Field(..., alias="vol85")
    iv_80_delta: float = Field(..., alias="vol80")
    iv_75_delta: float = Field(..., alias="vol75")
    iv_70_delta: float = Field(..., alias="vol70")
    iv_65_delta: float = Field(..., alias="vol65")
    iv_60_delta: float = Field(..., alias="vol60")
    iv_55_delta: float = Field(..., alias="vol55")
    iv_50_delta: float = Field(..., alias="vol50")
    iv_45_delta: float = Field(..., alias="vol45")
    iv_40_delta: float = Field(..., alias="vol40")
    iv_35_delta: float = Field(..., alias="vol35")
    iv_30_delta: float = Field(..., alias="vol30")
    iv_25_delta: float = Field(..., alias="vol25")
    iv_20_delta: float = Field(..., alias="vol20")
    iv_15_delta: float = Field(..., alias="vol15")
    iv_10_delta: float = Field(..., alias="vol10")
    iv_5_delta: float = Field(..., alias="vol5")
    iv_0_delta: float = Field(..., alias="vol0")
    updated_at: datetime.datetime = Field(..., alias="updatedAt")
