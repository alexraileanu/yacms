from flask import Blueprint

frontend = Blueprint('frontend', __name__, template_folder='templates')

from app.frontend.routes import index