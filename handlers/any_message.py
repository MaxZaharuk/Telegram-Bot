from aiogram import Router, types

import keyboards.main_menu
import lexicon
from config.config import load_config
from database import db_sqlite

router = Router()


@router.message()
async def any_text(message: types.Message):
    lang = await db_sqlite.get_language(load_config().db.db_file_name, message.from_user.id)
    if lang == "Ru":
        lang_file = lexicon.russian
    else:
        lang_file = lexicon.english
    kb = await keyboards.main_menu.create_main_kb(lang_file)
    await message.answer(text=lang_file.lexicon["Any"],
                         reply_markup=kb)
