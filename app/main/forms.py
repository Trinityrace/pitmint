from flask_wtf import FlaskForm
from wtforms import StringField ,PasswordField, SubmitField, BooleanField,TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo,Required


class PitchForm(FlaskForm):
    category = TextAreaField('CATEGORY',validators = [Required()])
    content = TextAreaField('CREATE PITCH',validators = [Required()])
    author = TextAreaField('AUTHOR',validators=[Required()])
    submit = SubmitField('submit')

class UpdateProfile(FlaskForm):
  bio = TextAreaField('Tell us about yourself.',validators = [Required()])
  submit = SubmitField('Submit')