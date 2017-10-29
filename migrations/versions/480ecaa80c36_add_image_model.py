"""add image model

Revision ID: 480ecaa80c36
Revises: 2dc3a426d4d4
Create Date: 2017-10-08 10:55:45.546676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '480ecaa80c36'
down_revision = '2dc3a426d4d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('original_name', sa.String(length=255), nullable=True),
    sa.Column('uid', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('image')
    # ### end Alembic commands ###
