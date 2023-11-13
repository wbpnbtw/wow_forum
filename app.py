from flask import Flask, render_template, request, redirect

app = Flask(__name__)
base_login = []
base_pass = []


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
        return redirect('/main')
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if username in base_login and password in base_pass:
            redirect('/main')
    render_template('login.html')


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
