from app.backend import backend
from flask_user import login_required, current_user


@backend.route('/')
@login_required
def index():
    return 'hello'
