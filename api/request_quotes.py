import json
import aiohttp
from config.config import load_config


headers = {
    "X-RapidAPI-Key": load_config().rapid_api.rapid_api_key,
    "X-RapidAPI-Host": load_config().rapid_api.rapid_api_url
}


async def create_quote_query(symbol1, symbol2, func):
    querystring_quotes = f"/query?from_symbol={symbol1}&function={func}&" \
                         f"to_symbol={symbol2}&outputsize=compact&datatype=json"
    return querystring_quotes


async def create_digital_query(symbol, time_serie, func):
    querystring_quotes = f"/query?market=USD&symbol={symbol}&function={func}_{time_serie}"
    return querystring_quotes


async def create_indicator_query(symbol, time_serie, func):
    querystring_indicator = f"/query?time_period=200&interval={time_serie.lower()}&series_type=close&" \
                            f"function={func}&symbol={symbol}&datatype=json"
    return querystring_indicator


async def make_request(query):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://{headers['X-RapidAPI-Host']}{query}", headers=headers) as response:
            return json.loads(await response.text())

