from flask import Blueprint, render_template, request, redirect
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash
from extensions import db

from models.usuario import Usuario
from models.evento import Evento
from models.pedido import PedidoOracao

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


# CONTEXTO GLOBAL (cards dashboard)
@admin_bp.app_context_processor
def inject_stats():
    return {
        "total_eventos": Evento.query.count(),
        "total_pedidos": PedidoOracao.query.count()
    }


# LOGIN
@admin_bp.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        senha = request.form['senha']

        usuario = Usuario.query.filter_by(email=email).first()

        # LOGIN OK
        if usuario and check_password_hash(usuario.senha, senha):

            login_user(usuario)

            return redirect('/admin/dashboard?auth=login_success')

        # LOGIN FALHOU
        else:

            return redirect('/admin/login?auth=login_error')

    return render_template('admin/login.html')


# LOGOUT
@admin_bp.route('/logout')
@login_required
def logout():

    logout_user()

    return redirect('/admin/login?auth=logout_success')


# DASHBOARD (BASE)
@admin_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('admin/dashboard.html')


# EVENTOS
@admin_bp.route('/eventos')
@login_required
def eventos():
    eventos = Evento.query.all()
    return render_template('admin/eventos.html', eventos=eventos)


# NOVO EVENTO
@admin_bp.route('/eventos/novo', methods=['GET', 'POST'])
@login_required
def novo_evento():

    if request.method == 'POST':

        evento = Evento(
            titulo=request.form['titulo'],
            descricao=request.form['descricao'],
            data=request.form['data'],
            hora=request.form['hora']
        )

        db.session.add(evento)
        db.session.commit()

        return redirect('/admin/eventos?evento=criado')

    return render_template('admin/novo_evento.html')


# EDITAR EVENTO
@admin_bp.route('/eventos/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_evento(id):

    evento = Evento.query.get_or_404(id)

    if request.method == 'POST':

        evento.titulo = request.form['titulo']
        evento.descricao = request.form['descricao']
        evento.data = request.form['data']
        evento.hora = request.form['hora']

        db.session.commit()

        return redirect('/admin/eventos?evento=editado')

    return render_template('admin/editar_evento.html', evento=evento)


# EXCLUIR EVENTO
@admin_bp.route('/eventos/excluir/<int:id>')
@login_required
def excluir_evento(id):

    evento = Evento.query.get_or_404(id)

    db.session.delete(evento)
    db.session.commit()

    return redirect('/admin/eventos?evento=excluido')


# PEDIDOS
@admin_bp.route('/pedidos')
@login_required
def pedidos():

    pedidos = PedidoOracao.query.all()

    return render_template('admin/pedidos.html', pedidos=pedidos)