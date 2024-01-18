from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

confirmation_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="tasdiqlash ✅", callback_data="confirm"),
            InlineKeyboardButton(text="tahrirlash ✏️", callback_data="edit")
        ],
    ]
)

link = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↪", url="https://t.me/chontak_bot"),
        ],
    ]
)

link_add = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="↪", url="https://t.me/chontak_bot/add"),
        ],
    ]
)