from flask import Flask, g
from flask_login import LoginManager, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_admin import Admin, AdminIndexView

SECRET_KEY = 'mysupersecretkey'

application = Flask(__name__)
application.secret_key = SECRET_KEY
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
application.config['SQLALCHEMY_BINDS'] = {}
application.config['WTF_CSRF_ENABLED'] = True
application.config['WTF_CSRF_SECRET_KEY'] = SECRET_KEY
application.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

login_manager = LoginManager()
login_manager.init_app(application)
login_manager.login_view = 'login'
login_manager.session_protection = 'strong'

database = SQLAlchemy(application)

csrf = CSRFProtect(application)


# Create customized index view class
class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        if current_user.is_authenticated:
            return current_user.is_admin
        return False


admin = Admin(application, name='My Flask App', template_mode='bootstrap4', index_view=MyAdminIndexView())


@application.before_request
def before_request():
    g.user = current_user


import services.web_application.web_app.myapp.views
