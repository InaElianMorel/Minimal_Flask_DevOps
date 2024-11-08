"""initial migration

Revision ID: 80e71b6b2e13
Revises: 
Create Date: 2024-11-07 10:10:24.722837

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80e71b6b2e13'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('todo', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todo_list')
    # ### end Alembic commands ###
