from flask_wtf.file import FileField
from flask_wtf import FlaskForm

class ImageForm(FlaskForm):
    file = FileField('Image')