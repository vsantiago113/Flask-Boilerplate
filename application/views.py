from application import app
from application.blueprints import example
from flask import render_template, redirect, url_for

app.register_blueprint(example.api)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/logout')
def logout():
    return redirect(url_for('login'))


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/forgot-password')
def forgot_password():
    return render_template('forgot-password.html')


@app.route('/blank')
def blank_page():
    return render_template('blank.html')


@app.route('/tables')
def tables():
    return render_template('tables.html')


app.register_error_handler(404, page_not_found)
app.register_error_handler(500, internal_server_error)
