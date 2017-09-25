from app.frontend import frontend
from app.backend.models.comment import Comment
from app.backend.models.article import Article
from app.frontend.forms.comment import CommentForm
from flask import request, flash, redirect
from flask_user import current_user


@frontend.route('/comment/add', methods=['POST'])
def comment():
    obj = Comment()

    form = CommentForm(obj=obj)

    if request.method == 'POST' and form.validate():
        if current_user.is_authenticated:
            current_user.comments.append(obj)

        article = Article.get('id', form.article_id.data)

        form.populate_obj(obj)
        article.comments.append(obj)

        msg, cat = obj.save()
        flash(msg, cat)

    return redirect(request.referrer)
