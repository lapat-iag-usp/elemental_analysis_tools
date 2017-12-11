from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextField, FieldList, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

micromatter_ids = [(1, '26728678'),(2, 'e73298e')]

class CalibrationForm(FlaskForm):
    
    description = TextField('description', validators=[DataRequired()])

class CalibrationFormFiles(FlaskForm):
    
    csv = FileField(validators=[FileRequired(),FileAllowed(['csv'], 'csv only!')])
    txt = FileField(validators=[FileRequired(),FileAllowed(['txt'], 'txt only!')])
    micromatter_id = SelectField('Produce',validators=[DataRequired()], choices=micromatter_ids)
