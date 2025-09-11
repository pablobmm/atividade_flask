from flask_restx import Resource
from apps.swagger.namespace.task_namespaces import task_ns, task_model
from ..database import db
from .model_task import Task

@task_ns.route('/')
class TaskList(Resource):
    @task_ns.marshal_list_with(task_model)
    def get(self):
        """Lista todas as tarefas"""
        return Task.query.all()

    @task_ns.expect(task_model)
    @task_ns.marshal_with(task_model, code=201)
    def post(self):
        """Cria uma nova tarefa"""
        data = task_ns.payload
        new_task = Task(title=data['title'], description=data.get('description'), user_id=data['user_id'])
        db.session.add(new_task)
        db.session.commit()
        return new_task, 201

@task_ns.route('/<int:id>')
@task_ns.param('id', 'O ID da tarefa')
class TaskResource(Resource):
    @task_ns.marshal_with(task_model)
    def get(self, id):
        """Busca uma tarefa por ID"""
        return Task.query.get_or_404(id)

    @task_ns.expect(task_model)
    @task_ns.marshal_with(task_model)
    def put(self, id):
        """Atualiza uma tarefa"""
        task = Task.query.get_or_404(id)
        data = task_ns.payload
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        db.session.commit()
        return task

    def delete(self, id):
        """Exclui uma tarefa"""
        task = Task.query.get_or_404(id)
        db.session.delete(task)
        db.session.commit()
        return {'message': 'Tarefa excluída'}, 200