from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def create_kb_timeseries(language_file):
    button1: InlineKeyboardButton = InlineKeyboardButton(
                                                        text=language_file.lexicon["Daily"],
                                                        callback_data='Daily')
    button2: InlineKeyboardButton = InlineKeyboardButton(
                                                        text=language_file.lexicon["Weekly"],
                                                        callback_data='Weekly')
    button3: InlineKeyboardButton = InlineKeyboardButton(
                                                        text=language_file.lexicon["Monthly"],
                                                        callback_data='Monthly')
    button4: InlineKeyboardButton = InlineKeyboardButton(text=language_file.lexicon["Cancel"],
                                                         callback_data="Back")

    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[
        [button1], [button2], [button3],
        [button4]
    ])
    return keyboard
