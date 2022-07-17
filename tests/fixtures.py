import datetime
import json
import os
import random
from typing import Dict, Any


def persist_fixture(resource, fixture, prefix="data"):
    directory = os.path.dirname(__file__)
    path = os.path.join(directory, "fixtures", prefix, f"{resource}.json")
    with open(path, "w") as file:
        json.dump(fixture, file, indent=2)


def _resource(url):
    return "/".join(url.split("://")[1].split("/")[2:])


def load_fixture(url, *args, **kwargs):
    return _endpoints[_resource(url)]


def ticker_data_definition() -> Dict[str, Any]:
    return {"ticker": "IBM", "min": "2007-01-03", "max": "2022-07-11"}


def strike_data_definition(ticker: str = "IBM") -> Dict[str, Any]:
    today = datetime.date.today()
    updated = datetime.datetime.now()
    days_to_expiration = 39
    spot_price = 100 + 65 * random.random()
    call_price = round(2 + 5 * random.random(), 2)
    call_iv = random.random()
    put_price = round(3 + 6 * random.random(), 2)
    put_iv = call_iv + 0.02 * (random.random() - 0.5)
    return {
        "ticker": ticker,
        "tradeDate": str(today),
        "expirDate": str(today + datetime.timedelta(days=days_to_expiration)),
        "dte": days_to_expiration,
        "strike": random.randint(112, 189),
        "stockPrice": spot_price,
        "callVolume": random.randint(0, 200),
        "callOpenInterest": random.randint(0, 200),
        "callBidSize": random.randint(0, 200),
        "callAskSize": random.randint(0, 200),
        "putVolume": random.randint(0, 200),
        "putOpenInterest": random.randint(0, 200),
        "putBidSize": random.randint(0, 200),
        "putAskSize": random.randint(0, 200),
        "callBidPrice": round(call_price - random.random(), 2),
        "callValue": call_price,
        "callAskPrice": round(call_price + random.random(), 2),
        "putBidPrice": round(put_price - random.random(), 2),
        "putValue": put_price,
        "putAskPrice": round(put_price + random.random(), 2),
        "callBidIv": call_iv - 0.02 * random.random(),
        "callMidIv": call_iv,
        "callAskIv": call_iv + 0.02 * random.random(),
        "smvVol": (call_iv + put_iv) / 2,
        "putBidIv": put_iv - 0.02 * random.random(),
        "putMidIv": put_iv,
        "putAskIv": put_iv + 0.02 * random.random(),
        "residualRate": 0.1 * (random.random() - 0.5),
        "delta": random.random(),
        "gamma": 0.2 * random.random(),
        "theta": -random.random(),
        "vega": random.random(),
        "rho": random.random(),
        "phi": -random.random(),
        "driftlessTheta": -random.random(),
        "callSmvVol": call_iv + 0.02 * (random.random() - 0.5),
        "putSmvVol": put_iv + 0.02 * (random.random() - 0.5),
        "extSmvVol": call_iv + 0.2 * (random.random() - 0.5),
        "extCallValue": call_price + 2 * (random.random() - 0.5),
        "extPutValue": put_price + 2 * (random.random() - 0.5),
        "spotPrice": spot_price,
        "quoteDate": f"{updated.isoformat()}Z",
        "updatedAt": f"{updated.isoformat()}Z",
        "snapShotEstTime": "1600",
        "snapShotDate": f"{updated.isoformat()}Z",
        "expiryTod": "pm",
    }


