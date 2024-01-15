from aiogram import types
from loader import dp, db, bot

from data.config import ADMINS
from states.states import user_states

import uuid


def generate_unique_id():
    return str(uuid.uuid4())


@dp.inline_handler(state=user_states.set_key)
@dp.inline_handler(state=user_states.confirmation)
@dp.inline_handler(state=user_states.start)
@dp.inline_handler(state=user_states.set_val)
async def inline_handler(query: types.InlineQuery):
    telegram_id = query.from_user.id
    key = query.query

    if query.query:
        row = await db.select_row(telegram_id=telegram_id, key_set=key)
        if row:
            if row[3] == "text":
                results = [
                    types.InlineQueryResultArticle(
                        id=generate_unique_id(),
                        title=row[1],
                        input_message_content=types.InputTextMessageContent(row[2])
                    ),
                ]
                await query.answer(results, cache_time=0)
            elif row[3] == "audio":
                results = [
                    types.InlineQueryResultAudio(
                        id=generate_unique_id(),
                        title=row[1],
                        audio_url=row[2]
                    ),
                ]
                await query.answer(results, cache_time=0)
            elif row[3] == "document":
                results = [
                    types.InlineQueryResultDocument(
                        id=generate_unique_id(),
                        title=row[1],  # Set the title of the document
                        document_url=row[2],  # Set the URL of the document file
                        mime_type='application/pdf'
                    ),
                ]
                await query.answer(results, cache_time=0)
            elif row[3] == "animation":
                results = [
                    types.InlineQueryResultGif(
                        id=generate_unique_id(),
                        title=row[1],  # Set the title of the animation
                        gif_url=row[2],
                        thumb_url=row[2]

                    ),
                ]
                await query.answer(results, cache_time=0)
            elif row[3] == "voice":
                results = [
                    types.InlineQueryResultVoice(
                        id=generate_unique_id(),
                        title=row[1],  # Set the title of the voice message
                        voice_url=row[2]
                    ),
                ]
                await query.answer(results, cache_time=0)
            elif row[3] == "photo":
                results = [
                    types.InlineQueryResultPhoto(
                        id=generate_unique_id(),
                        title=row[1],  # Set the title of the photo
                        photo_url=row[2],  # Set the URL of the photo file
                        thumb_url=row[2]
                    ),
                ]
                await query.answer(results, cache_time=0)
            elif row[3] == "location":
                lat_long = row[2]
                lat_lng = lat_long.split("&")
                results = [
                    types.InlineQueryResultLocation(
                        id=generate_unique_id(),
                        title=row[1],  # Set the title of the location
                        latitude=float(lat_lng[0]),  # Set the latitude of the location
                        longitude=float(lat_lng[1])
                    ),
                ]
                await query.answer(results, cache_time=0)
            elif row[3] == "sticker":
                results = [
                    types.InlineQueryResultCachedSticker(
                        id=generate_unique_id(),
                        sticker_file_id=row[2]
                    ),
                ]
                await query.answer(results, cache_time=0)

    else:
        rows = await db.select_rows(telegram_id=telegram_id)
        print(rows)
        if rows:
            results = []
            for row in rows:
                if row[3] == "text":
                    results.append(types.InlineQueryResultArticle(
                        id=generate_unique_id(),
                        title=row[1],
                        input_message_content=types.InputTextMessageContent(row[2])
                    ),)
                elif row[3] == "audio":
                    results.append(types.InlineQueryResultAudio(
                        id=generate_unique_id(),
                        title=row[1],
                        audio_url=row[2]
                    ),)
                elif row[3] == "document":
                    results.append(types.InlineQueryResultDocument(
                        id=generate_unique_id(),
                        title=row[1],  # Set the title of the document
                        document_url=row[2],  # Set the URL of the document file
                        mime_type='application/pdf'
                    ),)
                elif row[3] == "animation":
                    results.append(types.InlineQueryResultGif(
                        id=generate_unique_id(),
                        title=row[1],  # Set the title of the animation
                        gif_url=row[2],
                        thumb_url=row[2]

                    ),)
                elif row[3] == "voice":
                    results.append(types.InlineQueryResultVoice(
                        id=generate_unique_id(),
                        title=row[1],  # Set the title of the voice message
                        voice_url=row[2]
                    ),)
                elif row[3] == "photo":
                    results.append(types.InlineQueryResultPhoto(
                        id=generate_unique_id(),
                        title=row[1],  # Set the title of the photo
                        photo_url=row[2],  # Set the URL of the photo file
                        thumb_url=row[2]
                    ),)
                elif row[3] == "location":
                    lat_long = row[2]
                    lat_lng = lat_long.split("&")
                    results.append(types.InlineQueryResultLocation(
                        id=generate_unique_id(),
                        title=row[1],  # Set the title of the location
                        latitude=float(lat_lng[0]),  # Set the latitude of the location
                        longitude=float(lat_lng[1])
                    ),)
                elif row[3] == "sticker":
                    results.append(types.InlineQueryResultCachedSticker(
                        id=generate_unique_id(),
                        sticker_file_id=row[2]
                    ),)
            print(results)
            await query.answer(results, cache_time=0)