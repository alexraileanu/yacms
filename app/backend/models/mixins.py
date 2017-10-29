from app.backend import db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import exists


class BaseMixin(object):
    def save(self):
        # store the id before saving to check whether or not an object is new
        # if the id here is None then the object is new and i show some message
        # if it's not new, then i show some other message
        # idk
        id = self.id

        try:
            db.session.add(self)
            db.session.commit()

            if id:
                msg = '{} updated correctly'.format(self.type.capitalize())
            else:
                msg = '{} added correctly'.format(self.type.capitalize())

            cat = 'success'
        except SQLAlchemyError:
            if id:
                msg = 'Error updating your {}'.format(self.type)
            else:
                msg = 'Error saving your {}'.format(self.type)

            cat = 'error'

        return msg, cat

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()

            msg, cat = '{} deleted successfully'.format(self.type.capitalize()), 'success'
        except SQLAlchemyError:
            msg, cat = 'Error deleting {}'.format(self.type), 'error'

        return msg, cat

    """
        get an object from the database based on a filter column (if set).

        defaults to getting all the objects
    """

    @classmethod
    def get(cls, filter_column=None, filter_value=None):
        if filter_column:
            return cls.query.filter(getattr(cls, filter_column) == filter_value).first_or_404()

        return cls.query.all()

    """
        checks if an object with filter_column = filter_value exists in the db
    """

    @classmethod
    def exists(cls, filter_column=None, filter_value=None):
        return db.session.query(exists().where(getattr(cls, filter_column) == filter_value)).scalar()