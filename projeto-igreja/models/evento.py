# Importa a extensão do banco de dados
from extensions import db

# Classe responsável pela tabela de eventos
class Evento(db.Model):

    # Nome da tabela no banco
    __tablename__ = 'eventos'

    # ID do evento (chave primária)
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # Título do evento
    titulo = db.Column(
        db.String(200),
        nullable=False
    )

    # Descrição do evento
    descricao = db.Column(
        db.Text,
        nullable=False
    )

    # Data do evento
    data = db.Column(
        db.String(50),
        nullable=False
    )

    # Horário do evento
    hora = db.Column(
        db.String(20),
        nullable=False
    )
