from flask import Flask
from flask_redis import FlaskRedis

REDIS_URL = "redis://localhost:6379"

redis_client = FlaskRedis()


def create_app(test_config=None):
    """
    Application Factory para gerar instancias da aplicação
    """

    # Criando instancia do Flask e configurando
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY="dev")
    if test_config is None:
        # Carrega o arquivo de configuração padrão se existir
        app.config.from_pyfile("config.py", silent=True)
    else:
        # Carrega arquivo de configuração de teste
        app.config.from_mapping(test_config)

    # Só um 'healthcheck'
    @app.route("/healthcheck")
    def healthcheck():
        return "Datebayou"

    from . import todo

    app.register_blueprint(todo.bp)
    redis_client.init_app(app)

    return app
