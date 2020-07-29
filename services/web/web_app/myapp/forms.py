from flask_wtf import FlaskForm
from flask import flash, g, escape
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email, Regexp
from myapp.models import User
from flask_bcrypt import check_password_hash
from flask_login import login_user


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Length(min=6, max=250), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=32)])
    remember_me = BooleanField("Remember me", default=False)
    submit = SubmitField("Login")

    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False

        user = User.query.filter_by(
            email=self.email.data).first()
        if user is None:
            flash("Account does not exists, please register an account.", "warning")
            return False

        if not check_password_hash(user.password, self.password.data):
            flash("Invalid username/password!", "danger")
            return False

        if self.remember_me.data:
            login_user(user, remember=True)
        else:
            login_user(user)

        self.user = user
        return True
