from app.backend import backend
from app.backend.forms.cms import SettingsForm
from flask_user import login_required
from flask import request, redirect, url_for, render_template, flash
from app.backend.models.cms import CMS


@backend.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    obj = CMS()
    form = SettingsForm(
        site_title=CMS.get('site_title'),
        site_timezone=CMS.get('site_timezone'),
    )

    if request.method == 'POST' and form.validate():
        form.populate_obj(obj)
        msg, cat = obj.save()

        flash(msg, cat)

        return redirect(url_for('backend.settings'))

    return render_template('backend/cms/settings.j2', form=form)
