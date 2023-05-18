"""todo app

Revision ID: 53fef0124a44
Revises: 04bd456c74fd
Create Date: 2023-05-18 17:49:50.755478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53fef0124a44'
down_revision = '04bd456c74fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.drop_column('created')

    # ### end Alembic commands ###