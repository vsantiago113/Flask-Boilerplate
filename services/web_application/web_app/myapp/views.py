from services.web_application.web_app.myapp import application, login_manager, database, current_user, admin
from services.web_application.web_app.myapp.blueprints import example
from flask import render_template, redirect, url_for, request, escape, g, flash, abort
from services.web_application.web_app.myapp.models import User, Role
from flask_login import login_required, logout_user, login_user
from flask_bcrypt import check_password_hash, generate_password_hash
from services.web_application.web_app.myapp.forms import LoginForm
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink
from datetime import datetime
from wtforms import PasswordField

application.register_blueprint(example.api)


@application.before_first_request
def before_first_request():
    database.create_all()
    if not User.query.filter_by(username='admin').first():
        admin_user = User(username='admin', email='admin@example.local', password='Admin123', is_admin=True)
        database.session.add(admin_user)
        database.session.commit()


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


@login_manager.unauthorized_handler
def unauthorized_handler():
    abort(401)


@application.errorhandler(401)
def unauthorized(e: object):
    """

    :type e: object
    """
    return render_template('401.html', http_error=e), 401


@application.errorhandler(403)
def forbidden(e: object):
    """

    :type e: object
    """
    return render_template('403.html', http_error=e), 403


@application.errorhandler(404)
def page_not_found(e: object):
    """

    :type e: object
    """
    return render_template('404.html', http_error=e), 404


@application.errorhandler(500)
def internal_server_error(e: object):
    """

    :type e: object
    """
    return render_template('500.html', http_error=e), 500


class UserView(ModelView):
    page_size = 25
    column_exclude_list = ['password']
    column_searchable_list = ['username', 'email']
    column_filters = ['is_admin']

    # <--
    # Issue found: When the user was updated the password field was resend and a new hash was created from the
    # current password hash.
    # Solution: I removed the password field and added a new one named 'password2' to be able to change the password
    # if the form is filled. So now if someone enter a new password on the field 'password2' then we create a
    # password hash from the new password and this will be updated on the database as the new user password.
    form_excluded_columns = ['joined_on', 'roles', 'password']
    form_extra_fields = {
        'password2': PasswordField('New password')
    }
    # -->

    def is_accessible(self):
        if current_user.is_authenticated:
            return current_user.is_admin
        return False

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('login', next=request.url))

    def on_model_change(self, form, model, is_created):
        if is_created:
            model.joined_on = datetime.now()

        # Here
        if form.password2.data is not None:
            model.password = generate_password_hash(form.password2.data)


class RoleView(ModelView):
    page_size = 25

    def is_accessible(self):
        if current_user.is_authenticated:
            return current_user.is_admin
        return False

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('login', next=request.url))


@application.route('/')
def home():
    return render_template('index.html')


@application.route('/login', methods=['GET', 'POST'])
def login():
    if g.user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            email = escape(form.email.data)
            password = escape(form.password.data)
            user = User.query.filter_by(email=email).first()
            if user:
                if check_password_hash(user.password, password):
                    login_user(user, remember=form.remember_me.data)
                    return redirect(url_for('home'))
                else:
                    flash('Invalid username/password!', 'danger')
                    return render_template('login.html', form=form)
            else:
                flash('Account does not exists, please register an account.', 'warning')
                return render_template('login.html', form=form)
        else:
            return render_template('login.html', form=form)
    else:
        return render_template('login.html', form=form)


@application.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


application.register_error_handler(404, page_not_found)
application.register_error_handler(401, unauthorized)
application.register_error_handler(403, forbidden)
application.register_error_handler(500, internal_server_error)
admin.add_view(UserView(User, database.session))
admin.add_view(RoleView(Role, database.session))
admin.add_link(MenuLink(name='Logout', url='/logout', category=''))
