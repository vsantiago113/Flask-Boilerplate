from myapp import application
from myapp.blueprints import example
from flask import render_template, redirect, url_for

application.register_blueprint(example.api)


@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@application.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/login')
def login():
    return render_template('login.html')


@application.route('/logout')
def logout():
    return redirect(url_for('login'))


@application.route('/register')
def register():
    return render_template('register.html')


@application.route('/forgot-password')
def forgot_password():
    return render_template('forgot-password.html')


@application.route('/blank')
def blank_page():
    return render_template('blank.html')


@application.route('/tables')
def tables():
    return render_template('tables.html')


application.register_error_handler(404, page_not_found)
application.register_error_handler(500, internal_server_error)
