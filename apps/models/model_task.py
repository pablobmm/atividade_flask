# apps/models/model_task.py
from ..config import db_serv  # Importa a instância do DB do arquivo config

class Task(db_serv.Model):
    __tablename__ = 'tasks'

    id = db_serv.Column(db_serv.Integer, primary_key=True)
    title = db_serv.Column(db_serv.String(120), nullable=False)
    description = db_serv.Column(db_serv.Text, nullable=True)
    status = db_serv.Column(db_serv.String(50), nullable=False, default='Pendente')

    # Chave estrangeira para criar o relacionamento com a tabela de usuários
    user_id = db_serv.Column(db_serv.Integer, db_serv.ForeignKey('users.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'user_id': self.user_id
        }