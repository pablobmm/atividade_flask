from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String, nullable = False)
    desc = db.Column(db.String, nullable = True)
    status = db.Column(db.String, nullable = False, default = "Pendente")
    user_id = db.Column(db.Integer, db.ForeignKey ('users.id'))
