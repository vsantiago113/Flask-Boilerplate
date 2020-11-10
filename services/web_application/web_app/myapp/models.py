from flask_login import UserMixin, AnonymousUserMixin
from flask_bcrypt import generate_password_hash
from datetime import datetime
from services.web_application.web_app.myapp import database

'''
# How to add roles to a user?
# CODE:
role = Role.query.filter_by(name='MyRole').first()
user = User.query.filter_by(username='admin').first()
user.roles.append(role)
database.session.commit()
'''

roles_users = database.Table(
    'role_users',
    database.Column('user_id', database.Integer(), database.ForeignKey('user.id')),
    database.Column('role_id', database.Integer(), database.ForeignKey('role.id'))
)


class AnonymousUser(AnonymousUserMixin):
    """AnonymousUser definition"""

    def __init__(self):
        self.roles = list()

    @property
    def is_authenticated(self):
        return False

    @property
    def is_active(self):
        return False

    @property
    def is_anonymous(self):
        return True

    def get_id(self):
        return None

    @staticmethod
    def has_role(*args):
        return False


class User(UserMixin, database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(32), unique=True, nullable=False)
    password = database.Column(database.Binary(128), nullable=False)
    email = database.Column(database.String(250), unique=True, nullable=False)
    joined_on = database.Column(database.DateTime, default=datetime.now)
    is_admin = database.Column(database.Boolean, default=False)
    roles = database.relationship('Role', secondary=roles_users,
                                  backref=database.backref('users', lazy='dynamic'))

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

    def has_role(self, role):
        """Returns 'True' if the user identifies with the specified role.
        :param role: A role name or 'Role' instance"""
        if isinstance(role, str):
            return role.upper() in [user_role.name.upper() for user_role in self.roles]

    # Required for administrative interface
    def __unicode__(self):
        return self.username

    def __init__(self, username, email, password, is_admin=False):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.is_admin = is_admin

    def __repr__(self):
        return self.username


class Role(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(64), unique=True, nullable=False)
    description = database.Column(database.String(255), nullable=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return self.name
