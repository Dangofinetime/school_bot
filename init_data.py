from models import Subject, Lesson, Class
from db import db_session
import datetime

subject = db_session.query(Subject).first()

if subject is None:
	titles = ['Физика', 'Информатика', 'Алгебра', 'Английский язык', 'Русский язык', 'Физ-ра', 'Геометрия', 'Химия']
	for title in titles:
		db_session.add(Subject(title=title))
	db_session.commit()


classe = db_session.query(Class).first()

if classe is None:
	titles = ['8а', '8б', '8в', '8г']
	for title in titles:
		db_session.add(Class(title=title))
	db_session.commit()


lesson = db_session.query(Lesson).first()

if lesson is None:
	lesson1 = Lesson(title='Первый урок', time=datetime.time(8, 30), day_of_week='Понедельник', sub_id=1, cl_id=1)
	lesson2 = Lesson(title='Второй урок', time=datetime.time(9, 30), day_of_week='Вторник', sub_id=4, cl_id=2)
	lesson3 = Lesson(title='Третий урок', time=datetime.time(10, 30), day_of_week='Среда', sub_id=3, cl_id=3)
	lesson4 = Lesson(title='Четвёртый урок', time=datetime.time(11, 30), day_of_week='Пятница', sub_id=8, cl_id=4)
	lesson5 = Lesson(title='Пятый урок', time=datetime.time(12, 30), day_of_week='Среда', sub_id=5, cl_id=2)
	lesson6 = Lesson(title='Шестой урок', time=datetime.time(13, 30), day_of_week='вторник', sub_id=1, cl_id=4)
	lesson7 = Lesson(title='Первый урок', time=datetime.time(8, 30), day_of_week='Понедельник', sub_id=7, cl_id=3)
	lesson8 = Lesson(title='Третий урок', time=datetime.time(10, 30), day_of_week='Четверг', sub_id=6, cl_id=2)
	db_session.add_all([lesson3, lesson2, lesson1, lesson4, lesson5, lesson6, lesson7, lesson8])
	db_session.commit()
















