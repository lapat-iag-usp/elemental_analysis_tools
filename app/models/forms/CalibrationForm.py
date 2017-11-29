from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired

class CalibrationForm(FlaskForm):
    
    description = TextField('description', validators=[DataRequired()])
    #photo = FileField(validators=[FileRequired()])
