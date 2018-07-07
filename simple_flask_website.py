# install flask: pip install flask

'''
Deploying webapp on heroku:
1. Create account on heroku.com
2. install heroku toolbelt on pc
3. create venv
4. open cmd:
	heroku login
	create new app: heroku create my1flaskapp
	see all apps: heroku apps
	install gunicorn: pip install gunicorn
	create requirements.txt: pip freeze > requirements.txt
	create Procfile:
		web: gunicorn simple_flask_app.py:app

'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template("home.html")

@app.route('/about/')
def about():
	return render_template("about.html")

if __name__ == "__main__":
	app.run(debug=True)