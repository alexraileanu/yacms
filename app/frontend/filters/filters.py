from app.frontend import frontend
from arrow import get
from app.backend.models.cms import CMS


@frontend.app_template_filter('format_date')
def format_date(string):
    return get(string).format(CMS.get('site_date_format'))


@frontend.app_template_filter('format_time')
def format_time(string):
    return get(string).format(CMS.get('site_time_format'))


@frontend.app_template_filter('humanize')
def date(string):
    return get(string).replace(tzinfo=CMS.get('site_timezone')).humanize()
