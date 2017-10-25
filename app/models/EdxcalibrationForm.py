from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired

class EdxcalibrationForm(FlaskForm):
    #d = StringField('username', validators=[DataRequired()])
    #password = PasswordField('password',validators=[DataRequired()])
    photo = FileField(validators=[FileRequired()])
