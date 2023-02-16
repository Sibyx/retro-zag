from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/eb619777-d311-42fd-a2ae-95da7c362015')
def assignment1():
    # print(url_for('assignment1'))
    return render_template('assignment1.html')


if __name__ == '__main__':
    app.run()
