from ..swagger_config import api
from flask_restx import fields

task_ns = api.namespace('tasks', description='Operações relacionadas a tarefas')

task_model = api.model('TaskModel', {
    'id': fields.Integer(readonly=True),
    'title': fields.String(required=True, description='Título da tarefa'),
    'description': fields.String(description='Descrição da tarefa'),
    'status': fields.String(readonly=True, default='Pendente'),
    'user_id': fields.Integer(required=True, description='ID do usuário associado')
})