def money_implied_data_definition(ticker: str = "IBM") -> Dict[str, Any]:
    today = datetime.date.today()
    days_to_expiration = 39
    spot_price = 100 + 65 * random.random()
    volatility_100_delta = random.random()
    updated = datetime.datetime.now()
    return {
        "ticker": ticker,
        "tradeDate": str(today),
        "expirDate": str(today + datetime.timedelta(days=days_to_expiration)),
        "stockPrice": spot_price,
        "riskFreeRate": 0.05 + 0.15 * random.random(),
        "yieldRate": 0,
        "residualYieldRate": -0.001 * random.random(),
        "residualRateSlp": 0,
        "residualR2": 0.06 * random.random(),
        "confidence": 0.75 + 0.25 * random.random(),
        "mwVol": 0.1 * random.random(),
        "vol100": volatility_100_delta,
        "vol95": 0.95 * volatility_100_delta,
        "vol90": 0.95**2 * volatility_100_delta,
        "vol85": 0.95**3 * volatility_100_delta,
        "vol80": 0.95**4 * volatility_100_delta,
        "vol75": 0.95**5 * volatility_100_delta,
        "vol70": 0.95**6 * volatility_100_delta,
        "vol65": 0.95**7 * volatility_100_delta,
        "vol60": 0.95**8 * volatility_100_delta,
        "vol55": 0.95**9 * volatility_100_delta,
        "vol50": 0.95**10 * volatility_100_delta,
        "vol45": 0.95**11 * volatility_100_delta,
        "vol40": 0.95**12 * volatility_100_delta,
        "vol35": 0.95**13 * volatility_100_delta,
        "vol30": 0.95**14 * volatility_100_delta,
        "vol25": 0.95**15 * volatility_100_delta,
        "vol20": 0.95**16 * volatility_100_delta,
        "vol15": 0.95**17 * volatility_100_delta,
        "vol10": 0.95**18 * volatility_100_delta,
        "vol5": 00.95**19 * volatility_100_delta,
        "vol0": 00.95**20 * volatility_100_delta,
        "typeFlag": 0,
        "atmiv": volatility_100_delta / 2,
        "slope": 60 * (random.random() - 0.5),
        "deriv": 0.1 * (random.random() - 0.5),
        "fit": 1e-05 * random.random(),
        "spotPrice": spot_price,
        "calVol": volatility_100_delta * (0.4 + 0.2 * random.random()) / 2,
        "unadjVol": volatility_100_delta / 2,
        "earnEffect": 0,
        "quoteDate": f"{updated.isoformat()}Z",
        "updatedAt": f"{updated.isoformat()}Z",
        "snapShotEstTime": "1600",
        "snapShotDate": f"{updated.isoformat()}Z",
        "expiryTod": "pm",
    }


def money_forecast_data_definition(ticker: str = "IBM") -> Dict[str, Any]:
    today = datetime.date.today()
    days_to_expiration = 39
    spot_price = 100 + 65 * random.random()
    volatility_100_delta = random.random()
    updated = datetime.datetime.now()
    return {
        "ticker": ticker,
        "tradeDate": str(today),
        "expirDate": str(today + datetime.timedelta(days=days_to_expiration)),
        "stockPrice": spot_price,
        "riskFreeRate": 0.05 + 0.15 * random.random(),
        "vol100": volatility_100_delta,
        "vol95": 0.95 * volatility_100_delta,
        "vol90": 0.95**2 * volatility_100_delta,
        "vol85": 0.95**3 * volatility_100_delta,
        "vol80": 0.95**4 * volatility_100_delta,
        "vol75": 0.95**5 * volatility_100_delta,
        "vol70": 0.95**6 * volatility_100_delta,
        "vol65": 0.95**7 * volatility_100_delta,
        "vol60": 0.95**8 * volatility_100_delta,
        "vol55": 0.95**9 * volatility_100_delta,
        "vol50": 0.95**10 * volatility_100_delta,
        "vol45": 0.95**11 * volatility_100_delta,
        "vol40": 0.95**12 * volatility_100_delta,
        "vol35": 0.95**13 * volatility_100_delta,
        "vol30": 0.95**14 * volatility_100_delta,
        "vol25": 0.95**15 * volatility_100_delta,
        "vol20": 0.95**16 * volatility_100_delta,
        "vol15": 0.95**17 * volatility_100_delta,
        "vol10": 0.95**18 * volatility_100_delta,
        "vol5": 00.95**19 * volatility_100_delta,
        "vol0": 00.95**20 * volatility_100_delta,
        "quoteDate": f"{updated.isoformat()}Z",
        "updatedAt": f"{updated.isoformat()}Z",
        "snapShotEstTime": "1600",
        "snapShotDate": f"{updated.isoformat()}Z",
        "expiryTod": "pm",
    }


