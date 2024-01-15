from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import asyncpg

from loader import dp, db, bot
from states.states import user_states
from data.config import ADMINS
from keyboards.default import add


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message):
    await message.answer(f"Assalamu alaykum, {message.from_user.full_name}!")
    fullname = message.from_user.full_name
    username = message.from_user.username
    telegram_id = message.from_user.id
    try:
        user = await db.add_user(
            full_name=fullname,
            username=username,
            telegram_id=telegram_id,
        )
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=telegram_id)

    count = await db.count_users()
    msg = f"User '{user[1]}' has been added to User's database! We now have {count} users."
    await bot.send_message(chat_id=ADMINS[0], text=msg)

    await message.answer("Cho'ntak bot orqali siz har qanday faylni saqlab, uni telegramdagi ixtiyoriy chatga tezlik bilan jo'natish imkoniga ega bo'lasiz! \n\nFayl qo'shish uchun pastdagi 'qo\'shish' tugmasini bosing va kalit so'z bering.", reply_markup=add.add_file)
    await user_states.start.set()

