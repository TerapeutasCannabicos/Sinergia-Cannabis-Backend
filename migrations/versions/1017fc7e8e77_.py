"""empty message

Revision ID: 1017fc7e8e77
Revises: 
Create Date: 2021-05-04 15:47:40.767828

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1017fc7e8e77'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('administrador',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('sobrenome', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('cpf', sa.String(length=30), nullable=False),
    sa.Column('celular', sa.String(length=20), nullable=False),
    sa.Column('telefone_secundario', sa.String(length=20), nullable=True),
    sa.Column('endereço', sa.String(length=500), nullable=False),
    sa.Column('bairro', sa.String(length=200), nullable=False),
    sa.Column('numero', sa.Integer(), nullable=False),
    sa.Column('complemento', sa.String(length=50), nullable=False),
    sa.Column('cidade', sa.String(length=200), nullable=False),
    sa.Column('estado', sa.String(length=200), nullable=False),
    sa.Column('cep', sa.String(length=50), nullable=False),
    sa.Column('nome_associação', sa.String(length=200), nullable=False),
    sa.Column('password_hash', sa.LargeBinary(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email')
    )
    op.create_table('advogado',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('sobrenome', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('cpf', sa.String(length=30), nullable=False),
    sa.Column('celular', sa.String(length=20), nullable=False),
    sa.Column('telefone_secundario', sa.String(length=20), nullable=True),
    sa.Column('endereço', sa.String(length=500), nullable=False),
    sa.Column('bairro', sa.String(length=200), nullable=False),
    sa.Column('numero', sa.Integer(), nullable=False),
    sa.Column('complemento', sa.String(length=50), nullable=False),
    sa.Column('cidade', sa.String(length=200), nullable=False),
    sa.Column('estado', sa.String(length=200), nullable=False),
    sa.Column('cep', sa.String(length=50), nullable=False),
    sa.Column('password_hash', sa.LargeBinary(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email')
    )
    op.create_table('gestor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('sobrenome', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('cpf', sa.String(length=30), nullable=False),
    sa.Column('rg', sa.String(length=30), nullable=False),
    sa.Column('celular', sa.String(length=20), nullable=False),
    sa.Column('telefone_secundario', sa.String(length=20), nullable=True),
    sa.Column('endereço', sa.String(length=500), nullable=False),
    sa.Column('bairro', sa.String(length=200), nullable=False),
    sa.Column('numero', sa.Integer(), nullable=False),
    sa.Column('complemento', sa.String(length=50), nullable=False),
    sa.Column('cidade', sa.String(length=200), nullable=False),
    sa.Column('estado', sa.String(length=200), nullable=False),
    sa.Column('cep', sa.String(length=50), nullable=False),
    sa.Column('password_hash', sa.LargeBinary(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('rg')
    )
    op.create_table('medico',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('sobrenome', sa.String(length=100), nullable=False),
    sa.Column('especialidade', sa.String(length=100), nullable=False),
    sa.Column('sexo', sa.String(length=2000), nullable=True),
    sa.Column('Bio', sa.String(length=100), nullable=True),
    sa.Column('foto_perfil', sa.String(length=2000), nullable=True),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('facebook', sa.String(length=100), nullable=True),
    sa.Column('twitter', sa.String(length=100), nullable=True),
    sa.Column('instagram', sa.String(length=100), nullable=True),
    sa.Column('cpf', sa.String(length=30), nullable=False),
    sa.Column('rg', sa.String(length=30), nullable=False),
    sa.Column('celular', sa.String(length=20), nullable=False),
    sa.Column('telefone_secundario', sa.String(length=20), nullable=True),
    sa.Column('endereço', sa.String(length=500), nullable=False),
    sa.Column('bairro', sa.String(length=200), nullable=False),
    sa.Column('numero', sa.Integer(), nullable=False),
    sa.Column('complemento', sa.String(length=50), nullable=False),
    sa.Column('cidade', sa.String(length=200), nullable=False),
    sa.Column('estado', sa.String(length=200), nullable=False),
    sa.Column('cep', sa.String(length=50), nullable=False),
    sa.Column('password_hash', sa.LargeBinary(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('rg')
    )
    op.create_table('paciente',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('sobrenome', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('cpf', sa.String(length=30), nullable=False),
    sa.Column('rg', sa.String(length=30), nullable=False),
    sa.Column('documentos_pessoais', sa.String(length=2000), nullable=False),
    sa.Column('diagnóstico', sa.String(length=2000), nullable=False),
    sa.Column('laudo_médico', sa.String(length=2000), nullable=False),
    sa.Column('receita_médica', sa.String(length=2000), nullable=False),
    sa.Column('endereço', sa.String(length=500), nullable=False),
    sa.Column('bairro', sa.String(length=200), nullable=False),
    sa.Column('numero', sa.Integer(), nullable=False),
    sa.Column('complemento', sa.String(length=50), nullable=False),
    sa.Column('cidade', sa.String(length=200), nullable=False),
    sa.Column('estado', sa.String(length=200), nullable=False),
    sa.Column('password_hash', sa.LargeBinary(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('rg')
    )
    op.create_table('reponsavel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('sobrenome', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('celular', sa.String(length=20), nullable=False),
    sa.Column('telefone_secundario', sa.String(length=20), nullable=True),
    sa.Column('endereço', sa.String(length=500), nullable=False),
    sa.Column('bairro', sa.String(length=200), nullable=False),
    sa.Column('numero', sa.Integer(), nullable=False),
    sa.Column('complemento', sa.String(length=50), nullable=False),
    sa.Column('cidade', sa.String(length=200), nullable=False),
    sa.Column('estado', sa.String(length=200), nullable=False),
    sa.Column('password_hash', sa.LargeBinary(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reponsavel')
    op.drop_table('paciente')
    op.drop_table('medico')
    op.drop_table('gestor')
    op.drop_table('advogado')
    op.drop_table('administrador')
    # ### end Alembic commands ###
