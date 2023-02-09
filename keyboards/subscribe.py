from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def create_subscribe_kb(language):
    button1: InlineKeyboardButton = InlineKeyboardButton(text=language.lexicon["Choose action"],
                                                         callback_data="Subscribe")
    button2: InlineKeyboardButton = InlineKeyboardButton(text=language.lexicon["Cancel"],
                                                         callback_data="Main")
    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button1], [button2]])

    return keyboard
