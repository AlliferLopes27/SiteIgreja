from flask import Flask

from extensions import db
from extensions import login_manager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretkey'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/igreja_db'

# Inicializa banco

db.init_app(app)

# Inicializa login

login_manager.init_app(app)

login_manager.login_view = 'admin.login'

# Import usuário

from models.usuario import Usuario

# Carrega usuário logado

@login_manager.user_loader
def load_user(user_id):

    return Usuario.query.get(int(user_id))

# Importa rotas

from routes.site_routes import site_bp
from routes.admin_routes import admin_bp

# Registra blueprints

app.register_blueprint(site_bp)

app.register_blueprint(admin_bp)

# Executa servidor

app.run(
    host='0.0.0.0',
    port=5000,
    debug=True
)