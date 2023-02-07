from aiogram import Router
from aiogram.filters import Text

router = Router()


@router.callback_query(Text(text="Day"))
async def choose_mode():
    pass

