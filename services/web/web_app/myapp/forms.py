from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Optional, InputRequired


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), DataRequired(), Length(min=6, max=250), Email(),
                                             Optional(strip_whitespace=True)])
    password = PasswordField('Password', validators=[InputRequired(), DataRequired(), Length(min=8, max=32),
                                                     Optional(strip_whitespace=True)])
    remember_me = BooleanField('Remember me', default=False)
    submit = SubmitField('Login')
