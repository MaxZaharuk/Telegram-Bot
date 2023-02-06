from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button_1: InlineKeyboardButton = InlineKeyboardButton(
                                    text='Русский',
                                    callback_data='Ru')

button_2: InlineKeyboardButton = InlineKeyboardButton(
                                    text='English',
                                    callback_data='En')


keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[
    [
        button_1
    ],
    [
        button_2
    ]
])
