from app.backend import backend
from flask_user import login_required, current_user
from flask import render_template


@backend.route('/')
@login_required
def index():
    return render_template('backend/index.j2', user=current_user)
