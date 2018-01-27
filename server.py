from flask import Flask, render_template, request, redirect
from flask.ext.login import LoginManager
from flask_login import current_user


my_flask_app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(my_flask_app)

@my_flask_app.route('/')
def index():

	if not current_user.is_authenticated:
		return redirect('/login/')

	return render_template('index.html', title='')



@my_flask_app.route('/login/', methods=['POST', 'GET'])
def login():
	return render_template('login.html', email=request.form.get('email'), password=request.form.get('password'))

if __name__ == "__main__":
	my_flask_app.run(debug=True)