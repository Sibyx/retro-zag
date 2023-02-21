"""init

Revision ID: 3106846d7297
Revises: 
Create Date: 2023-02-21 22:44:53.097539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3106846d7297'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('records',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('stage', sa.String(), nullable=True),
    sa.Column('answer', sa.String(), nullable=False),
    sa.Column('assignment', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('records')
    # ### end Alembic commands ###
