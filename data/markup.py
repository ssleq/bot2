from aiogram import types
from database import Database


class Markup_konkurs:
    def get_markup():
            for i in Database.database_konkurs():
                verification = types.InlineKeyboardMarkup(
                    inline_keyboard=[
                        [types.InlineKeyboardButton(text=i[0], callback_data=i[0])]
                    ]
                )


