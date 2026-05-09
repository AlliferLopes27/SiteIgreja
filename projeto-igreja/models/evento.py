from extensions import db

class Evento(db.Model):

    __tablename__ = 'eventos'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    titulo = db.Column(
        db.String(200),
        nullable=False
    )

    descricao = db.Column(
        db.Text,
        nullable=False
    )

    data = db.Column(
        db.String(50),
        nullable=False
    )

    hora = db.Column(
        db.String(20),
        nullable=False
    )