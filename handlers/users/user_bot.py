from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes, ReplyKeyboardRemove
import asyncpg

from loader import dp, db, bot
from states.states import user_states
from keyboards.inline.confirmation import confirmation_keyboard
from data.config import ADMINS
from keyboards.default import add


# ADD FILE

@dp.message_handler(text="Qo'shish +", state=user_states.start)
async def send_welcome(message: types.Message):
    await message.answer("Istagan ma'lumot turini menga jo'nating 🙂...", reply_markup=ReplyKeyboardRemove())
    await user_states.set_val.set()


@dp.message_handler(state=user_states.start, content_types=types.ContentTypes.ANY)
async def send_welcome(message: types.Message):
    await message.answer("Iltimos, ma'lumot qo'shish uchun pastdagi <b>Qo'shish</b> tugmasini bosing. \n\nYoki yordam oling...\n\n/help\n👆", reply_markup=add.add_file)

# VALUE STATE

@dp.message_handler(state=user_states.set_val, content_types=ContentTypes.TEXT)
async def set_val(message: types.Message, state: FSMContext):
    await state.update_data({
        "value": message.text,
        "type": "text"
    })
    # await message.answer(message.text)
    await message.reply("Endi <b>kalit so'z</b> yuboring! \n\nAynan shu kalit so'z orqali bu ma'lumotni chatda jo'natasiz. Shuning uchun, kalit so'zni eslab qoling!")
    await user_states.set_key.set()


@dp.message_handler(state=user_states.set_val, content_types=ContentTypes.AUDIO)
async def set_val(message: types.Message, state: FSMContext):
    value = message.audio.file_id
    await state.update_data({"value": value, "type": "audio"})
    # await message.reply_audio(value)
    await message.reply("Endi <b>kalit so'z</b> yuboring! \n\nAynan shu kalit so'z orqali bu ma'lumotni chatda jo'natasiz. Shuning uchun, kalit so'zni eslab qoling!")
    await user_states.set_key.set()


@dp.message_handler(state=user_states.set_val, content_types=ContentTypes.DOCUMENT)
async def set_val(message: types.Message, state: FSMContext):
    value = message.document.file_id
    await state.update_data({"value": value, "type": "document"})
    # await message.reply_document(value)
    await message.reply("Endi <b>kalit so'z</b> yuboring! \n\nAynan shu kalit so'z orqali bu ma'lumotni chatda jo'natasiz. Shuning uchun, kalit so'zni eslab qoling!")
    await user_states.set_key.set()


@dp.message_handler(state=user_states.set_val, content_types=ContentTypes.ANIMATION)
async def set_val(message: types.Message, state: FSMContext):
    value = message.animation.file_id
    await state.update_data({"value": value, "type": "animation"})
    # await message.reply_animation(value)
    await message.reply("Endi <b>kalit so'z</b> yuboring! \n\nAynan shu kalit so'z orqali bu ma'lumotni chatda jo'natasiz. Shuning uchun, kalit so'zni eslab qoling!")
    await user_states.set_key.set()


@dp.message_handler(state=user_states.set_val, content_types=ContentTypes.CONTACT)
async def set_val(message: types.Message, state: FSMContext):
    # value = message.contact
    # await state.update_data({"value": value})
    # await message.reply_contact(phone_number=value.phone_number, first_name=value.first_name, protect_content=False, allow_sending_without_reply=False)
    # await message.answer("Endi kalit so'z yuboring!")
    # await user_states.set_key.set()
    await message.answer("Bu ma'lumot turini qo'shish mumkin emas. Iltimos, boshqa ma'lumot turini jo'nating...")


@dp.message_handler(state=user_states.set_val, content_types=ContentTypes.VOICE)
async def set_val(message: types.Message, state: FSMContext):
    value = message.voice.file_id
    await state.update_data({"value": value, "type": "voice"})
    # await message.reply_voice(value)
    await message.reply("Endi <b>kalit so'z</b> yuboring! \n\nAynan shu kalit so'z orqali bu ma'lumotni chatda jo'natasiz. Shuning uchun, kalit so'zni eslab qoling!")
    await user_states.set_key.set()


@dp.message_handler(state=user_states.set_val, content_types=ContentTypes.VIDEO)
async def set_val(message: types.Message, state: FSMContext):
    value = message.video.file_id
    await state.update_data({"value": value, "type": "video"})
    # await message.reply_video(value)
    await message.reply("Endi <b>kalit so'z</b> yuboring! \n\nAynan shu kalit so'z orqali bu ma'lumotni chatda jo'natasiz. Shuning uchun, kalit so'zni eslab qoling!")
    await user_states.set_key.set()


@dp.message_handler(state=user_states.set_val, content_types=ContentTypes.LOCATION)
async def set_val(message: types.Message, state: FSMContext):
    value = f"{message.location.latitude}" + "&" + f"{message.location.longitude}"
    await state.update_data({"value": value, "type": "location"})
    # lat_long = value.split("&")
    # await message.reply_location(latitude=lat_long[0], longitude=lat_long[1])
    await message.reply("Endi <b>kalit so'z</b> yuboring! \n\nAynan shu kalit so'z orqali bu ma'lumotni chatda jo'natasiz. Shuning uchun, kalit so'zni eslab qoling!")
    await user_states.set_key.set()


