from flask_login import UserMixin
from flask_bcrypt import generate_password_hash
from datetime import datetime
from myapp import database


class User(UserMixin, database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(32), unique=True, nullable=False)
    password = database.Column(database.Binary(128), nullable=False)
    email = database.Column(database.String(250), unique=True, nullable=False)
    is_admin = database.Column(database.Boolean, default=False)
    is_active = database.Column(database.Boolean, default=True)
    joined_on = database.Column(database.DateTime, default=datetime.now)

    def __init__(self, username, email, password, is_admin=False):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.is_admin = is_admin

    def __repr__(self):
        return '<User %r>' % self.username
