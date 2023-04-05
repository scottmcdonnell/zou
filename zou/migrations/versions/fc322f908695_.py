"""empty message

Revision ID: fc322f908695
Revises: f995b28fb749
Create Date: 2018-09-18 20:25:14.447916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "fc322f908695"
down_revision = "f995b28fb749"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "project",
        sa.Column("production_type", sa.String(length=20), nullable=True),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("project", "production_type")
    # ### end Alembic commands ###
