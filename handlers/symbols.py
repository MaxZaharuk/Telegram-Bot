from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from database import db_sqlite
import lexicon
from config.config import load_config
from fsm.states import States
from keyboards import instruments

router = Router()


@router.callback_query(Text(text="FX"))
async def choose_fx_instrument(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.update_data(chosen_mode=call.data)
    lang = await db_sqlite.get_language(load_config().db.db_file_name, call.from_user.id)
    if lang == "Ru":
        lang_file = lexicon.russian
    else:
        lang_file = lexicon.english
    kb = await instruments.create_FX_symbols(lang_file)
    await call.message.answer(text=lang_file.lexicon["Choose symbol"], reply_markup=kb)
    await state.set_state(States.forex_instrument)


@router.callback_query(Text(text="CR"))
async def choose_digital_instrument(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.update_data(chosen_mode=call.data)
    lang = await db_sqlite.get_language(load_config().db.db_file_name, call.from_user.id)
    if lang == "Ru":
        lang_file = lexicon.russian
    else:
        lang_file = lexicon.english
    kb = await instruments.create_digital_symbols(lang_file)
    await call.message.answer(text=lang_file.lexicon["Choose symbol"], reply_markup=kb)
    await state.set_state(States.digital_instrument)


@router.callback_query(Text(text="QH"))
async def choose_digital_instrument(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.update_data(chosen_mode=call.data)
    lang = await db_sqlite.get_language(load_config().db.db_file_name, call.from_user.id)
    if lang == "Ru":
        lang_file = lexicon.russian
    else:
        lang_file = lexicon.english
    kb = await instruments.create_digital_symbols(lang_file)
    await call.message.answer(text=lang_file.lexicon["Choose symbol"], reply_markup=kb)
    await state.set_state(States.digital_instrument)

