"""change notification unique constraint

Revision ID: 9060dd4f6116
Revises: 77d6820f494f
Create Date: 2021-11-14 21:20:23.848173

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = "9060dd4f6116"
down_revision = "77d6820f494f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("notification_uc", "notification", type_="unique")
    op.create_unique_constraint(
        "notification_uc",
        "notification",
        ["person_id", "author_id", "comment_id", "reply_id", "type"],
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("notification_uc", "notification", type_="unique")
    op.create_unique_constraint(
        "notification_uc",
        "notification",
        ["person_id", "author_id", "comment_id", "type"],
    )
    # ### end Alembic commands ###
