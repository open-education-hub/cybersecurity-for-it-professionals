from flask import *

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        resp = make_response(redirect('/auth'))
        if username == 'admin' and password == 'P@ssw0rd':
            resp.set_cookie('user', username)
        else:
            resp.set_cookie('user', 'notadmin')

        return resp
    elif request.method == 'GET':
        user = request.cookies.get('user')

        if user == 'admin':
            return 'Congratz! You\'re an admin!'
        else:
            return 'You\'re not admin'
