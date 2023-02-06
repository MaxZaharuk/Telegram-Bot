from aiogram import types
from keyboards import start_menu
from aiogram import Router
from aiogram.filters import Command, Text
from config import config
from aiogram.fsm.context import FSMContext


router = Router()


@router.message(Command("start"))
@router.message(Text(text="start"))
async def command_start(message: types.Message, bot, state: FSMContext = None):
    await bot.send_sticker(chat_id=message.from_user.id, sticker=config.load_config().sticker_hello.sticker)
    await message.reply(f"Привет/Hello, {message.from_user.full_name}\! "
                        f"Выберите язык/Choose language", reply_markup=start_menu.keyboard)
    await state.set_state(None)


@router.message(Command("help"))
@router.message(Text(text="help"))
async def command_help(message: types.Message, state: FSMContext = None):
    await message.reply("Switch language tap /start /Сменить язык нажмите /start")
    await state.set_state(None)


@router.callback_query(Text(text='start'))
async def command_start(call: types.CallbackQuery, bot, state: FSMContext = None):
    await bot.send_sticker(chat_id=call.from_user.id, sticker=config.load_config().sticker_hello.sticker)
    await bot.send_message(chat_id=call.from_user.id, text=f"Привет/Hello, {call.from_user.full_name}\! "
                        f"Выберите язык/Choose language", reply_markup=start_menu.keyboard)
    await state.set_state(None)



