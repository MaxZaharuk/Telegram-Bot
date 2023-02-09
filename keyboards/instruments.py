from aiogram.utils.keyboard import InlineKeyboardBuilder


main_symbols = {"EUR", "USD"}
secondary_straight = {"CHF", "JPY", "CAD"}
secondary_reverse = {"GBP", "AUD", "RUB"}


async def create_FX_symbols(language):
    builder1 = InlineKeyboardBuilder()
    for main in main_symbols:
        for secondary in secondary_straight:
            builder1.button(text=f"{main}{secondary}", callback_data=f"{main}{secondary}")
        for secondary in secondary_reverse:
            if main == "USD":
                builder1.button(text=f"{secondary}{main}", callback_data=f"{secondary}{main}")
            else:
                builder1.button(text=f"{main}{secondary}", callback_data=f"{main}{secondary}")
    builder1.button(text=language.lexicon["Back"], callback_data="Back")
    builder1.adjust(3)
    return builder1.as_markup()


digital = {"BTC", "ETC", "DOGE"}


async def create_digital_symbols(language):
    builder2 = InlineKeyboardBuilder()
    for digit in digital:
        builder2.button(text=f"{digit}USD", callback_data=f"{digit}USD")

    builder2.button(text=language.lexicon["Back"], callback_data="Back")
    builder2.adjust(3)
    return builder2.as_markup()



