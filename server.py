from flask import Flask, render_template, request, redirect
from flask.ext.login import LoginManager
from flask_login import current_user, login_user
from db import db_session
from models import User, Lesson
import uuid



my_flask_app = Flask(__name__)

my_flask_app.secret_key = str(uuid.uuid1).replace('-', '')



login_manager = LoginManager()
login_manager.init_app(my_flask_app)


@login_manager.user_loader
def load_user(user_id):
    return db_session.query(User).get(user_id)


@my_flask_app.route('/')
def index():

	if not current_user.is_authenticated:
		return redirect('/login/')

	all_lessons = db_session.query(Lesson).all()

	return render_template('index.html', title='', lessons=all_lessons)



@my_flask_app.route('/login/', methods=['POST', 'GET'])
def login():
	if request.method == "POST":
		print(request.form.get('user_name'))
		print(request.form.get('password'))
		user = db_session.query(User).filter(User.username == request.form.get('user_name'), 
											 User.password == request.form.get('password')).first()
		if user is None:
			return render_template('login.html', error= "Ошибка авторизации")
		else:
			login_user(user)
			return redirect('/')

	return render_template('login.html')



if __name__ == "__main__":
	my_flask_app.run(debug=True)
