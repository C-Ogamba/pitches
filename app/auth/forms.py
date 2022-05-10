from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from ..models import User

class LoginForm(FlaskForm):
    """
    Login form
    """
    email = StringField('Email',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')


class SignupForm(FlaskForm):
    """
    Signup form
    """
    email = StringField('Email',validators=[DataRequired()])
    username = StringField('username',validators=[DataRequired()])
    name = StringField('Name',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    about = StringField('About')

    def validate_email(self,data_field):
            if User.query.filter_by(email = data_field.data).first():
                raise ValidationError('Email already exists')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('Username is already taken')