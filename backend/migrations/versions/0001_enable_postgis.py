"""Ensure PostGIS is enabled in the target database.

Revision ID: 0001_enable_postgis
Revises:
Create Date: 2026-11-06
"""

from alembic import op

revision = "0001_enable_postgis"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE EXTENSION IF NOT EXISTS postgis")


def downgrade() -> None:
    # Leave PostGIS installed: it is a database capability and may be shared by
    # other objects or applications. Schema migrations can remove their own use.
    pass
