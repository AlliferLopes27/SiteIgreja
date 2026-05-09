from app import app

from extensions import db

from models.usuario import Usuario

from werkzeug.security import generate_password_hash

with app.app_context():

    admin = Usuario(

        nome='Administrador',

        email='admin@admin.com',

        senha=generate_password_hash('12345@')
    )

    db.session.add(admin)

    db.session.commit()

    print('Administrador criado com sucesso')