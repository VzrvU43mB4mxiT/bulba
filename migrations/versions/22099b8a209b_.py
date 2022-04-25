"""empty message

Revision ID: 22099b8a209b
Revises: 
Create Date: 2022-04-21 22:34:27.050750

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22099b8a209b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('email', sa.String(length=256), nullable=False),
    sa.Column('nome', sa.String(length=64), nullable=False),
    sa.Column('sobrenome', sa.String(length=64), nullable=False),
    sa.Column('cpf', sa.String(length=8), nullable=False),
    sa.Column('nacionalidade', sa.String(length=64), nullable=False),
    sa.Column('cep', sa.String(length=8), nullable=False),
    sa.Column('estado', sa.String(length=64), nullable=False),
    sa.Column('cidade', sa.String(length=64), nullable=False),
    sa.Column('logradouro', sa.String(length=128), nullable=False),
    sa.Column('telefone', sa.String(length=14), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###