from telebot.types import ReplyKeyboardMarkup
from telebot import types


def return_back_markup() -> ReplyKeyboardMarkup:

    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    return_btn = types.KeyboardButton('Начать заново▶️')
    markup.add(return_btn)

    return markup