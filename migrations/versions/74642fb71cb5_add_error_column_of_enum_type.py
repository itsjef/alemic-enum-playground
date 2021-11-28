"""Add error column of enum type

Revision ID: 74642fb71cb5
Revises: b98d25057475
Create Date: 2021-11-29 00:43:24.472894

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "74642fb71cb5"
down_revision = "b98d25057475"
branch_labels = None
depends_on = None

error_type = postgresql.ENUM("INCORRECT_ACCOUNT", name="myerrors")


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    error_type.create(op.get_bind(), checkfirst=False)
    op.add_column("my_table", sa.Column("error", error_type, nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("my_table", "error")
    error_type.drop(op.get_bind(), checkfirst=False)
    # ### end Alembic commands ###
