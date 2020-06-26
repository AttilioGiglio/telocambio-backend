"""empty message

Revision ID: 0e0b131604ee
Revises: 
Create Date: 2020-06-26 11:14:07.790415

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e0b131604ee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=100), nullable=True),
    sa.Column('lastname', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.Column('password', sa.String(length=200), nullable=True),
    sa.Column('role', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('tags', sa.String(length=200), nullable=True),
    sa.Column('shortDesc', sa.String(length=600), nullable=True),
    sa.Column('longDesc', sa.String(length=1000), nullable=True),
    sa.Column('cover_img', sa.String(length=600), nullable=True),
    sa.Column('gallery', sa.String(length=600), nullable=True),
    sa.Column('tradeBy', sa.String(length=600), nullable=True),
    sa.Column('username', sa.String(length=600), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('done', sa.Integer(), nullable=True),
    sa.Column('offers', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('productswap',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('oferta_id', sa.Integer(), nullable=False),
    sa.Column('muestra_id', sa.Integer(), nullable=False),
    sa.Column('done', sa.Boolean(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['muestra_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['oferta_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('productswap')
    op.drop_table('product')
    op.drop_table('user')
    # ### end Alembic commands ###
