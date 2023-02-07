import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import pandas as pd
import matplotlib.dates as mpl_dates
import numpy as np
import datetime
import json


async def make_quote_plot(response, market_type, time_frame):
    data = [[price for price in json.loads(response.text)[f"Time Series {market_type} ({time_frame})"][date]]
            for date in json.loads(response.text)[f"Time Series {market_type} ({time_frame})"]]

