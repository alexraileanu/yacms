from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
from pytz import common_timezones


class SettingsForm(FlaskForm):
    site_title = StringField('Site title', [DataRequired()])
    site_timezone = SelectField('Test', choices=[(k, k) for k in common_timezones])
    submit = SubmitField('Save')
