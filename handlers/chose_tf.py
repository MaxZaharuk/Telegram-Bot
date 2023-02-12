from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

import keyboards.time_frame
import lexicon
from config.config import load_config
from database import db_sqlite
from fsm.states import States

router = Router()


@router.callback_query(Text(text="USDCAD"))
@router.callback_query(Text(text="USDJPY"))
@router.callback_query(Text(text="USDCHF"))
@router.callback_query(Text(text="AUDUSD"))
@router.callback_query(Text(text="RUBUSD"))
@router.callback_query(Text(text="GBPUSD"))
@router.callback_query(Text(text="EURCAD"))
@router.callback_query(Text(text="EURJPY"))
@router.callback_query(Text(text="EURCHF"))
@router.callback_query(Text(text="EURAUD"))
@router.callback_query(Text(text="EURRUB"))
@router.callback_query(Text(text="EURGBP"))
@router.callback_query(Text(text="ETCUSD"))
@router.callback_query(Text(text="DOGEUSD"))
@router.callback_query(Text(text="BTCUSD"))
async def choose_fx_instrument(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.update_data(chosen_symbol=call.data)
    lang = await db_sqlite.get_language(load_config().db.db_file_name, call.from_user.id)
    if lang == "Ru":
        lang_file = lexicon.russian
    else:
        lang_file = lexicon.english
    kb = await keyboards.time_frame.create_kb_timeseries(lang_file)
    await call.message.answer(text=lang_file.lexicon["Choose TF"], reply_markup=kb)
    await state.set_state(States.choose_mode)


# @router.callback_query(Text(text="ETCUSD"))
# @router.callback_query(Text(text="DOGEUSD"))
# @router.callback_query(Text(text="BTCUSD"))
# async def choose_digital_instrument(call: CallbackQuery, state: FSMContext):
#     await call.message.delete()
#     await state.update_data(chosen_symbol=call.data)
#     lang = await db_sqlite.get_language(load_config().db.db_file_name, call.from_user.id)
#     if lang == "Ru":
#         lang_file = lexicon.russian
#     else:
#         lang_file = lexicon.english
#     kb = await keyboards.time_frame.create_kb_timeseries(lang_file)
#     await call.message.answer(text=lang_file.lexicon["Choose TF"], reply_markup=kb)
#     await state.set_state(States.choose_mode)
