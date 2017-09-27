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
        article = Article.get('id', form.article_id.data)

        form.populate_obj(obj)
        article.comments.append(obj)

        msg, cat = obj.save()

        # this has to be after saving the comment itself as the session is commited when appending
        # comments to the user (so then we lose track of whether the comment is new or not)
        if current_user.is_authenticated:
            current_user.comments.append(obj)

        flash(msg, cat)

    return redirect(request.referrer)
