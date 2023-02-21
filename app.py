from datetime import datetime
import os

from flask import Flask, render_template, session, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = os.getenv('SECRET')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    "POSTGRES_CONNECTION", "postgresql://postgres@localhost:5432/zag"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Record(db.Model):
    __tablename__ = 'records'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=True)
    stage = db.Column(db.String(), nullable=True)
    answer = db.Column(db.String(), nullable=True)
    assignment = db.Column(db.String(), nullable=True)
    created_at = db.Column(db.DateTime(), default=datetime.now, nullable=False)

    def __init__(self, name, stage, answer, assignment):
        self.name = name
        self.stage = stage
        self.answer = answer
        self.assignment = assignment


@app.route('/', methods=['GET', 'POST'])
def index():
    stage = session.get('stage', 'intro')
    assignment = session.get('assignment', '1')
    if request.method == 'POST':
        if stage == 'intro':
            session['name'] = request.form['name'].strip()
            stage = 'assignment'
        elif stage in ['assignment', 'fail']:
            if assignment == '1':
                if request.form['answer'] == '42':
                    stage = 'assignment'
                    assignment = '2'
                else:
                    stage = 'fail'
            elif assignment == '2':
                if request.form['answer'] == '42':
                    stage = 'success'
                    assignment = '1'
                else:
                    stage = 'fail'

    else:
        if stage in ['fail', 'success']:
            stage = 'assignment'

    session['stage'] = stage
    session['assignment'] = assignment

    record = Record(
        session.get('name'),
        session.get('stage'),
        request.form.get('answer'),
        session.get('assignment'),
    )
    db.session.add(record)
    db.session.commit()

    return render_template('index.html', stage=stage, assignment=assignment)


if __name__ == '__main__':
    app.run()
