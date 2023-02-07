import requests
from config.config import load_config

querystring_quotes = {"from_symbol": "EUR",
                      "function": "FX_DAILY",
                      "to_symbol": "USD",
                      "outputsize": "compact",
                      "datatype": "json"}

querystring_indicator = {"time_period": "200",
                         "interval": "5min",
                         "series_type": "close",
                         "function": "SMA",
                         "symbol": "MSFT",
                         "datatype": "json"}

headers = {
    "X-RapidAPI-Key": load_config().rapid_api.rapid_api_key,
    "X-RapidAPI-Host": load_config().rapid_api.rapid_api_host
}

url = f"https://{headers[1]}/query"


async def create_quote_query(symbol1, symbol2, func):
    new_query = querystring_quotes
    new_query["from_symbol"] = symbol1
    new_query["function"] = func
    new_query["to_symbol"] = symbol2
    return new_query


async def create_indicator_query(symbol, time_serie, func):
    new_query_indicator = querystring_indicator
    new_query_indicator["interval"] = time_serie
    new_query_indicator["function"] = func
    new_query_indicator["to_symbol"] = symbol2
    return new_query_indicator


async def make_request(query):
    response = requests.request("GET", url, headers=headers, params=query)
    return response

