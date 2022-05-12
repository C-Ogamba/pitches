"""first migration

Revision ID: f9d38f9e485c
Revises: 63bc4d48c8e4
Create Date: 2022-05-12 09:05:51.803060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9d38f9e485c'
down_revision = '63bc4d48c8e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('body', sa.String(length=140), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'body')
    # ### end Alembic commands ###