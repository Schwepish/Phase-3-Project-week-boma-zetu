"""Added Agent, CommercialProperty and ResidentialProperty models

Revision ID: 88ec72ab0c6b
Revises: 2474f5376957
Create Date: 2023-09-06 14:08:12.603050

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '88ec72ab0c6b'
down_revision: Union[str, None] = '2474f5376957'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('commercial_properties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('area', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('grade', sa.String(), nullable=True),
    sa.Column('price_per_sqf', sa.Integer(), nullable=True),
    sa.Column('agent_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['agent_id'], ['agents.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('residential_properties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('area', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('bedrooms', sa.Integer(), nullable=True),
    sa.Column('bathrooms', sa.Integer(), nullable=True),
    sa.Column('floor_space_sqf', sa.Integer(), nullable=True),
    sa.Column('price_per_sqf', sa.Integer(), nullable=True),
    sa.Column('agent_id', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['agent_id'], ['agents.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('residential_properties')
    op.drop_table('commercial_properties')
    op.drop_table('agents')
    # ### end Alembic commands ###
