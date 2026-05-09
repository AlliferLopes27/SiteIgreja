from flask import Blueprint, render_template, request, redirect

from extensions import db
from models.evento import Evento
from models.pedido import PedidoOracao

site_bp = Blueprint('site', __name__)

# Página inicial
@site_bp.route('/')
def home():

    eventos = Evento.query.all()

    return render_template(
        'index.html',
        eventos=eventos
    )

# Sobre
@site_bp.route('/sobre')
def sobre():

    return render_template('sobre.html')

# Agenda
@site_bp.route('/agenda')
def agenda():

    eventos = Evento.query.all()

    return render_template(
        'agenda.html',
        eventos=eventos
    )

# Contato
@site_bp.route('/contato')
def contato():

    return render_template('contato.html')

# ORAÇÃO (COM TOAST FUNCIONANDO)
@site_bp.route('/oracao', methods=['GET', 'POST'])
def oracao():

    if request.method == 'POST':

        nome = request.form['nome']
        email = request.form['email']
        pedido = request.form['pedido']

        novo_pedido = PedidoOracao(
            nome=nome,
            email=email,
            pedido=pedido
        )

        db.session.add(novo_pedido)
        db.session.commit()

        # sinal para o JS mostrar toast
        return redirect('/oracao?enviado=1')

    return render_template('oracao.html')