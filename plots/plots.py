import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import pandas as pd
import matplotlib.dates as mpl_dates
import numpy as np
import datetime
import json


async def make_quote_plot(response, market_type, time_frame):
    date = []
    open = []
    close = []
    high = []
    low = []
    for key, value in response[f"Time Series {market_type} ({time_frame})"].items():
        date.append(key)
        open.append(value["1. open"])
        high.append(value["2. high"])
        low.append(value["3. low"])
        close.append(value["4. close"])
    prices = await pd.DataFrame({
        "date": date,
        "open": open,
        "close": close,
        "high": high,
        "low": low
    })
    ohlc = await prices.loc[:, ['date', 'open', 'high', 'low', 'close']]
    ohlc['date'] = await pd.to_datetime(ohlc['date'])
    ohlc['date'] = await ohlc['date'].apply(mpl_dates.date2num)
    ohlc = await ohlc.astype(float)
    fig, ax = plt.subplots()

    candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='blue',
                     colordown='green', alpha=0.4)

    date_format = mpl_dates.DateFormatter('%d-%m-%Y')
    await ax.xaxis.set_major_formatter(date_format)
    await fig.autofmt_xdate()

    await fig.tight_layout()

    return await plt.show()


