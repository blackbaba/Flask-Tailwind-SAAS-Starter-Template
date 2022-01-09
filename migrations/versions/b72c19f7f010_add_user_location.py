"""add user location

Revision ID: b72c19f7f010
Revises: f673d9097f3f
Create Date: 2022-01-07 19:33:43.916529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b72c19f7f010'
down_revision = 'f673d9097f3f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('location', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'location')
    # ### end Alembic commands ###
