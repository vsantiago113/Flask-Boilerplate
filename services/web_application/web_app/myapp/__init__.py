from flask import Flask, g, request, redirect
from flask_login import LoginManager, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
import os

application = Flask(__name__)
application.secret_key = os.environ.get('SECRET_KEY')
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
application.config['SQLALCHEMY_BINDS'] = {}
application.config['WTF_CSRF_ENABLED'] = True
application.config['WTF_CSRF_SECRET_KEY'] = os.environ.get('WTF_CSRF_SECRET_KEY')

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
