import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["HOST"] = "0.0.0.0"
app.config["PORT"] = 5002
app.config["DEBUG"] = True

DB_USER = os.environ.get("DB_USER") or 'adm'
DB_PASSWORD = os.environ.get("DB_PASSWORD") or '12345'
DB_HOST = os.environ.get("DB_HOST") or 'localhost'
DB_PORT =  int(os.environ.get("DB_PORT",3306))
DB_NAME = os.environ.get("DB_NAME") or "ProjetoFlask"

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
db_serv = SQLAlchemy(app)