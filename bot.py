from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from models import Subject, Lesson, Class
from db import db_session
from datetime import datetime
from collections import OrderedDict


logging.basicConfig(format="%(name)s -%(levelname)s-%(message)s",
    level=logging.INFO,
    filename="bot.log"
    )


def lessons(bot, update):
    class_titles = db_session.query(Class.title).all()
    class_titles = [title[0] for title in class_titles]
    class_name = update.message.text [9:]
    current_class = db_session.query(Class).filter(Class.title==class_name).first()
    if  current_class is None :
        update.message.reply_text("Такого класса нету!")
    else:
        lessons = db_session.query(Lesson).filter(Lesson.cl_id==current_class.id).order_by(Lesson.day_of_week, Lesson.time).all()
        subjects = db_session.query(Subject).all()
        subjects_dict = {}
        for subject in subjects:
            subjects_dict[subject.id] = subject.title
        lessons_by_day = OrderedDict()
        for lesson in lessons:
            if lesson.day_of_week not in lessons_by_day:
                lessons_by_day[lesson.day_of_week] = []
            lessons_by_day[lesson.day_of_week].append(lesson)
        for key in lessons_by_day.keys():
            table_text = '{}:\n\n'.format(key)
            for lesson in lessons_by_day[key]:
               table_text = table_text+'{} {} [{}]\n'.format(lesson.time.strftime("%H:%M"), lesson.title, subjects_dict[lesson.sub_id])
               update.message.reply_text(table_text)


def main():
    updater = Updater("425488603:AAFtfqpA1CDbMlMcqNXnPDPJ5jZOC-rgWkA")
    dp =updater.dispatcher
    dp.add_handler(CommandHandler("lessons", lessons))
    updater.start_polling()
    updater.idle()


if __name__ = '__main__':   
    main()