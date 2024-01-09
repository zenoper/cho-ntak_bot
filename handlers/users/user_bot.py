from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes

from loader import dp
from states.states import user_states
from keyboards.inline.confirmation import confirmation_keyboard

# VALUE STATE

@dp.message_handler(state=user_states.set_val, content_types=ContentTypes.TEXT)
async def set_val(message: types.Message, state: FSMContext):
    await state.update_data({"value": message.text})
    await message.answer(message.text)
    await message.answer("Endi kalit so'z yuboring!")
    await user_states.set_key.set()


@dp.message_handler(state=user_states.set_val, content_types=ContentTypes.AUDIO)
async def set_val(message: types.Message, state: FSMContext):
    value = message.audio.file_id
    await state.update_data({"value": value})
    await message.reply_audio(value)
    await message.answer("Endi kalit so'z yuboring!")
    await user_states.set_key.set()


@dp.message_handler(state=user_states.set_val, content_types=ContentTypes.DOCUMENT)
async def set_val(message: types.Message, state: FSMContext):
    value = message.document.file_id
    await state.update_data({"value": value})
    await message.reply_document(value)
    await message.answer("Endi kalit so'z yuboring!")
    await user_states.set_key.set()


@dp.message_handler(state=user_states.set_val, content_types=ContentTypes.ANIMATION)
async def set_val(message: types.Message, state: FSMContext):
    value = message.animation.file_id
    await state.update_data({"value": value})
    await message.reply_animation(value)
    await message.answer("Endi kalit so'z yuboring!")
    await user_states.set_key.set()


@dp.message_handler(state=user_states.set_val, content_types=ContentTypes.CONTACT)
async def set_val(message: types.Message, state: FSMContext):
    # value = message.contact
    # await state.update_data({"value": value})
    # await message.reply_contact(phone_number=value.phone_number, first_name=value.first_name, protect_content=False, allow_sending_without_reply=False)
    # await message.answer("Endi kalit so'z yuboring!")
    # await user_states.set_key.set()
    await message.answer("Contakt jo'natmang! Bu funksiya ishlamaydi...")


@dp.message_handler(state=user_states.set_val, content_types=ContentTypes.VOICE)
async def set_val(message: types.Message, state: FSMContext):
    value = message.voice.file_id
    await state.update_data({"value": value})
    await message.reply_voice(value)
    await message.answer("Endi kalit so'z yuboring!")
    await user_states.set_key.set()


@dp.message_handler(state=user_states.set_val, content_types=ContentTypes.LOCATION)
async def set_val(message: types.Message, state: FSMContext):
    value = f"{message.location.latitude}" + "&" + f"{message.location.longitude}"
    await state.update_data({"value": value})
    lat_long = value.split("&")
    await message.reply_location(latitude=lat_long[0], longitude=lat_long[1])
    await message.answer("Endi kalit so'z yuboring!")
    await user_states.set_key.set()


@dp.message_handler(state=user_states.set_val, content_types=ContentTypes.PHOTO)
async def set_val(message: types.Message, state: FSMContext):
    value = message.photo[-1].file_id
    await state.update_data({"value": value})
    await message.reply_photo(value, caption="Here is your photo")
    await message.answer("Endi kalit so'z yuboring!")
    await user_states.set_key.set()


@dp.message_handler(state=user_states.set_val, content_types=ContentTypes.STICKER)
async def set_val(message: types.Message, state: FSMContext):
    value = message.sticker.file_id
    await state.update_data({"value": value})
    await message.reply_sticker(value)
    await message.answer("Endi kalit so'z yuboring!")
    await user_states.set_key.set()


@dp.message_handler(state=user_states.set_val, content_types=ContentTypes.ANY)
async def set_val(message: types.Message):
    await message.answer("Xohlagan narsangizni jo'nating! photo, text, video, document. Farqi yo'q")


# KEY STATE

@dp.message_handler(state=user_states.set_key, content_types=ContentTypes.TEXT)
async def set_text(message: types.Message, state: FSMContext):
    await state.update_data({"key": message.text})
    await message.answer("Endi tasdiqlang!", reply_markup=confirmation_keyboard)
    await user_states.confirmation.set()


@dp.message_handler(state=user_states.set_key, content_types=ContentTypes.ANY)
async def set_text(message: types.Message):
    await message.answer("Kalit so'z faqatgina text bo'la oladi halos!")



# CONFIRMATION STATE

@dp.callback_query_handler(state=user_states.confirmation, text="edit")
async def confirm_callback(call: types.CallbackQuery):
    await call.message.answer("Xohlagan narsangizni jo'nating! photo, text, video, document. Farqi yo'q")
    await call.answer(cache_time=60)
    await user_states.set_val.set()


@dp.callback_query_handler(state=user_states.confirmation, text="confirm")
async def confirm_callback(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Bo'ldi hammasi tayyor. Endi siz topa olasiz")
    await call.answer(cache_time=60)
    await user_states.set_val.set()
