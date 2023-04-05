"""add max retake parameter

Revision ID: 5a291251823c
Revises: 4095103c7d01
Create Date: 2022-06-29 10:56:13.556495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5a291251823c"
down_revision = "4095103c7d01"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "project", sa.Column("max_retakes", sa.Integer(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("project", "max_retakes")
    # ### end Alembic commands ###
