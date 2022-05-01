import time

import requests.packages
from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import *
import requests
import random
from datetime import datetime

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'abc'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///items.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class SubmitYourEmail(FlaskForm):
    email = StringField('')


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(300))
    answer = db.Column(db.String(100))
    correct_answer = db.Column(db.String(100))


db.create_all()


@app.route('/')
def home():
    return render_template('index.html')


correct = 0
question_id = 0


@app.route('/maths', methods=['GET', 'POST'])
def maths():
    global correct
    global question_id
    if request.method == 'GET':
        if question_id <= 9:
            question_id += 1
            data = Data.query.get(question_id)
            answers = data.answer.split(',')
            return render_template('math.html', data=data, answers=answers, id=question_id, correct=correct)
        else:
            correct = 0
            question_id = 1
            data = Data.query.get(question_id)
            answers = data.answer.split(',')
            time.sleep(10)
            return render_template('math.html', data=data, answers=answers, id=question_id, correct=correct)
    if request.method == 'POST':
        data = Data.query.get(question_id)
        if request.form['options'] == data.correct_answer:
            correct += 1
            return redirect(url_for('maths', id=question_id, correct=correct))
        return redirect(url_for('maths', id=question_id, correct=correct))


@app.route('/bla', methods=['GET', 'POST'])
def bla():
    global question_id
    global correct
    point = correct
    question_no = question_id
    correct = 0
    question_id = 0
    if request.method == 'POST':
        print('hello')
        print(request.form['options'])
        if request.form['options'] == '1':
            point += 1
            return render_template('bla.html', point=point, question_no=question_no)
    return render_template('bla.html', point=point, question_no=question_no)


@app.route('/books')
def books():
    data = requests.get(url="https://api.itbook.store/1.0/new").json()
    free = [i for i in data['books'] if float(i['price'][1::]) < 1]
    print(free)
    return render_template('books.html', data=free)


@app.route('/hangman')
def hangman():
    return render_template('hangman.html')


if __name__ == '__main__':
    app.run(debug=True)
