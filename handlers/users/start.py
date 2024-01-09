from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from states.states import user_states


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
    await message.answer("Xohlagan narsangizni jo'nating! photo, text, video, document. Farqi yo'q")
    await user_states.set_val.set()

