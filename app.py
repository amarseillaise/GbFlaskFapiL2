from flask import Flask, request
from flask import url_for, redirect, render_template, make_response

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('base.html')


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        response = make_response(render_template('welcome.html', name=request.form['name']))
        response.set_cookie('username', request.form['name'])
        response.set_cookie('email', request.form['email'])
        return response


@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        response = make_response(redirect(url_for('login')))
        response.set_cookie('username', '', expires=0)
        response.set_cookie('email', '', expires=0)
        return response


if __name__ == '__main__':
    app.run()
