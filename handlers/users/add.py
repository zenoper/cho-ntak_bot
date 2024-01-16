from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from loader import dp
from states.states import user_states


@dp.message_handler(Command(["add"]), state="*")
async def add(message: types.Message):
    await message.answer("Istagan ma'lumot turini menga jo'nating...", reply_markup=types.ReplyKeyboardRemove())
    await user_states.set_val.set()