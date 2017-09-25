from app.backend import backend
from app.backend.forms.article import ArticleForm
from app.backend.models.article import Article
from flask_user import login_required, current_user
from flask import render_template, request, redirect, url_for, flash
from slugify import slugify


@backend.route('/article/list')
@login_required
def article_list():
    articles = Article.get()
    return render_template('backend/articles/index.j2', articles=articles)


@backend.route('/article/add', methods=['GET', 'POST'])
@backend.route('/article/edit/<slug>', methods=['GET', 'POST'])
@login_required
def article(slug=''):
    if slug:
        obj = Article.get('slug', slug)
        action = 'Edit'
    else:
        obj = Article()
        action = 'Add'

    form = ArticleForm(obj=obj)

    if request.method == 'POST' and form.validate():
        current_user.articles.append(obj)
        form.populate_obj(obj)
        obj.slug = slugify(obj.title)
        msg, cat = obj.save()

        flash(msg, cat)

        return redirect(url_for('backend.article_list'))

    return render_template('backend/articles/add.j2', form=form, action=action)


@backend.route('/article/<slug>')
def article_view(slug):
    obj = Article.query.filter(Article.slug == slug).first_or_404()
    return render_template('backend/articles/view.j2', article=obj)


@backend.route('/article/delete/<slug>')
def article_delete(slug):
    obj = Article.get('slug', slug)
    msg, cat = obj.delete()
    flash(msg, cat)

    return redirect(url_for('backend.article_list'))
