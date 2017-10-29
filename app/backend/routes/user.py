from app.backend import backend
from app.backend.forms.image import ImageForm
from flask_user import login_required, current_user
from flask import render_template
import sys


@backend.route('/me')
@login_required
def me():
    image_form = ImageForm()
    return render_template('backend/user/profile.j2', user=current_user, image_form=image_form)


@backend.route('/me/<attr>/change')
@login_required
def attr_change(attr):
    return render_template('backend/user/change{}.j2'.format(attr.upper()), user=current_user)
