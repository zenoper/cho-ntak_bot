from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from loader import dp, db, bot
from states.states import delete_states, user_states


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
        await message.answer("Qaysi ma'lumotni o'chirishni istaysiz?", reply_markup=delete_info)
    else:
        await message.answer("Sizda hozircha hech qanday ma'lumotlar saqlamagansiz. \n\nMa'lumot qo'shish uchun /add buyrug'ini bering")
        await user_states.start.set()


@dp.callback_query_handler(state=delete_states.select)
async def delete(call: CallbackQuery):
    callback_data = call.data
    row = await db.select_row(telegram_id=call.from_user.id, key_set=str(callback_data))
    if row:
        delete_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="o'chirish", callback_data=row[1])
                ],
            ]
        )
        if row[3] == "audio":
            await call.message.answer_audio(audio=row[2], caption=f"Kalit so'z : {row[1]}", reply_markup=delete_keyboard)
            await delete_states.delete.set()
        elif row[3] == "text":
            await call.message.answer(f"Kalit so'z : {row[1]} \n\nTekst : {row[2]}", reply_markup=delete_keyboard)
            await delete_states.delete.set()
        elif row[3] == "document":
            await call.message.answer_document(document=row[2], thumb=row[2], caption=f"Kalit so'z : {row[1]}", reply_markup=delete_keyboard)
            await delete_states.delete.set()
        elif row[3] == "animation":
            await call.message.answer_animation(animation=row[2], caption=f"Kalit so'z : {row[1]}", reply_markup=delete_keyboard)
        elif row[3] == "voice":
            await call.message.answer_voice(voice=row[2], caption=f"Kalit so'z : {row[1]}", reply_markup=delete_keyboard)
        elif row[3] == "location":
            lat_long = row[2].split("&")
            await call.message.answer_location(latitude=lat_long[0], longitude=lat_long[1], reply_markup=delete_keyboard)
            await call.message.answer(f"Kalit so'z : {row[1]}")
        elif row[3] == "photo":
            await call.message.answer_photo(photo=row[2], caption=f"Kalit so'z : {row[1]}", reply_markup=delete_keyboard)
        elif row[3] == "sticker":
            await call.message.answer_sticker(sticker=row[2], reply_markup=delete_keyboard)
            await call.message.answer(f"Kalit so'z : {row[1]}")

        await delete_states.delete.set()
    else:
        await call.answer("Iltimos, tugmalardan birini tanlang!")


@dp.callback_query_handler(state=delete_states.delete)
async def delete(call: CallbackQuery):
    try:
        await db.delete_info(telegram_id=call.from_user.id, key_set=call.data)
        await call.message.answer("O'chirish muvaffaqiyatli amalga oshdi! \n\nMa'lumot qo'shish uchun : /add \n\nMa'lumot o'chirish uchun : /delete \n\n Yordam olish uchun : /help")
        await user_states.start.set()
    except Exception as e:
        await call.message.answer("O'chirish amalga oshmadi. Uzr :( \n\nQaytadan harakat qilib ko'ring : /delete")
        print(e)
