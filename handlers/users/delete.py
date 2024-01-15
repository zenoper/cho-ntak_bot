from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from loader import dp, db, bot
from states.states import delete_states


@dp.message_handler(Command(["delete"]), state="*")
async def remove(message: types):
    await delete_states.select.set()
    rows = await db.select_rows(telegram_id=message.from_user.id)
    if rows:
        delete_info = InlineKeyboardMarkup(
            inline_keyboard=[

            ]
        )
        for row in rows:
            delete_info.inline_keyboard.append([
                    InlineKeyboardButton(text=row[1], callback_data=row[1])
                ],)
        await message.answer("Qaysi birini o'chirishni istaysiz?", reply_markup=delete_info)
    else:
        await message.answer("Sizda, hozircha saqlangan hech qanday record'lar yo'q")


@dp.callback_query_handler(state=delete_states.select)
async def delete(call: CallbackQuery):
    callback_data = call.data
    row = await db.select_row(telegram_id=call.from_user.id, key_set=str(callback_data))
    print(row)
    if row:
        delete_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="o'chirish", callback_data=row[1])
                ],
            ]
        )
        if row[3] == "audio":
            await call.message.answer_audio(audio=row[2], caption=row[1], reply_markup=delete_keyboard)
            await delete_states.delete.set()
    else:
        await call.answer("Iltimos, tugmalardan birini tanlang!")


@dp.callback_query_handler(state=delete_states.delete)
async def delete(call: CallbackQuery):
    print(call.data)
    try:
        await db.delete_info(telegram_id=call.from_user.id, key_set=call.data)
        await call.message.answer("O'chirish muvaffaqiyatli amalga oshdi!")
    except Exception as e:
        await call.message.answer("O'chirish amalga oshmadi. Uzr :(")
        print(e)
