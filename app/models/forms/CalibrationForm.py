from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextField, FieldList, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

from app.scripts.Micromatter import serials4flask

# TODO: read micromatter id and insert in this array
micromatter_ids = serials4flask()

class CalibrationForm(FlaskForm):
    
    description = TextField('description', validators=[DataRequired()])

class CalibrationFormFiles(FlaskForm):
    
    csv_file = FileField(validators=[FileRequired(),FileAllowed(['csv'], 'csv only!')])
    txt_file = FileField(validators=[FileRequired(),FileAllowed(['txt'], 'txt only!')])
    micromatter_id = SelectField('Produce',validators=[DataRequired()], choices=micromatter_ids)
