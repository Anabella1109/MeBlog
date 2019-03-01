"""add username columnin comment table

Revision ID: a002d432a443
Revises: d9762465fb43
Create Date: 2019-03-01 13:11:52.611617

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a002d432a443'
down_revision = 'd9762465fb43'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('username', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'username')
    # ### end Alembic commands ###
