from extensions import db

class PedidoOracao(db.Model):

    __tablename__ = 'pedidos_oracao'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(150),
        nullable=False
    )

    email = db.Column(
        db.String(150),
        nullable=False
    )

    pedido = db.Column(
        db.Text,
        nullable=False
    )