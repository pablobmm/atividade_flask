from flask import Flask
import os
from config import Config
from .database import db
from .swagger.swagger_config import api
from .database import db

# Importa os namespaces para registro
from .swagger.namespace.user_namespace import user_ns
from .swagger.namespace.task_namespaces import task_ns

def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)

    # Garante que a pasta 'instance' exista na raiz do projeto
    instance_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'instance')
    try:
        os.makedirs(instance_path)
    except OSError:
        pass

    db.init_app(app)
    api.init_app(app)

    # Adiciona os namespaces à API
    api.add_namespace(user_ns)
    api.add_namespace(task_ns)

    return app