"""added added_by field

Revision ID: 6ddd36477708
Revises: 
Create Date: 2023-12-11 16:00:54.390190

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ddd36477708'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('opinion', sa.Column('added_by', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('opinion', 'added_by')
    # ### end Alembic commands ###
