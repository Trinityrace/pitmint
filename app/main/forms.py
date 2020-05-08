from flask_wtf import FlaskForm
from wtforms import StringField ,PasswordField, SubmitField, BooleanField,TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo,Required


class PitchForm(FlaskForm):
    category = TextAreaField('Category?')
    content = TextAreaField('CREATE PITCH')
    submit = SubmitField('submit')

class UpdateProfile(FlaskForm):
  bio = TextAreaField('Tell us about yourself.',validators = [Required()])
  submit = SubmitField('Submit')