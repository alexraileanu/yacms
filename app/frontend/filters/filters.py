from app.frontend import frontend
from arrow import get


@frontend.app_template_filter('date')
def date(string, format):
    return get(string).format(format)


@frontend.app_template_filter('humanize')
def date(string):
    return get(string).replace(tzinfo='local').humanize()
