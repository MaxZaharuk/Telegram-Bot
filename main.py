import logging
import sys
import asyncio
from aiogram import Bot, Dispatcher

from config.config import load_config
from handlers import commands, any_message
from handlers import start_language
from handlers import symbols
from handlers import chose_tf
from handlers import get_plots
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from database import db_sqlite

storage = MemoryStorage() if not load_config().redis.use else RedisStorage.from_url(load_config().redis.host)
bot: Bot = Bot(load_config().tg_bot.token, parse_mode='MarkdownV2')
dp: Dispatcher = Dispatcher(storage=storage)


dp.include_router(commands.router)
dp.include_router(start_language.router)
dp.include_router(symbols.router)
dp.include_router(chose_tf.router)
dp.include_router(get_plots.router)
dp.include_router(any_message.router)
asyncio.run(db_sqlite.start_db(load_config().db.db_file_name))

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    dp.run_polling(bot)

