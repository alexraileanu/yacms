from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, RadioField
from wtforms.validators import DataRequired
from pytz import common_timezones

DATE_FORMATS = [
    ('Do of MMMM, YYYY', '22nd of September, 2017'),
    ('YYYY-MM-DD', '2017-09-22'),
    ('MM/DD/YYYY', '09/22/2017'),
    ('DD/MM/YYYY', '22/09/2017')
]

TIME_FORMATS = [
    ('hh:mm A', '01:33 PM'),
    ('HH:mm', '13:33')
]


class SettingsForm(FlaskForm):
    site_title = StringField('Site title', [DataRequired()])
    site_timezone = SelectField('Timezone', choices=[(k, k) for k in common_timezones])
    site_date_format = RadioField('Date format', choices=DATE_FORMATS)
    site_time_format = RadioField('Time format', choices=TIME_FORMATS)
    submit = SubmitField('Save')
