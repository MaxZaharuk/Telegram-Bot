import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import pandas as pd
import matplotlib.dates as mpl_dates
import os


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
    prices = pd.DataFrame({
        "date": date,
        "open": open,
        "close": close,
        "high": high,
        "low": low
    })
    ohlc = prices.loc[:, ['date', 'open', 'high', 'low', 'close']]
    ohlc['date'] = pd.to_datetime(ohlc['date'])
    ohlc['date'] = ohlc['date'].apply(mpl_dates.date2num)
    ohlc = ohlc.astype(float)
    fig, ax = plt.subplots()

    candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='blue',
                     colordown='green', alpha=0.4)

    date_format = mpl_dates.DateFormatter('%d-%m-%Y')
    ax.xaxis.set_major_formatter(date_format)
    ax.minorticks_on()
    ax.grid(which='major',
            color='k',
            linewidth=0.5)
    ax.grid(which='minor',
            color='k',
            linestyle=':')
    ax.set_title(response["Meta Data"]['2. From Symbol'] + response["Meta Data"]['3. To Symbol'] + " " + time_frame)
    fig.autofmt_xdate()
    fig.tight_layout()
    path = os.path.join(os.path.abspath('plots'), 'temp.png')
    plt.savefig(os.path.join(os.path.abspath('plots'), 'temp.png'))
    return path


async def make_technical_quote(response, indicator):
    date = []
    price = []
    for key, value in response[f"Technical Analysis: {indicator}"].items():
        date.append(key)
        price.append(float(value[f"{indicator}"]))
    prices = pd.DataFrame({
        'date': date,
        'price': price
    })
    prices['date'] = pd.to_datetime(prices['date'])
    fig, ax = plt.subplots()
    date_format = mpl_dates.DateFormatter('%d-%m-%Y')
    ax.xaxis.set_major_formatter(date_format)
    ax.set_title(f'{response["Meta Data"]["1: Symbol"]} - {indicator}')
    ax.autoscale_view()
    ax.plot(prices['date'], prices['price'], color="blue")
    ax.minorticks_on()
    ax.grid(which='major',
            color='k',
            linewidth=0.5)
    ax.grid(which='minor',
            color='k',
            linestyle=':')
    fig.autofmt_xdate()
    fig.tight_layout()
    path = os.path.join(os.path.abspath('plots'), 'temp.png')
    plt.savefig(os.path.join(os.path.abspath('plots'), 'temp.png'))
    return path
