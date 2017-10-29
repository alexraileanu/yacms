from app import db
from app.backend.models.mixins import BaseMixin
import datetime
import slugify
import time


class Article(BaseMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    title = db.Column(db.String(length=255))
    slug = db.Column(db.String(length=255))
    content = db.Column(db.Text())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    comments = db.relationship('Comment', backref='article', lazy='dynamic')

    type = 'article'

    def __init__(self, title='', content=''):
        self.title = title
        self.content = content

    def make_slug(self):
        ymd = datetime.date.fromtimestamp(time.time()).strftime('%Y/%m/%d')
        slug = '{}/{}'.format(ymd, slugify.slugify(self.title))

        article_exists = self.exists('slug', slug)

        if article_exists:
            print(slug)
            # todo change slug and check until a free one is open. too lazy to do rn
        else:
            self.slug = slug
