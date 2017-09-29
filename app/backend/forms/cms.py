from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class SettingsForm(FlaskForm):
    site_title = StringField('Site title', [DataRequired()])
    submit = SubmitField('Save')
