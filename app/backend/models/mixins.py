from app.backend import db
from sqlalchemy.exc import SQLAlchemyError


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
