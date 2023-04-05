"""Add man days fields

Revision ID: 9f8445f9b42c
Revises: e29638428dfd
Create Date: 2019-07-10 19:54:05.160074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9f8445f9b42c"
down_revision = "e29638428dfd"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "project", sa.Column("man_days", sa.Integer(), nullable=True)
    )
    op.add_column(
        "schedule_item", sa.Column("man_days", sa.Integer(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("schedule_item", "man_days")
    op.drop_column("project", "man_days")
    # ### end Alembic commands ###
