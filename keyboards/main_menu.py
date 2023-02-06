from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def create_main_kb(language_file):
    button1: InlineKeyboardButton = InlineKeyboardButton(text=language_file.lexicon["Forex"], callback_data="FX")
    button2: InlineKeyboardButton = InlineKeyboardButton(text=language_file.lexicon["Crypto"], callback_data="CR")
    button3: InlineKeyboardButton = InlineKeyboardButton(text=language_file.lexicon["Query history"], callback_data="QH")
    button4: InlineKeyboardButton = InlineKeyboardButton(text=language_file.lexicon["Cancel"], callback_data="start")

    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[
                                                                            [button1, button2],
                                                                            [button3, button4]
    ])
    return keyboard
