from importlib.resources import contents
from wtforms import StringField, TextAreaField, SubmitField,SelectField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm

class Pitches(FlaskForm):
    contents = TextAreaField('add a pitch')
    submit = SubmitField()

class Comments(FlaskForm):
    comment = TextAreaField('leave a comment')
    submit = SubmitField()

class Category(FlaskForm):
    select = StringField('Enter Category: ', validators=[InputRequired()])
    submit =SubmitField()

class Updates(FlaskForm):
    bio = TextAreaField('bio', validators=[InputRequired()])
    submiit = SubmitField()