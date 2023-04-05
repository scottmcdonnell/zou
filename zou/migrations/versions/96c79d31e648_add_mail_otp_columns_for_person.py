"""Add mail otp columns for Person

Revision ID: 96c79d31e648
Revises: 8a1b4a1b7f4a
Create Date: 2022-11-30 05:19:44.449553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "96c79d31e648"
down_revision = "8a1b4a1b7f4a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "person", sa.Column("email_otp_enabled", sa.Boolean(), nullable=True)
    )
    op.add_column(
        "person",
        sa.Column("email_otp_secret", sa.String(length=32), nullable=True),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("person", "email_otp_secret")
    op.drop_column("person", "email_otp_enabled")
    # ### end Alembic commands ###
