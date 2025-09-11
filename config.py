import os

class Config:
    # O caminho do DB agora aponta para a pasta instance na raiz do projeto
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///../instance/tasks.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_VALIDATE = True
    RESTX_MASK_SWAGGER = False