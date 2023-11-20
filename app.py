from flask import Flask, render_template, request, redirect
import random
app = Flask(__name__)
base_login = []
base_pass = []
alpha= ['1', '2','3', '4', '5', '6', '7', '8', '9', '0', '-', '=','[', 'p', 'o', 'i', 'u', 'y',
        't',' r', 'e', 'w', 'q', 'a', 's', 'd', 'f','g','h','j','k','l',';','z','x','c','v','b','n','m']


@app.route('/')
def page():
    return render_template("hello.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        base_login.append(username)
        base_pass.append(password)
        a=''
        for i in range(0, 12):
            a=a+random.choice(alpha)
        return render_template('register.html', variable=a)
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if username in base_login and password in base_pass:
            return redirect('/main')
    return render_template('login.html')


@app.route('/post', methods=['POST'])
def post():
    username = request.form['username']
    message = request.form['message']
    return redirect('/main')


@app.route('/main', methods=["post"])
def main():
    render_template('index.html')


@app.route('/topik', methods=['get', 'post'])
def view():
    render_template('topiks.html')


def create():
    render_template('create.html')


if __name__ == '__main__':
    app.run()
