from app.frontend import frontend
from flask import render_template, url_for
from flask_user import current_user
from app.backend.models.article import Article
from app.frontend.forms.comment import CommentForm


@frontend.route('/article/<path:slug>')
def article_view(slug):
    obj = Article.get('slug', slug)
    comment_form = CommentForm(article_id=obj.id)
    comment_form.action = url_for('frontend.comment')

    return render_template('frontend/articles/view.j2',
                           article=obj,
                           comment_form=comment_form,
                           user=current_user
                           )
