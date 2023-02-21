import os

from flask import Flask, render_template, session, request

app = Flask(__name__)
app.secret_key = os.getenv('SECRET')


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

    return render_template('index.html', stage=stage, assignment=assignment)


if __name__ == '__main__':
    app.run()
