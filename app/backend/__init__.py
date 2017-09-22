from flask import Blueprint
from flask_user import UserManager, SQLAlchemyAdapter

from app import db
from app import app

backend = Blueprint('backend', __name__, template_folder='templates', url_prefix='/admin',
                    static_folder='static/public', static_url_path='')

from app.backend.models import user as user_model
from app.backend.models import article
from app.backend.models import comment

db_adapter = SQLAlchemyAdapter(db, user_model.User)  # Register the User model
user_manager = UserManager(db_adapter, app)  # Initialize Flask-User

from app.backend.routes import user as user_routes
from app.backend.routes import dashboard
from app.backend.routes import article