def summary_data_definition() -> Dict[str, Any]:
    return {
        "ticker": "IBM",
        "tradeDate": "2022-07-11",
        "stockPrice": 140.91,
        "annActDiv": 6.6,
        "annIdiv": 6.219711241365849,
        "borrow30": 0.0007589506622195224,
        "borrow2y": 0.026864400946853068,
        "confidence": 0.9511693079292712,
        "exErnIv10d": 0.3041920894594634,
        "exErnIv20d": 0.29160431277613263,
        "exErnIv30d": 0.28517382319786666,
        "exErnIv60d": 0.2631281058677467,
        "exErnIv90d": 0.2593226395931322,
        "exErnIv6m": 0.25396767417436256,
        "exErnIv1y": 0.2547238899422641,
        "ieeEarnEffect": 2.3326074086309134,
        "impliedMove": 0.059163109598338016,
        "impliedNextDiv": 1.3731729188456947,
        "iv10d": 0.38004932901298644,
        "iv20d": 0.3529915107614268,
        "iv30d": 0.3255071862567114,
        "iv60d": 0.2827035536453777,
        "iv90d": 0.2795040098334221,
        "iv6m": 0.27121636682668493,
        "iv1y": 0.2677721968612911,
        "mwAdj30": 0.018797358208937392,
        "mwAdj2y": 0.011647567343255817,
        "nextDiv": "1.65",
        "rDrv30": 0.0664285390504781,
        "rDrv2y": 0.07293921201827949,
        "rSlp30": 3.8435617418488426,
        "rSlp2y": 4.088827606838615,
        "rVol30": 0.27178778135848247,
        "rVol2y": 0.2379080218447835,
        "rip": 2.393222788098016,
        "riskFree30": 0.018104692644101184,
        "riskFree2y": 0.027794697788554024,
        "skewing": 0.46518035784671186,
        "contango": -0.013361055789295556,
        "totalErrorConf": 9.720635977434513e-05,
        "dlt5Iv10d": 0.36433382385042123,
        "dlt5Iv20d": 0.3275399934923336,
        "dlt5Iv30d": 0.29101853678463113,
        "dlt5Iv60d": 0.24977408021107766,
        "dlt5Iv90d": 0.24762096987351007,
        "dlt5Iv6m": 0.24184903102400507,
        "dlt5Iv1y": 0.23400217253119976,
        "exErnDlt5Iv10d": 0.2884765842968982,
        "exErnDlt5Iv20d": 0.2661527955070394,
        "exErnDlt5Iv30d": 0.2506851737257864,
        "exErnDlt5Iv60d": 0.23019863243344668,
        "exErnDlt5Iv90d": 0.2274395996332201,
        "exErnDlt5Iv6m": 0.2246003383716827,
        "exErnDlt5Iv1y": 0.22095386561217276,
        "dlt25Iv10d": 0.35957717177118464,
        "dlt25Iv20d": 0.33052286579814616,
        "dlt25Iv30d": 0.30338031461138093,
        "dlt25Iv60d": 0.25878890378440106,
        "dlt25Iv90d": 0.25537693028433983,
        "dlt25Iv6m": 0.24689456811408952,
        "dlt25Iv1y": 0.2449072199792144,
        "exErnDlt25Iv10d": 0.2837199322176616,
        "exErnDlt25Iv20d": 0.26913566781285203,
        "exErnDlt25Iv30d": 0.2630469515525362,
        "exErnDlt25Iv60d": 0.23921345600677008,
        "exErnDlt25Iv90d": 0.23519556004404987,
        "exErnDlt25Iv6m": 0.22964587546176715,
        "exErnDlt25Iv1y": 0.2318589130601874,
        "dlt75Iv10d": 0.4162113132307224,
        "dlt75Iv20d": 0.39187711818015064,
        "dlt75Iv30d": 0.36465435070691954,
        "dlt75Iv60d": 0.3203020423035514,
        "dlt75Iv90d": 0.3149299138967877,
        "dlt75Iv6m": 0.30412582618561945,
        "dlt75Iv1y": 0.30260992807671594,
        "exErnDlt75Iv10d": 0.3403540736771994,
        "exErnDlt75Iv20d": 0.33048992019485646,
        "exErnDlt75Iv30d": 0.3243209876480748,
        "exErnDlt75Iv60d": 0.30072659452592043,
        "exErnDlt75Iv90d": 0.2947485436564977,
        "exErnDlt75Iv6m": 0.2868771335332971,
        "exErnDlt75Iv1y": 0.2895616211576889,
        "dlt95Iv10d": 0.5112827790074124,
        "dlt95Iv20d": 0.4929953607371904,
        "dlt95Iv30d": 0.4355311708792758,
        "dlt95Iv60d": 0.3930229181152338,
        "dlt95Iv90d": 0.39364306506151264,
        "dlt95Iv6m": 0.3838325080167292,
        "dlt95Iv1y": 0.3654632132449407,
        "exErnDlt95Iv10d": 0.43542553945388934,
        "exErnDlt95Iv20d": 0.4316081627518963,
        "exErnDlt95Iv30d": 0.39519780782043107,
        "exErnDlt95Iv60d": 0.37344747033760284,
        "exErnDlt95Iv90d": 0.3734616948212227,
        "exErnDlt95Iv6m": 0.3665838153644068,
        "exErnDlt95Iv1y": 0.35241490632591366,
        "fwd30_20": 0.26202818851225745,
        "fwd60_30": 0.23213717966471567,
        "fwd90_30": 0.2533895678931196,
        "fwd90_60": 0.2729924468761641,
        "fwd180_90": 0.26266736332550367,
        "fexErn30_20": 0.2718569069429415,
        "fexErn60_30": 0.23905792343657664,
        "fexErn90_30": 0.24537785635562193,
        "fexErn90_60": 0.2515390506890577,
        "fexErn180_90": 0.24849733931275975,
        "ffwd30_20": 0.20457560906797856,
        "ffwd60_30": 0.17709452279475948,
        "ffwd90_30": 0.21450437242036208,
        "ffwd90_60": 0.26496646893800485,
        "ffwd180_90": 0.250852945712395,
        "ffexErn30_20": 0.256265021639109,
        "ffexErn60_30": 0.20811900652301785,
        "ffexErn90_30": 0.22341087759026282,
        "ffexErn90_60": 0.24258041453772214,
        "ffexErn180_90": 0.24085091652355958,
        "fbfwd30_20": 0.7807389358737207,
        "fbfwd60_30": 0.7628873713833504,
        "fbfwd90_30": 0.8465398721972666,
        "fbfwd90_60": 0.9705999999999999,
        "fbfwd180_90": 0.9550213720367386,
        "fbfexErn30_20": 0.9426467199999999,
        "fbfexErn60_30": 0.8705798307422885,
        "fbfexErn90_30": 0.9104769310009672,
        "fbfexErn90_60": 0.9643847103390326,
        "fbfexErn180_90": 0.9692293575039999,
        "impliedEarningsMove": 0.045007312129919666,
        "quoteDate": "2022-07-11T19:59:35Z",
        "updatedAt": "2022-07-11T19:59:49Z",
        "snapShotEstTime": "1600",
        "snapShotDate": "2022-07-11T20:00:02Z",
    }