@dp.message_handler(state=user_states.set_val, content_types=ContentTypes.PHOTO)
async def set_val(message: types.Message, state: FSMContext):
    value = message.photo[-1].file_id
    await state.update_data({"value": value, "type": "photo"})
    # await message.reply_photo(value, caption="Here is your photo")
    await message.reply("Endi <b>kalit so'z</b> yuboring! \n\nAynan shu kalit so'z orqali bu ma'lumotni chatda jo'natasiz. Shuning uchun, kalit so'zni eslab qoling!")
    await user_states.set_key.set()


@dp.message_handler(state=user_states.set_val, content_types=ContentTypes.STICKER)
async def set_val(message: types.Message, state: FSMContext):
    value = message.sticker.file_id
    await state.update_data({"value": value, "type": "sticker"})
    # await message.reply_sticker(value)
    await message.reply("Endi <b>kalit so'z</b> yuboring! \n\nAynan shu kalit so'z orqali bu ma'lumotni chatda jo'natasiz. Shuning uchun, kalit so'zni eslab qoling!")
    await user_states.set_key.set()


@dp.message_handler(state=user_states.set_val, content_types=ContentTypes.ANY)
async def set_val(message: types.Message):
    await message.answer("Bu ma'lumot turi saqlab bo'lmaydi...\n\nBoshqa ma'lumot turini jo'nating!")


# KEY STATE

@dp.message_handler(state=user_states.set_key, content_types=ContentTypes.TEXT)
async def set_text(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id
    await state.update_data({
        "key": message.text,
        "telegram_id": telegram_id
    })
    info = await state.get_data()
    data_type = info.get("type")
    value = info.get("value")
    key = info.get("key")
    if data_type == "audio":
        await message.answer_audio(audio=value, caption=f"\nKalit so'z : <b>{key}</b>")
    elif data_type == "text":
        await message.answer(f"Kalit so'z : <b>{key}</b> \n\nTekst : <b>{value}</b>")
    elif data_type == "document":
        await message.answer_document(document=value, thumb=value, caption=f"\nKalit so'z : <b>{key}</b>")
    elif data_type == "animation":
        await message.answer_animation(animation=value, caption=f"Kalit so'z : <b>{key}</b>")
    elif data_type == "voice":
        await message.answer_voice(voice=value, caption=f"Kalit so'z : <b>{key}</b>")
    elif data_type == "location":
        lat_long = value.split("&")
        await message.answer_location(latitude=lat_long[0], longitude=lat_long[1])
        await message.answer(f"Kalit so'z : <b>{key}</b>")
    elif data_type == "photo":
        await message.answer_photo(photo=value, caption=f"Kalit so'z : <b>{key}</b>")
    elif data_type == "sticker":
        await message.answer_sticker(sticker=value)
        await message.answer(f"Kalit so'z : <b>{key}</b>")
    await message.answer(f"Endi ma'lumot va kalit so'zni tasdiqlang!", reply_markup=confirmation_keyboard)
    await user_states.confirmation.set()


@dp.message_handler(state=user_states.set_key, content_types=ContentTypes.ANY)
async def set_text(message: types.Message):
    await message.answer("Kalit so'z faqatgina tekst formatida bo'lishi mumkin! \n\nItimos, faqatgina tekst jo'nating!")



# CONFIRMATION STATE

@dp.callback_query_handler(state=user_states.confirmation, text="edit")
async def confirm_callback(call: types.CallbackQuery):
    await call.message.answer("Qaytadan boshlaymizmi? \n\nOk! \n\nIstagan ma'lumot turini menga jo'nating 🙂...")
    await call.answer(cache_time=60)
    await user_states.set_val.set()


@dp.callback_query_handler(state=user_states.confirmation, text="confirm")
async def confirm_callback(call: types.CallbackQuery, state: FSMContext):
    info = await state.get_data()
    key = info.get("key")
    value = info.get("value")
    telegram_id = info.get("telegram_id")
    data_type = info.get("type")

    try:
        storage = await db.add_info(
            telegram_id=telegram_id,
            key_set=key,
            value_set=value,
            data_type=data_type
        )
    except asyncpg.exceptions.UniqueViolationError:
        storage = await db.select_row(telegram_id=telegram_id)

    count = await db.count_info_rows()
    msg = f"Key '{storage[1]}' from id '{storage[0]}' has been added to storage! We now have {count} rows."
    await bot.send_message(chat_id=ADMINS[0], text=msg)

    await call.message.answer("Ma'lumot muvaffaqiyatli qo'shildi! 🥳 \n\n 👉<b>@chontak_bot kalit so\'z</b>👈 \nshu jumlani Telegramdagi istagan chatga yozish orqali saqlangan ma'lumotni jo'natishingiz mumkin!")
    await call.answer(cache_time=60)
    await user_states.set_val.set()


@dp.message_handler(state=user_states.confirmation, content_types=types.ContentTypes.ANY)
async def confirm_callback(message: types.Message):
    await message.answer("Iltimos, tugmalardan biri bosing.", reply_markup=confirmation_keyboard)


