from aiogram import types
from aiogram import Router
from aiogram.filters import Text
from config import config
from aiogram.fsm.context import FSMContext
from fsm.states import States
from database.db_sqlite import set_language
from database.db_sqlite import get_language
import lexicon
from keyboards import main_menu

router = Router()


@router.callback_query(Text(text="Ru"))
@router.callback_query(Text(text="En"))
async def choose_language(call: types.CallbackQuery, state: FSMContext = None):
    await call.message.delete()
    if call.data == "Ru":
        await call.message.answer(f"_Выбран русский язык_")
    else:
        await call.message.answer("_English language chosen_")
    await set_language(config.load_config().db.db_file_name, call.from_user.id, call.data)
    lang = await get_language(config.load_config().db.db_file_name, call.from_user.id)
    if lang == "Ru":
        lang_file = lexicon.russian
    else:
        lang_file = lexicon.english
    await call.message.answer(text=lang_file.lexicon["Choose menu"], reply_markup=await main_menu.create_main_kb(lang_file))
    await state.set_state(States.start_state)


