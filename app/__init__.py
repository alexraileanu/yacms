from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_redis import FlaskRedis

app = Flask(__name__)
app.config.from_pyfile('../config/config.cfg')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
redis_instance = FlaskRedis(app)

from app.backend import backend
from app.frontend import frontend
from app.backend.commands import seed

app.register_blueprint(frontend)
app.register_blueprint(backend)
