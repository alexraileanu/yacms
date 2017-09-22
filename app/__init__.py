from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_pyfile('../config/config.cfg')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.backend import backend
from app.frontend import frontend
from app.backend.commands import seed

app.register_blueprint(frontend)
app.register_blueprint(backend)

from arrow import get
# idk where else to put this template filter *shrug*

@app.template_filter('date')
def date(string, format):
    return get(string).format(format)
