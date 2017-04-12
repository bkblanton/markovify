from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length


class TextFileForm(FlaskForm):
    # file = FileField(label='File', validators=[
    #     FileRequired(message='You must include a text file.'),
    #     FileAllowed(['txt'], message='You may only upload .txt files.')
    # ])
    text = TextAreaField(label='Text', validators=[
        DataRequired(message='You must include some text to analyze.'),
        Length(min=1, max=5000000, message='Your text size must be less than 5 megabytes.')
    ])
    sentences = IntegerField(label='Sentences', default=1, validators=[
        DataRequired(message='You must specify at least 1 sentence per output.'),
        lambda form, field: field.data > 0
    ])
    number = IntegerField(label='How many?', default=1, validators=[
        DataRequired(message='You must specify at least 1 output to generate.'),
        lambda form, field: field.data > 0
    ])
