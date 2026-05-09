# Importa banco

from app import db

# Importa model

from models.evento import Evento

# Listar eventos

def listar_eventos():

    return Evento.query.all()

# Buscar evento

def buscar_evento(id):

    return Evento.query.get(id)

# Criar evento

def criar_evento(titulo, descricao, data, hora):

    novo_evento = Evento(

        titulo=titulo,
        descricao=descricao,
        data=data,
        hora=hora
    )

    db.session.add(novo_evento)

    db.session.commit()

# Atualizar evento

def atualizar_evento(evento):

    db.session.commit()

# Excluir evento

def excluir_evento(evento):

    db.session.delete(evento)

    db.session.commit()