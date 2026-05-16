# Importa a extensão do banco de dados
from extensions import db

# Classe responsável pela tabela de pedidos de oração
class PedidoOracao(db.Model):

    # Nome da tabela no banco
    __tablename__ = 'pedidos_oracao'

    # ID do pedido (chave primária)
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # Nome da pessoa
    nome = db.Column(
        db.String(150),
        nullable=False
    )

    # Email da pessoa
    email = db.Column(
        db.String(150),
        nullable=False
    )

    # Texto do pedido de oração
    pedido = db.Column(
        db.Text,
        nullable=False
    )
