# Importa banco

from app import db

# Importa model

from models.pedido import Oracao

# Salvar pedido

def salvar_pedido(nome, email, pedido):

    novo_pedido = Oracao(

        nome=nome,
        email=email,
        pedido=pedido
    )

    db.session.add(novo_pedido)

    db.session.commit()

# Listar pedidos

def listar_pedidos():

    return Oracao.query.all()