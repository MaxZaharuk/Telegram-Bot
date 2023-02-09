from aiogram import Router, types
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types.input_file import FSInputFile
import keyboards.subscribe
import lexicon
from api import request_quotes
from config.config import load_config
from database import db_sqlite
from fsm.states import States
from plots import plots
import os

router = Router()


@router.callback_query(Text(text="Daily"))
@router.callback_query(Text(text="Weekly"))
@router.callback_query(Text(text="Monthly"))
async def show_plots(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.update_data(chosen_tf=call.data)
    lang = await db_sqlite.get_language(load_config().db.db_file_name, call.from_user.id)
    if lang == "Ru":
        lang_file = lexicon.russian
    else:
        lang_file = lexicon.english
    kb = await keyboards.subscribe.create_subscribe_kb(lang_file)
    data = await state.get_data()
    func = f"{data['chosen_mode']}_{data['chosen_tf']}"
    symbol1 = data["chosen_symbol"][:3]
    symbol2 = data["chosen_symbol"][3:]
    query = await request_quotes.create_quote_query(func=func,
                                              symbol1=symbol1,
                                              symbol2=symbol2)
    response = await request_quotes.make_request(query)
    path = await plots.make_quote_plot(response=response, market_type=data["chosen_mode"], time_frame=data["chosen_tf"])
    input_file = FSInputFile(path)
    await call.message.answer_photo(input_file)
    os.remove(path)
    await call.message.answer(text=lang_file.lexicon["Choose action"], reply_markup=kb)
    query = await request_quotes.create_indicator_query(data["chosen_symbol"],
                                                        time_serie=data["chosen_tf"],
                                                        func="SMA")
    response = await request_quotes.make_request(query)
    path = await plots.make_technical_quote(response=response, indicator="SMA")
    input_file = FSInputFile(path)
    await call.message.answer_photo(input_file)
    os.remove(path)
    await state.set_state(States.time_series)

