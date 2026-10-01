from flask import Flask

from config import Config
from database import init_db
from routes import register_blueprints


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_blueprints(app)
    return app


app = create_app()

if __name__ == "__main__":
    # Cria as tabelas na primeira execução, caso ainda não existam.
    init_db()
    app.run(debug=True)
