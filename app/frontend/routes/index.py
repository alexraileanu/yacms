from app.frontend import frontend
from flask import render_template
from flask_user import current_user


@frontend.route('/')
def index():
    name = ''

    # TODO: add index
    if current_user.is_authenticated:
        name = current_user.username

    return render_template('frontend/index.j2', username=name)
