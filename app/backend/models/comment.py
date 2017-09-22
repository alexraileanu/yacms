from app import db
import datetime


class Comment(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    author = db.Column(db.String(length=255))
    content = db.Column(db.Text())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, title='', content=''):
        print(title)
        self.title = title
        self.content = content
