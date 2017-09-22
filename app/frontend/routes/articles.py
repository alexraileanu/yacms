from app.frontend import frontend
from flask import render_template
from app.backend.models.article import Article


@frontend.route('/article/<slug>')
def article_view(slug):
    obj = Article.query.filter(Article.slug == slug).first_or_404()

    return render_template('frontend/articles/view.j2', article=obj)
