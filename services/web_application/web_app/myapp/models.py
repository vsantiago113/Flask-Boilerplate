from flask_login import UserMixin
from flask_bcrypt import generate_password_hash
from datetime import datetime
from services.web_application.web_app.myapp import database


class User(UserMixin, database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(32), unique=True, nullable=False)
    password = database.Column(database.Binary(128), nullable=False)
    email = database.Column(database.String(250), unique=True, nullable=False)
    is_admin = database.Column(database.Boolean, default=False)
    joined_on = database.Column(database.DateTime, default=datetime.now)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.username

    def __init__(self, username, email, password, is_admin=False):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.is_admin = is_admin

    def __repr__(self):
        return '<User %r>' % self.username