def core_data_definition() -> Dict[str, Any]:
    return {
        "ticker": "IBM",
        "tradeDate": "2022-07-11",
        "assetType": 3,
        "priorCls": 140.47,
        "pxAtmIv": 140.98,
        "mktCap": 126802,
        "cVolu": 23498,
        "cOi": 219415,
        "pVolu": 7746,
        "pOi": 134068,
        "orFcst20d": 24.232,
        "orIvFcst20d": 21.863,
        "orFcstInf": 19.23,
        "orIvXern20d": 25.8,
        "orIvXernInf": 22.37,
        "iv200Ma": 22.77,
        "atmIvM1": 26.498,
        "atmFitIvM1": 27.963,
        "atmFcstIvM1": 24.232,
        "dtExM1": 5,
        "atmIvM2": 31.039,
        "atmFitIvM2": 30.868,
        "atmFcstIvM2": 24.657,
        "dtExM2": 40,
        "atmIvM3": 27.589,
        "atmFitIvM3": 28.038,
        "atmFcstIvM3": 23.148,
        "dtExM3": 68,
        "atmIvM4": 28.158,
        "atmFitIvM4": 28.424,
        "atmFcstIvM4": 22.771,
        "dtExM4": 103,
        "iRate5wk": 1.81,
        "iRateLt": 2.78,
        "px1kGam": 2066.71,
        "volOfVol": 0.084,
        "volOfIvol": 0.0402,
        "slope": 3.884673,
        "slopeInf": 4.14018,
        "slopeFcst": 4.19185,
        "slopeFcstInf": 4.40008,
        "deriv": 0.0653,
        "derivInf": 0.0662,
        "derivFcst": 0.0714,
        "derivFcstInf": 0.0871,
        "mktWidthVol": 1.696,
        "mktWidthVolInf": 1.123,
        "cAddPrem": 0,
        "pAddPrem": 0,
        "rip": 2.16236,
        "ivEarnReturn": 0,
        "fcstR2": 0.362,
        "fcstR2Imp": 0.2878,
        "hiHedge": 0,
        "loHedge": 0,
        "stkVolu": 5073401,
        "avgOptVolu20d": 35913.1,
        "sector": "XLK Business Services  NEC42934",
        "orHv1d": 10.46,
        "orHv5d": 23.89,
        "orHv10d": 24.06,
        "orHv20d": 23.45,
        "orHv60d": 28.77,
        "orHv90d": 26.07,
        "orHv120d": 26.39,
        "orHv252d": 23.87,
        "orHv500d": 24.14,
        "orHv1000d": 27.25,
        "clsHv5d": 22.73,
        "clsHv10d": 21.52,
        "clsHv20d": 20.44,
        "clsHv60d": 28.19,
        "clsHv90d": 24.51,
        "clsHv120d": 24.67,
        "clsHv252d": 22.93,
        "clsHv500d": 24.16,
        "clsHv1000d": 28.69,
        "iv20d": 35.13,
        "iv30d": 32.5,
        "iv60d": 28.3,
        "iv90d": 27.96,
        "iv6m": 27.04,
        "clsPx1w": 137.62,
        "stkPxChng1wk": 2.44,
        "clsPx1m": 135.11,
        "stkPxChng1m": 4.34,
        "clsPx6m": 131.8238,
        "stkPxChng6m": 6.95,
        "clsPx1y": 128.1993,
        "stkPxChng1y": 9.97,
        "divFreq": 91,
        "divYield": 4.7,
        "divGrwth": 0,
        "divDate": "2022-08-09",
        "divAmt": 1.65,
        "nextErn": "0000-00-00",
        "nextErnTod": 1630,
        "lastErn": "2022-04-19",
        "lastErnTod": 3,
        "absAvgErnMv": 5.0635,
        "impliedIee": 3.0363,
        "daysToNextErn": 0,
        "tkOver": 0,
        "etfIncl": "",
        "bestEtf": "XLK",
        "sectorName": "Technology Hardware & Equipment",
        "correlSpy1m": 0.93,
        "correlSpy1y": 0.88,
        "correlEtf1m": 0.91,
        "correlEtf1y": 0.88,
        "beta1m": 0.53,
        "beta1y": 0.48,
        "ivPctile1m": 23,
        "ivPctile1y": 64,
        "ivPctileSpy": 18,
        "ivPctileEtf": 23,
        "ivStdvMean": 0.38,
        "ivStdv1y": 3.38,
        "ivSpyRatio": 1.01,
        "ivSpyRatioAvg1m": 0.91,
        "ivSpyRatioAvg1y": 1.31,
        "ivSpyRatioStdv1y": 4.36,
        "ivEtfRatio": 0.81,
        "ivEtfRatioAvg1m": 0.72,
        "ivEtfRatioAvg1y": 0.96,
        "ivEtFratioStdv1y": 3.72,
        "ivHvXernRatio": 0.98,
        "ivHvXernRatio1m": 0.97,
        "ivHvXernRatio1y": 1.08,
        "ivHvXernRatioStdv1y": 4.9,
        "etfIvHvXernRatio": 1.11,
        "etfIvHvXernRatio1m": 1.12,
        "etfIvHvXernRatio1y": 1.03,
        "etfIvHvXernRatioStdv1y": 0.1,
        "slopepctile": 75.4,
        "slopeavg1m": 3.81,
        "slopeavg1y": 2.99,
        "slopeStdv1y": 1.03,
        "etfSlopeRatio": 0.82,
        "etfSlopeRatioAvg1m": 0.86,
        "etfSlopeRatioAvg1y": 0.67,
        "etfSlopeRatioAvgStdv1y": 0.23,
        "impliedR2": 0.4195,
        "contango": -0.48,
        "nextDiv": 1.65,
        "impliedNextDiv": 1.3241,
        "annActDiv": 6.6,
        "annIdiv": 6.0681,
        "borrow30": -0.4207,
        "borrow2yr": 2.5395,
        "error": 0.0128,
        "confidence": 95.0004,
        "pxCls": 140.47,
        "wksNextErn": 1,
        "ernMnth": 7,
        "oi": 353483,
        "straPxM1": 3.15,
        "straPxM2": 8.18,
        "smoothStraPxM1": 3.15,
        "smoothStrPxM2": 8.18,
        "fcstStraPxM1": 2.86,
        "fcstStraPxM2": 5.56,
        "loStrikeM1": 141,
        "hiStrikeM1": 141,
        "loStrikeM2": 141,
        "hiStrikeM2": 141,
        "ernDate1": "4/19/2022",
        "ernDate2": "1/24/2022",
        "ernDate3": "10/20/2021",
        "ernDate4": "7/19/2021",
        "ernDate5": "4/19/2021",
        "ernDate6": "1/21/2021",
        "ernDate7": "10/19/2020",
        "ernDate8": "7/20/2020",
        "ernDate9": "4/20/2020",
        "ernDate10": "1/21/2020",
        "ernDate11": "10/16/2019",
        "ernDate12": "7/17/2019",
        "ernMv1": 7.1003,
        "ernMv2": 5.6513,
        "ernMv3": -9.5631,
        "ernMv4": 1.4864,
        "ernMv5": 3.7861,
        "ernMv6": -9.9051,
        "ernMv7": -6.493,
        "ernMv8": -0.2453,
        "ernMv9": -3.0313,
        "ernMv10": 3.3915,
        "ernMv11": -5.5239,
        "ernMv12": 4.5852,
        "ernStraPct1": 7.1536,
        "ernStraPct2": 8.8803,
        "ernStraPct3": 5.9566,
        "ernStraPct4": 6.4897,
        "ernStraPct5": 6.7275,
        "ernStraPct6": 7.4359,
        "ernStraPct7": 7.8042,
        "ernStraPct8": 8.0954,
        "ernStraPct9": 10.8637,
        "ernStraPct10": 5.754,
        "ernStraPct11": 4.6138,
        "ernStraPct12": 4.0031,
        "ernEffct1": 2.6865,
        "ernEffct2": 2.2976,
        "ernEffct3": 3.6819,
        "ernEffct4": 1.6731,
        "ernEffct5": 1.5488,
        "ernEffct6": 2.7594,
        "ernEffct7": 1.808,
        "ernEffct8": 1.3719,
        "ernEffct9": 1.0591,
        "ernEffct10": 1.7018,
        "ernEffct11": 2.3169,
        "ernEffct12": 2.589,
        "orHvXern5d": 23.89,
        "orHvXern10d": 24.06,
        "orHvXern20d": 23.45,
        "orHvXern60d": 27.03,
        "orHvXern90d": 24.75,
        "orHvXern120d": 24.19,
        "orHvXern252d": 21.69,
        "orHvXern500d": 22.36,
        "orHvXern1000d": 26.08,
        "clsHvXern5d": 22.73,
        "clsHvXern10d": 21.52,
        "clsHvXern20d": 20.44,
        "clsHvXern60d": 24.29,
        "clsHvXern90d": 21.46,
        "clsHvXern120d": 20.94,
        "clsHvXern252d": 18.84,
        "clsHvXern500d": 20.63,
        "clsHvXern1000d": 26.43,
        "iv10d": 37.9,
        "iv1yr": 26.77,
        "fcstSlope": 4.1918,
        "fcstErnEffct": 2.0296,
        "ernMvStdv": 2.8171,
        "impliedEe": 3.0363,
        "impErnMv": 6.99,
        "impMth2ErnMv": 6.99,
        "fairVol90d": 41.6097,
        "fairXieeVol90d": 42.1331,
        "fairMth2XieeVol90d": 25.949,
        "impErnMv90d": 14.76,
        "impErnMvMth290d": 9.85,
        "exErnIv10d": 26.76,
        "exErnIv20d": 25.66,
        "exErnIv30d": 26,
        "exErnIv60d": 24.96,
        "exErnIv90d": 24.49,
        "exErnIv6m": 24.05,
        "exErnIv1yr": 24.5,
        "dlt5Iv10d": 36.33,
        "dlt5Iv20d": 32.55,
        "dlt5Iv30d": 29.08,
        "dlt5Iv60d": 24.92,
        "dlt5Iv90d": 24.81,
        "dlt5Iv6m": 24.19,
        "dlt5Iv1y": 23.47,
        "exErnDlt5Iv10d": 25.2,
        "exErnDlt5Iv20d": 23.07,
        "exErnDlt5Iv30d": 22.58,
        "exErnDlt5Iv60d": 21.58,
        "exErnDlt5Iv90d": 21.34,
        "exErnDlt5Iv6m": 21.2,
        "exErnDlt5Iv1y": 21.2,
        "dlt25Iv10d": 35.86,
        "dlt25Iv20d": 32.92,
        "dlt25Iv30d": 30.37,
        "dlt25Iv60d": 25.88,
        "dlt25Iv90d": 25.54,
        "dlt25Iv6m": 24.69,
        "dlt25Iv1y": 24.51,
        "exErnDlt25Iv10d": 24.73,
        "exErnDlt25Iv20d": 23.45,
        "exErnDlt25Iv30d": 23.86,
        "exErnDlt25Iv60d": 22.54,
        "exErnDlt25Iv90d": 22.07,
        "exErnDlt25Iv6m": 21.7,
        "exErnDlt25Iv1y": 22.24,
        "dlt75Iv10d": 41.55,
        "dlt75Iv20d": 39.07,
        "dlt75Iv30d": 36.43,
        "dlt75Iv60d": 32.05,
        "dlt75Iv90d": 31.51,
        "dlt75Iv6m": 30.34,
        "dlt75Iv1y": 30.24,
        "exErnDlt75Iv10d": 30.41,
        "exErnDlt75Iv20d": 29.6,
        "exErnDlt75Iv30d": 29.93,
        "exErnDlt75Iv60d": 28.71,
        "exErnDlt75Iv90d": 28.04,
        "exErnDlt75Iv6m": 27.35,
        "exErnDlt75Iv1y": 27.97,
        "dlt95Iv10d": 51.14,
        "dlt95Iv20d": 49.39,
        "dlt95Iv30d": 43.48,
        "dlt95Iv60d": 39.75,
        "dlt95Iv90d": 39.88,
        "dlt95Iv6m": 38.41,
        "dlt95Iv1y": 36.32,
        "exErnDlt95Iv10d": 40.01,
        "exErnDlt95Iv20d": 39.92,
        "exErnDlt95Iv30d": 36.98,
        "exErnDlt95Iv60d": 36.41,
        "exErnDlt95Iv90d": 36.41,
        "exErnDlt95Iv6m": 35.42,
        "exErnDlt95Iv1y": 34.05,
        "fwd30_20": 26.49,
        "fwd60_30": 23.36,
        "fwd90_60": 27.26,
        "fwd180_90": 26.09,
        "fwd90_30": 25.38,
        "fexErn30_20": 26.68,
        "fexErn60_30": 23.88,
        "fexErn90_60": 23.52,
        "fexErn180_90": 23.61,
        "fexErn90_30": 23.7,
        "ffwd30_20": 20.7,
        "ffwd60_30": 17.88,
        "ffwd90_60": 26.46,
        "ffwd180_90": 24.7,
        "ffwd90_30": 21.55,
        "ffexErn30_20": 27.46,
        "ffexErn60_30": 22.48,
        "ffexErn90_60": 22.21,
        "ffexErn180_90": 22.91,
        "ffexErn90_30": 22.34,
        "fbfwd30_20": 0.781647,
        "fbfwd60_30": 0.765352,
        "fbfwd90_60": 0.9706,
        "fbfwd180_90": 0.946864,
        "fbfwd90_30": 0.848832,
        "fbfexErn30_20": 1.0294,
        "fbfexErn60_30": 0.941347,
        "fbfexErn90_60": 0.944504,
        "fbfexErn180_90": 0.9706,
        "fbfexErn90_30": 0.942647,
        "impliedEarningsMove": 4.78,
        "updatedAt": "2022-07-11T20:47:03Z",
    }


