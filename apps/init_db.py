from .app import app
from .config import db_serv
from .models.model_user import User
from .models.model_task import Task

print("Iniciando a criação das tabelas no banco de dados...")

with app.app_context():
    db_serv.create_all()

print("Tabelas criadas com sucesso!")