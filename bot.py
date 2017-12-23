from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from models import Subject, Lesson, Class
from db import db_session


logging.basicConfig(format="%(name)s -%(levelname)s-%(message)s",
    level=logging.INFO,
    filename="bot.log"
    )

def lessons(bot, update):
    class_titles = db_session.query(Class.title).all()
    class_titles = [title[0] for title in class_titles]
    print(class_titles)
    class_name = update.message.text [9:]
    if class_name in class_titles:
        update.message.reply_text(class_name)
    else:
        update.message.reply_text("Такого класса нету!")


def main():
    updater = Updater("425488603:AAFtfqpA1CDbMlMcqNXnPDPJ5jZOC-rgWkA")
    dp =updater.dispatcher
    dp.add_handler(CommandHandler("lessons", lessons))
    updater.start_polling()
    updater.idle()
main()