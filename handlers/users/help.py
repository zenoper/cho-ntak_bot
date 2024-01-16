from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp(), state='*')
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni qayta ishga tushirish",
            "/help - Yordam",
            "/add - Yangi ma'lumot qo'shish",
            "/delete - Ma'lumot o'chirish")
    
    await message.answer("\n".join(text))