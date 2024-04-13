import logging
import utils
from logger import setUpLogger
from config import MustLoad
import telebot
from telebot import types
import rs
import sqlite as st

# TODO: VERIFY IF ALL FIELDS ARE FILLED IN
config = MustLoad()

setUpLogger(config["log-level"])
logger = logging.getLogger(__name__)

logger.info("[bold yellow]== * Starting Bot * ==[/]", extra={"markup": True})
logger.info("[bold yellow]Logging level: {}[/]".format(config["log-level"]), extra={"markup": True})

r = rs.Storage(config["redis"]["host"], config["redis"]["port"])
r.checkConnection()

storage = st.Storage(config["sqlite"]["path"])

bot = telebot.TeleBot(config["bot"]["token"], skip_pending=True)


# handlers
@bot.message_handler(commands=['start'])
def send_welcome(message):
    response = storage.is_user_exists(message.from_user.id)
    if not response:
        storage.add_user(message.from_user.id)
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        start_btn = types.KeyboardButton('Начать▶️')
        markup.add(start_btn)
        try:
            bot.send_message(message.chat.id, "ПРИВЕТСТВЕННОЕ СООБЩЕНИЕ", reply_markup=markup)
        except Exception as e:
            logger.error(e)


@bot.message_handler(content_types=['text'])
def bot_handler(message):
    logger.debug("Message from {}: {}".format(message.from_user.id, message.text))

    response = storage.is_user_exists(message.from_user.id)

    logger.debug("Response to {}: {}".format(message.from_user.id, message.text))

    if not response:
        send_welcome(message)
        return

    match message.text:

        case "Начать▶️":
            logger.debug("Request: Get stage: {}: {}".format(message.from_user.id, message.text))
            stage = storage.get_user_stage(message.from_user.id)
            logger.debug("Response to {}: {}".format(message.from_user.id, stage))

            if stage == 0:
                text = """Введите ФИО 👤\nНапример: Иванов Иван Иванович"""

                bot.send_message(message.from_user.id, text, reply_markup=utils.return_back_markup())
            else:
                text = """У вас есть незаконченная анкета❌"""
                bot.send_message(message.from_user.id, text)

        case "Начать заново▶️":
            logger.debug("Request from {}: {}".format(message.from_user.id, message.text))
            response = storage.set_user_stage(message.from_user.id, 0)
            logger.debug("Response to {}: {}".format(message.from_user.id, response))

            storage.set_user_stage(message.from_user.id, 0)

            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            start_btn = types.KeyboardButton('Начать▶️')
            markup.add(start_btn)

            bot.send_message(message.from_user.id, "НАЧАТЬ", reply_markup=markup)

        case _:
            logger.debug("Request: Get stage: {}: {}".format(message.from_user.id, message.text))
            stage = storage.get_user_stage(message.from_user.id)
            logger.debug("Response to {}: {}".format(message.from_user.id, stage))

            match stage:

                case 0:

                    # ФИО
                    pass

                case 1:

                    # Дата рождения
                    pass

                case 2:

                    # Место рождения
                    pass

                case 3:

                    # Дата смерти
                    pass

                case 5:

                    # Черты характера
                    pass

                case 7:
                    # Увлечения
                    pass

                case 8:
                    # Род деятельности
                    pass

                case 9:
                    # Награды или заслуги или другие достижения
                    pass


if __name__ == "__main__":
    logger.info("[bold yellow]== * Running Bot * ==[/]", extra={"markup": True})
    bot.polling(none_stop=True)
