import click
from app import app, db
from app.backend.models.user import User
from app.backend.models.cms import CMS
from app.backend import user_manager
from sqlalchemy.exc import SQLAlchemyError
from redis.exceptions import RedisError


@app.cli.command()
def seed():
    """
    Add initial users to the db.
    """
    user = User(username='demo', password=user_manager.hash_password('demo'))
    try:
        db.session.add(user)
        db.session.commit()
        click.echo('added user {} to the db'.format(user.username))
    except SQLAlchemyError as e:
        click.echo('error occurred: {}'.format(str(e)))


@app.cli.command()
def prepare_redis():
    """
    Add default settings to Redis
    """
    cms = CMS()
    cms.site_title = 'YaCMS'
    cms.site_timezone = 'Europe/Amsterdam'
    cms.site_date_format = 'Do of MMMM, YYYY'

    try:
        cms.save()
        click.echo('initial redis settings saved successfully')
    except RedisError as e:
        click.echo('error occurred: {}'.format(str(e)))
