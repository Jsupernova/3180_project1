"""empty message

Revision ID: cbc74a6b2c8b
Revises: 
Create Date: 2022-03-23 09:15:10.649709

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbc74a6b2c8b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('properties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('property_name', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('rooms_num', sa.Integer(), nullable=True),
    sa.Column('bathrooms_num', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('property_type', sa.String(length=9), nullable=True),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.Column('photo', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('properties')
    # ### end Alembic commands ###