def iv_rank_data_definition(ticker: str = "IBM") -> Dict[str, Any]:
    today = datetime.date.today()
    updated = datetime.datetime.now()
    return {
        "ticker": ticker,
        "tradeDate": str(today),
        "iv": 100 * random.random(),
        "ivRank1m": 100 * random.random(),
        "ivPct1m": 100 * random.random(),
        "ivRank1y": 100 * random.random(),
        "ivPct1y": 100 * random.random(),
        "updatedAt": f"{updated}Z",
    }


def daily_price_data_definition(ticker: str = "IBM") -> Dict[str, Any]:
    today = datetime.date.today()
    updated = datetime.datetime.now()
    close_price = 100 + 65 * random.random()
    high_price = close_price + 4 * random.random()
    low_price = close_price - 4 * random.random()
    open_price = close_price + 8 * (random.random())
    volume = 1e7 * (1 + random.random())
    adjustment = random.random()
    return {
        "ticker": ticker,
        "tradeDate": str(today),
        "clsPx": close_price,
        "hiPx": high_price,
        "loPx": low_price,
        "open": open_price,
        "stockVolume": 1e7 * (1 + random.random()),
        "unadjClsPx": adjustment * close_price,
        "unadjHiPx": adjustment * high_price,
        "unadjLoPx": adjustment * low_price,
        "unadjOpen": adjustment * open_price,
        "unadjStockVolume": adjustment * volume,
        "updatedAt": f"{updated}Z",
    }


