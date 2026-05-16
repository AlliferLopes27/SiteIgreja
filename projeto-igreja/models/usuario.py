# Importa a extensão do banco de dados
from extensions import db

# Importa recursos de autenticação do Flask-Login
from flask_login import UserMixin

# Classe responsável pela tabela de usuários
class Usuario(UserMixin, db.Model):

    # Nome da tabela no banco
    __tablename__ = 'usuarios'

    # ID do usuário (chave primária)
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # Nome do usuário
    nome = db.Column(
        db.String(150),
        nullable=False
    )

    # Email do usuário
    email = db.Column(
        db.String(150),
        unique=True,
        nullable=False
    )

    # Senha criptografada do usuário
    senha = db.Column(
        db.String(255),
        nullable=False
    )
