"""nullable

Revision ID: 575419e8dca5
Revises: 3106846d7297
Create Date: 2023-02-21 22:57:43.463621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '575419e8dca5'
down_revision = '3106846d7297'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('records', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('stage',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('records', schema=None) as batch_op:
        batch_op.alter_column('stage',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###
