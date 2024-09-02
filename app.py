# app.py ' OR '1'='1

from flask import Flask, render_template, request, redirect, url_for
from config import validate_login

app = Flask(__name__)

@app.route('/')
def index():
    error = request.args.get('error')
    return render_template('login.html', error=error)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    mode = request.form['mode']
    if validate_login(username, password, mode):
        return redirect(url_for('dashboard', username=username, mode=mode))
    else:
        return redirect(url_for('index', error='true'))

@app.route('/dashboard/<username>')
def dashboard(username):
    mode = request.args.get('mode')
    return render_template('dashboard.html', username=username, mode=mode)

@app.route('/xss', methods=['GET', 'POST'])
def xss():
    comment = ''
    if request.method == 'POST':
        comment = request.form['comment']
    return render_template('xss.html', comment=comment)

if __name__ == '__main__':
    app.run(debug=True)
