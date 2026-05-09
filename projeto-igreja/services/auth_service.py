# Importações

from models.usuario import Usuario

from werkzeug.security import check_password_hash

# Função de login

def autenticar_usuario(email, senha):

    # Busca usuário pelo email

    usuario = Usuario.query.filter_by(email=email).first()

    # Verifica se usuário existe

    if usuario:

        # Verifica senha criptografada

        if check_password_hash(usuario.senha, senha):

            return usuario

    return None