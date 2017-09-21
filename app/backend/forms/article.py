from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class ArticleForm(FlaskForm):
    title = StringField('Title', [DataRequired()])
    content = TextAreaField('Content', [DataRequired()])
    submit = SubmitField('Submit')
