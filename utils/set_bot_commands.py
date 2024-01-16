from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand("add", "Yangi ma'lumot qo'shish"),
            types.BotCommand("delete", "Ma'lumotni o'chirish")
        ]
    )
