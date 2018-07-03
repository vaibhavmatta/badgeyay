"""empty message

Revision ID: e7e7c9ed6863
Revises: f82c06cf3a14
Create Date: 2018-07-03 14:03:40.492846

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7e7c9ed6863'
down_revision = 'f7bd4949b116'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Modules',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ticketInclude', sa.Boolean(), nullable=True),
    sa.Column('paymentInclude', sa.Boolean(), nullable=True),
    sa.Column('donationInclude', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Modules')
    # ### end Alembic commands ###
