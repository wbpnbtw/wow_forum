from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

login_pass_base = {'login': "", "pass": ""}


@app.route("/")
def hello_page():
    return render_template('hello_page.html')


@app.route('/user/<username>')
def user_profile(username):
    if username in login_pass_base:
        return render_template('login_error.html')
    else:
        return "Это профиль юзера (f'username')"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in login_pass_base['login']:
            if password in login_pass_base['pass']:
                return render_template("users.html")
            else:
                return login
        else:
            return login
    else:
        return render_template('login.html')


@app.route('/reg', methods=['Get'])
def register():
    username = request.form['']
    password = request.form['']
    login_pass_base['login'] = username
    login_pass_base['password'] = password


@app.route('/main', methods=['get', 'post'])
def main():
    render_template('main.html')


@app.route('/create', methods=['get', 'post'])
def create():
    render_template('create_topic.html')


@app.route('/support')
def support():
    render_template('support.html')


if __name__ == '__main__':
    app.run
