from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import IntegerField
from wtforms.validators import DataRequired


class TextFileForm(FlaskForm):
    file = FileField(label='File', validators=[
        FileRequired(message='You must include a text file.'),
        FileAllowed(['txt'], message='You may only upload .txt files.')
    ])
    sentences = IntegerField(label='Sentences', default=1, validators=[
        DataRequired(message='You must specify at least 1 sentence.'),
        lambda form, field: field.data > 0
    ])
    number = IntegerField(label='Number', default=1, validators=[
        DataRequired(),
        lambda form, field: field.data > 0
    ])
