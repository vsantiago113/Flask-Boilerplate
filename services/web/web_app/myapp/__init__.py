from flask import Flask, g
from flask_login import LoginManager, current_user
import uuid
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

application = Flask(__name__)
application.secret_key = uuid.uuid4().hex
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
application.config['SQLALCHEMY_BINDS'] = {}

login_manager = LoginManager()
login_manager.init_app(application)
login_manager.login_view = 'login'
login_manager.session_protection = 'strong'

database = SQLAlchemy(application)

csrf = CSRFProtect(application)
csrf.init_app(application)


@application.before_request
def before_request():
    g.user = current_user


import myapp.views
