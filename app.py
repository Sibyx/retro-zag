import os

from flask import Flask, render_template, session, request

app = Flask(__name__)
app.secret_key = os.getenv('SECRET')


@app.route('/', methods=['GET', 'POST'])
def assignment1():
    stage = session.get('stage', 'intro')
    if request.method == 'POST':
        if stage == 'intro':
            session['name'] = request.form['name'].strip()
            stage = 'assignment'
        elif stage in ['assignment', 'fail']:
            if request.form['answer'] == '42':
                stage = 'success'
            else:
                stage = 'fail'
    else:
        if stage in ['fail', 'success']:
            stage = 'assignment'

    session['stage'] = stage

    return render_template('index.html', stage=stage)


if __name__ == '__main__':
    app.run()
