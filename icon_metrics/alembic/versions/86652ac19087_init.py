"""init

Revision ID: 86652ac19087
Revises:
Create Date: 2021-10-11 22:47:49.971077

"""
import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision = "86652ac19087"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "addresses",
        sa.Column("address", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("organization_wallet", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("address"),
    )
    op.create_index(op.f("ix_addresses_address"), "addresses", ["address"], unique=False)
    op.create_index(
        op.f("ix_addresses_organization_wallet"), "addresses", ["organization_wallet"], unique=False
    )
    op.create_table(
        "supply",
        sa.Column("id", sa.Integer(), nullable=True),
        sa.Column("timestamp", sa.Integer(), nullable=True),
        sa.Column("total_supply", sa.Float(), nullable=True),
        sa.Column("organization_supply", sa.Float(), nullable=True),
        sa.Column("circulating_supply", sa.Float(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_supply_id"), "supply", ["id"], unique=False)
    op.create_index(op.f("ix_supply_timestamp"), "supply", ["timestamp"], unique=False)
    op.create_table(
        "transactions",
        sa.Column("id", sa.Integer(), nullable=True),
        sa.Column("timestamp", sa.Integer(), nullable=True),
        sa.Column("total_tx", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_transactions_id"), "transactions", ["id"], unique=False)
    op.create_index(op.f("ix_transactions_timestamp"), "transactions", ["timestamp"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_transactions_timestamp"), table_name="transactions")
    op.drop_index(op.f("ix_transactions_id"), table_name="transactions")
    op.drop_table("transactions")
    op.drop_index(op.f("ix_supply_timestamp"), table_name="supply")
    op.drop_index(op.f("ix_supply_id"), table_name="supply")
    op.drop_table("supply")
    op.drop_index(op.f("ix_addresses_organization_wallet"), table_name="addresses")
    op.drop_index(op.f("ix_addresses_address"), table_name="addresses")
    op.drop_table("addresses")
    # ### end Alembic commands ###
