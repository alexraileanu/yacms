from flask import Blueprint

frontend = Blueprint('frontend', __name__, template_folder='templates', static_folder='static/public',
                     static_url_path='')

from app.frontend.routes import index
from app.frontend.routes import article
from app.frontend.routes import comment
from app.frontend.filters import filters

from app.frontend.utils import processors
