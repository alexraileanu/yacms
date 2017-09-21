from app.backend import backend, db
from flask_user import login_required, current_user
from app.backend.models.article import Article
from flask import render_template, request, redirect, url_for, flash
from app.backend.forms.article import ArticleForm
from slugify import slugify
from sqlalchemy.exc import SQLAlchemyError


@backend.route('/article/list')
@login_required
def article_list():
    articles = Article.query.all()
    return render_template('backend/articles/index.j2', articles=articles)


@backend.route('/article/add', methods=['GET', 'POST'])
@backend.route('/article/edit/<slug>', methods=['GET', 'POST'])
@login_required
def article(slug=''):
    if slug:
        obj = Article.query.filter(Article.slug == slug).first_or_404()
        action = 'Edit'
    else:
        obj = Article()
        action = 'Add'

    form = ArticleForm(obj=obj)

    if request.method == 'POST' and form.validate():
        current_user.articles.append(obj)
        form.populate_obj(obj)
        obj.slug = slugify(obj.title)

        try:
            db.session.add(obj)
            db.session.commit()

            if slug:
                flash('Article updated correctly', 'success')
            else:
                flash('Article added correctly', 'success')
        except SQLAlchemyError:
            if slug:
                flash('Error updating your article', 'error')
            else:
                flash('Error adding your article', 'error')

        return redirect(url_for('backend.article_list'))

    return render_template('backend/articles/add.j2', form=form, action=action)


@backend.route('/article/<slug>')
def article_view(slug):
    obj = Article.query.filter(Article.slug == slug)
    return render_template('backend/articles/view.j2', article=obj)


@backend.route('/article/delete/<slug>')
def article_delete(slug):
    obj = Article.query.filter(Article.slug == slug).first_or_404()

    try:
        db.session.delete(obj)
        db.session.commit()

        flash('Article deleted successfully', 'success')
    except SQLAlchemyError as e:
        print(str(e))
        flash('Error deleting article', 'error')

    return redirect(url_for('backend.article_list'))
