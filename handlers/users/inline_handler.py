from aiogram import types
from loader import dp, db, bot
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent



from data.config import ADMINS


@dp.inline_handler()
async def inline_handler(query: types.InlineQuery):
    telegram_id = query.from_user.id
    key = query.query
    # print(f"key: {key}")
    row = await db.select_row(telegram_id=telegram_id, key_set=key)
    # print(f"row: {row}")
    # print(f"queryID {query.id}")
    if row and row[0] == query.from_user.id:
        print("yes")
        print(f"telegram_id: {query.from_user.id} db_id: {row[0]}")
        results = [
            InlineQueryResultArticle(
                id='1',
                title=telegram_id,
                input_message_content=InputTextMessageContent(f"Your file_id: {row[2]}")
            ),
        ]

        await query.answer(results)
    else:
        print("NO")