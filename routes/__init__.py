from routes.auth import auth_bp
from routes.main import main_bp
from routes.records import records_bp


def register_blueprints(app):
    """Registra todas as rotas. Ao criar uma entidade nova, adicione aqui."""
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(records_bp)