def historical_volatility_data_definition() -> Dict[str, Any]:
    return {
        "ticker": "IBM",
        "tradeDate": "2006-01-05",
        "orHv1d": 23.01,
        "orHv5d": 23.01,
        "orHv10d": 23.01,
        "orHv20d": 23.01,
        "orHv30d": 23.01,
        "orHv60d": 23.01,
        "orHv90d": 23.01,
        "orHv100d": 23.01,
        "orHv120d": 23.01,
        "orHv252d": 23.01,
        "orHv500d": 23.01,
        "orHv1000d": 23.01,
        "clsHv5d": 0,
        "clsHv10d": 0,
        "clsHv20d": 0,
        "clsHv30d": 0,
        "clsHv60d": 0,
        "clsHv90d": 0,
        "clsHv100d": 0,
        "clsHv120d": 0,
        "clsHv252d": 0,
        "clsHv500d": 0,
        "clsHv1000d": 0,
        "orHvXern5d": 23.01,
        "orHvXern10d": 23.01,
        "orHvXern20d": 23.01,
        "orHvXern30d": 23.01,
        "orHvXern60d": 23.01,
        "orHvXern90d": 23.01,
        "orHvXern100d": 23.01,
        "orHvXern120d": 23.01,
        "orHvXern252d": 23.01,
        "orHvXern500d": 23.01,
        "orHvXern1000d": 23.01,
        "clsHvXern5d": 0,
        "clsHvXern10d": 0,
        "clsHvXern20d": 0,
        "clsHvXern30d": 0,
        "clsHvXern60d": 0,
        "clsHvXern90d": 0,
        "clsHvXern100d": 0,
        "clsHvXern120d": 0,
        "clsHvXern252d": 0,
        "clsHvXern500d": 0,
        "clsHvXern1000d": 0,
        "updatedAt": "2018-06-07T19:28:17Z",
    }


