from models.task import db  
from flask_sqlalchemy import SQLAlchemy
from . import db 
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    tasks = db.relationship("Task", back_populates="user", lazy=True)

    def __repr__(self):
        return f'<User {self.name}>'