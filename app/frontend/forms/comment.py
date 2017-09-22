from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, IntegerField
from wtforms.validators import DataRequired
from wtforms.widgets import HiddenInput


class CommentForm(FlaskForm):
    username = StringField('Username', [DataRequired()])
    content = TextAreaField('Content', [DataRequired()])
    article_id = IntegerField(widget=HiddenInput())