def dividend_history_data_definition(ticker="IMB") -> Dict[str, Any]:
    today = datetime.date.today()
    return {
        "ticker": ticker,
        "exDate": today,
        "divAmt": 1.5 * random.random(),
        "divFreq": "4",
        "declaredDate": today - datetime.timedelta(days=15),
    }


def earnings_history_data_definition(ticker="IMB") -> Dict[str, Any]:
    today = datetime.date.today()
    updated = datetime.datetime.now()
    return {
        "ticker": ticker,
        "earnDate": str(today),
        "anncTod": "1630",
        "updatedAt": f"{updated}Z",
    }


def stock_split_history_data_definition(ticker="UVXY") -> Dict[str, Any]:
    today = datetime.date.today()
    return {
        "ticker": ticker,
        "splitDate": str(today),
        "divisor": 0.1 * random.random(),
    }


def endpoint(resource, count=1):
    return {"data": [resource() for _ in range(count)]}


# TODO: Use mapping of Request types to Response types
_endpoints = {
    "tickers": endpoint(ticker_data_definition),
    "strikes": endpoint(strike_data_definition),
    "hist/strikes": endpoint(strike_data_definition),
    "strikes/options": endpoint(strike_data_definition),
    "hist/strikes/options": endpoint(strike_data_definition),
    "monies/implied": endpoint(money_implied_data_definition),
    "monies/forecast": endpoint(money_forecast_data_definition),
    "hist/monies/implied": endpoint(money_implied_data_definition),
    "hist/monies/forecast": endpoint(money_forecast_data_definition),
    "summaries": endpoint(summary_data_definition),
    "hist/summaries": endpoint(summary_data_definition),
    "cores": endpoint(core_data_definition),
    "hist/cores": endpoint(core_data_definition),
    "hist/dailies": endpoint(daily_price_data_definition),
    "hist/hvs": endpoint(historical_volatility_data_definition),
    "hist/divs": endpoint(dividend_history_data_definition),
    "hist/earnings": endpoint(earnings_history_data_definition),
    "hist/splits": endpoint(stock_split_history_data_definition),
    "ivrank": endpoint(iv_rank_data_definition),
    "hist/ivrank": endpoint(iv_rank_data_definition),
}
