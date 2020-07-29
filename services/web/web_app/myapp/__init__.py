from flask import Flask, g
from flask_login import LoginManager, current_user
import uuid
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

global_secret_key = uuid.uuid4().hex
wtf_csrf_secret_key = uuid.uuid4().hex

application = Flask(__name__)
application.secret_key = global_secret_key
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
application.config['SQLALCHEMY_BINDS'] = {}
application.config['WTF_CSRF_ENABLED'] = True
application.config['WTF_CSRF_SECRET_KEY'] = wtf_csrf_secret_key

login_manager = LoginManager()
login_manager.init_app(application)
login_manager.login_view = 'login'
login_manager.session_protection = 'strong'

database = SQLAlchemy(application)

csrf = CSRFProtect(application)


@application.before_request
def before_request():
    g.user = current_user


import myapp.views
