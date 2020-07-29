from myapp import application, login_manager, database, csrf
from myapp.blueprints import example
from flask import render_template, redirect, url_for, abort, request, session, escape, g, flash
from myapp.models import User
from flask_login import login_required, logout_user, current_user, login_user
from flask_bcrypt import generate_password_hash
from myapp.forms import LoginForm

application.register_blueprint(example.api)


@application.before_first_request
def before_first_request():
    database.create_all()
    if User.query.get(1):
        pass
    else:
        admin = User('admin', 'admin@example.local', 'Admin123', True)
        database.session.add(admin)
        database.session.commit()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get_or_404(int(user_id))


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'


@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@application.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@application.route('/')
def home():
    return render_template('index.html')


@application.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            return redirect(url_for('home'))
        else:
            return render_template('login.html', form=form)
    else:
        return render_template('login.html', form=form)


@application.route('/logout')
def logout():
    logout_user()
    return 'Logged out'


# @application.route('/register')
# def register():
#     return render_template('register.html')
#
#
# @application.route('/tables')
# def tables():
#     return render_template('tables.html')


application.register_error_handler(404, page_not_found)
application.register_error_handler(500, internal_server_error)
