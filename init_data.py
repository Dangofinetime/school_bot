from models import Subject, Lesson, Class, User
from db import db_session
import datetime, getpass

subject = db_session.query(Subject).first()

if subject is None:
	titles = ['Физика', 'Информатика', 'Алгебра', 'Английский язык', 'Русский язык', 'Физ-ра', 'Геометрия', 'Химия', 'Немецкий язык', 'История', 'Обществознание', 'География', 'Литература', 'Биология']
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
	lesson9 = Lesson(title='Второй урок', time=datetime.time(9, 30), day_of_week='Понедельник', sub_id=10, cl_id=2)
	lesson10 = Lesson(title='Седьмой урок', time=datetime.time(14, 30), day_of_week='Среда', sub_id=11, cl_id=4)
	lesson11 = Lesson(title='Шестой урок', time=datetime.time(13, 30), day_of_week='Пятница', sub_id=1, cl_id=3)
	lesson12 = Lesson(title='Четвёртый урок', time=datetime.time(11, 30), day_of_week='Вторник', sub_id=8, cl_id=1)
	db_session.add_all([lesson3, lesson2, lesson1, lesson4, lesson5, lesson6, lesson7, lesson8, lesson9, lesson10, lesson11, lesson12])
	db_session.commit()


super_user_name = input("Введите имя пользователя\n")
super_user_pass = getpass.getpass("Введите пароль\n")
super_user_repeat_pass = getpass.getpass("Повторите пароль\n")
if super_user_pass == super_user_repeat_pass:
    Super_user = User(username=super_user_name, password=super_user_pass)
    db_session.add(Super_user)
    db_session.commit()
else:
    print("Пароли не совпадают!")

















