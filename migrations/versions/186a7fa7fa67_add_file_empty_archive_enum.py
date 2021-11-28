"""Add FILE_EMPTY_ARCHIVE enum

Revision ID: 186a7fa7fa67
Revises: e772522154a1
Create Date: 2021-11-29 01:00:28.241483

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "186a7fa7fa67"
down_revision = "e772522154a1"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.sync_enum_values(
        "public",
        "myerrors",
        ["FILE_NOT_EXISTS", "FILE_NOT_FOUND", "INCORRECT_ACCOUNT"],
        [
            "FILE_EMPTY_ARCHIVE",
            "FILE_NOT_EXISTS",
            "FILE_NOT_FOUND",
            "INCORRECT_ACCOUNT",
        ],
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.sync_enum_values(
        "public",
        "myerrors",
        [
            "FILE_EMPTY_ARCHIVE",
            "FILE_NOT_EXISTS",
            "FILE_NOT_FOUND",
            "INCORRECT_ACCOUNT",
        ],
        ["FILE_NOT_EXISTS", "FILE_NOT_FOUND", "INCORRECT_ACCOUNT"],
    )
    # ### end Alembic commands ###
