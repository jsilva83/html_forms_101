from flask import Flask
from flask import render_template
from flask import request
import random as rand
import datetime as dt
import requests as req

app = Flask(__name__)


@app.route("/index.html")
@app.route("/")
def a_index():

    return render_template('index.html')


@app.route('/login', methods=['POST'])
def receive_login():

    username = request.form['username']
    password = request.form['password']

    return render_template('password.html', a_username=username, a_password=password)


if __name__ == '__main__':

    this_year = str(dt.date.today().year)
    app.run(debug=True)