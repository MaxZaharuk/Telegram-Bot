import os
from dotenv import load_dotenv
from dataclasses import dataclass


@dataclass
class TgBot:
    token: str


@dataclass
class RapidApi:
    rapid_api_key: str


@dataclass
class DB:
    db_file_name: str


@dataclass
class Stickers:
    sticker: str


@dataclass
class Redis:
    host: str
    use: bool


@dataclass
class Config:
    tg_bot: TgBot
    rapid_api: RapidApi
    db: DB
    redis: Redis
    sticker_hello: Stickers


def load_config():
    if not load_dotenv("BOT_TOKEN"):
        load_dotenv()
    return Config(
        tg_bot=TgBot(token=os.getenv("BOT_TOKEN")),
        rapid_api=RapidApi(rapid_api_key=os.getenv("RAPID_API_KEY")),
        db=DB(db_file_name=os.getenv("DB_FILE_NAME")),
        redis=Redis(host=os.getenv("REDIS_HOST"), use=(os.getenv("REDIS_USE") == True)),
        sticker_hello=Stickers(sticker=os.getenv("STICKER_HELLO"))
    )
