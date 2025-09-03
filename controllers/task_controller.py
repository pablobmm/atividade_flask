from flask import request, jsonify
from models.task import Task
from models.users import User
from models import db

class TaskController:

    @staticmethod
    def list_tasks():
        tasks = Task.query.all()
        output = []
        for task in tasks:
            task_data = {
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'status': task.status,
                'user_id': task.user_id
            }
            output.append(task_data)
        return jsonify({'tasks': output})

    @staticmethod
    def create_task():
        data = request.get_json()
        new_task = Task(
            title=data['title'],
            description=data.get('description', ''),
            user_id=data['user_id']
        )
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'message': 'Nova tarefa criada!'}), 201

    @staticmethod
    def update_task(task_id):
        task = Task.query.get(task_id)
        if not task:
            return jsonify({'message': 'Tarefa não encontrada'}), 404

        data = request.get_json()
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.status = data.get('status', task.status)
        
        db.session.commit()
        return jsonify({'message': 'Tarefa atualizada!'})

    @staticmethod
    def delete_task(task_id):
        task = Task.query.get(task_id)
        if not task:
            return jsonify({'message': 'Tarefa não encontrada'}), 404

        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Tarefa excluída!'})