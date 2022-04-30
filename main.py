from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import *
import requests
import random

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
        question_id += 1
        print(question_id)
        data = Data.query.get(question_id)
        answers = data.answer.split(',')
        return render_template('math.html', data=data, answers=answers, id=question_id, correct=correct*10)

    if request.method == 'POST':
        data = Data.query.get(question_id)
        print(request.form['options'])
        print(data.correct_answer)
        if request.form['options'] == data.correct_answer:
            correct += 1
            print(correct)
            return redirect(url_for('maths', id=question_id, correct=correct*10))
        return redirect(url_for('maths', id=question_id, correct=correct*10))



@app.route('/bla/<int:id>')
def bla(id):
    return render_template('bla.html', id=1)


if __name__ == '__main__':
    app.run(debug=True)
