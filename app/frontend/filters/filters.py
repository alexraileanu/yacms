from app.frontend import frontend
from arrow import get
from app.backend.models.cms import CMS


@frontend.app_template_filter('date')
def date(string, format):
    return get(string).format(format)


@frontend.app_template_filter('humanize')
def date(string):
    return get(string).replace(tzinfo=CMS.get('site_timezone')).humanize()
