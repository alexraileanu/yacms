from app.frontend import frontend
from app.backend.models.cms import CMS


@frontend.context_processor
def site_title():
    return dict(site_title=CMS.get('site_title'))
