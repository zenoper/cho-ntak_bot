from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

confirmation_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="tasdiqlash ✅", callback_data="confirm"),
            InlineKeyboardButton(text="tahrirlash ✏️", callback_data="edit")
        ],
    ]
)