import datetime

from pydantic import BaseModel, Field


class Strike(BaseModel):
    underlying_symbol: str = Field(..., alias='ticker')
    trade_date: datetime.date = Field(..., alias='tradeDate')
    expiration_date: datetime.date = Field(..., alias='expirDate')
    days_to_expiration: int = Field(..., alias='dte')
    strike: float
    spot_price: float = Field(..., alias='spotPrice')
    underlying_price: float = Field(..., alias='stockPrice')
    iv: float = Field(..., alias='smvVol')
    external_iv: float = Field(..., alias='extSmvVol')
    call_volume: int = Field(..., alias='callVolume')
    call_open_interest: int = Field(..., alias='callOpenInterest')
    call_bid_size: int = Field(..., alias='callBidSize')
    call_ask_size: int = Field(..., alias='callAskSize')
    call_bid_price: float = Field(..., alias='callBidPrice')
    call_ask_price: float = Field(..., alias='callAskPrice')
    call_value: float = Field(..., alias='callValue')
    call_bid_iv: float = Field(..., alias='callBidIv')
    call_mid_iv: float = Field(..., alias='callMidIv')
    call_ask_iv: float = Field(..., alias='callAskIv')
    external_call_value: float = Field(..., alias='extCallValue')
    put_volume: int = Field(..., alias='putVolume')
    put_open_interest: int = Field(..., alias='putOpenInterest')
    put_bid_size: int = Field(..., alias='putBidSize')
    put_ask_size: int = Field(..., alias='putAskSize')
    put_bid_price: float = Field(..., alias='putBidPrice')
    put_ask_price: float = Field(..., alias='putAskPrice')
    put_value: float = Field(..., alias='putValue')
    external_put_value: float = Field(..., alias='extPutValue')
    put_bid_iv: float = Field(..., alias='putBidIv')
    put_mid_iv: float = Field(..., alias='putMidIv')
    put_ask_iv: float = Field(..., alias='putAskIv')
    residual_rate: float = Field(..., alias='residualRate')
    delta: float
    gamma: float
    theta: float
    vega: float
    rho: float
    phi: float
    driftless_theta: float = Field(..., alias='driftlessTheta')
    updated_at: datetime.datetime = Field(..., alias='updatedAt')


class Money:
    underlying_symbol: str = Field(..., alias='ticker')
    trade_date: datetime.date = Field(..., alias='tradeDate')
    expiration_date: datetime.date = Field(..., alias='expirDate')
    underlying_price: float = Field(..., alias='stockPrice')
    spot_price: float = Field(..., alias='spotPrice')
    risk_free_rate: float = Field(..., alias='riskFreeRate')
    yield_rate: float = Field(..., alias='yieldRate')
    residual_yield_rate: float = Field(..., alias='residualYieldRate')
    residual_rate_slope: float = Field(..., alias='residualRateSlp')
    residual_r2: float = Field(..., alias='residualR2')
    confidence: float
    market_width: float = Field(..., alias='mwVol')
    iv_delta_100: float = Field(..., alias='vol100')
    iv_delta_95: float = Field(..., alias='vol95')
    iv_delta_90: float = Field(..., alias='vol90')
    iv_delta_85: float = Field(..., alias='vol85')
    iv_delta_80: float = Field(..., alias='vol80')
    iv_delta_75: float = Field(..., alias='vol75')
    iv_delta_70: float = Field(..., alias='vol70')
    iv_delta_65: float = Field(..., alias='vol65')
    iv_delta_60: float = Field(..., alias='vol60')
    iv_delta_55: float = Field(..., alias='vol55')
    iv_delta_50: float = Field(..., alias='vol50')
    iv_delta_45: float = Field(..., alias='vol45')
    iv_delta_40: float = Field(..., alias='vol40')
    iv_delta_35: float = Field(..., alias='vol35')
    iv_delta_30: float = Field(..., alias='vol30')
    iv_delta_25: float = Field(..., alias='vol25')
    iv_delta_20: float = Field(..., alias='vol20')
    iv_delta_15: float = Field(..., alias='vol15')
    iv_delta_10: float = Field(..., alias='vol10')
    iv_delta_5: float = Field(..., alias='vol5')
    iv_delta_0: float = Field(..., alias='vol0')
    atm_iv: float = Field(..., alias='atmiv')
    slope: float
    derivative: float = Field(..., alias='deriv')
    fit: float
    iv: float = Field(..., alias='calVol')
    unadjusted_iv: float = Field(..., alias='unadjVol')
    earnings_effect: float = Field(..., alias='earnEffect')
    updated_at: datetime.datetime = Field(..., alias='updatedAt')
