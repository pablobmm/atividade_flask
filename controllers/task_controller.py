from flask import request, jsonify
from models.task import Task
from models.user import User
from . import db

def list_tasks():
    """
    Listar todas as tarefas
    ---
    tags:
      - Tasks
    responses:
      200:
        description: Lista de tarefas
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              title:
                type: string
              user_id:
                type: integer
              done:
                type: boolean
    """
    tasks = Task.query.all()
    tasks_list = [task.to_dict() for task in tasks]
    return jsonify(tasks_list), 200

def create_task():
    """
    Criar uma nova tarefa
    ---
    tags:
      - Tasks
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - title
            - user_id
          properties:
            title:
              type: string
            user_id:
              type: integer
    responses:
      201:
        description: Tarefa criada com sucesso
        schema:
          type: object
          properties:
            id:
              type: integer
            title:
              type: string
            user_id:
              type: integer
            done:
              type: boolean
      400:
        description: Dados inválidos ou usuário não encontrado
    """
    data = request.get_json()
    if not data or 'title' not in data or 'user_id' not in data:
        return jsonify({'error': 'title e user_id são obrigatórios'}), 400

    user = User.query.get(data['user_id'])
    if not user:
        return jsonify({'error': 'Usuário não encontrado'}), 400

    new_task = Task(title=data['title'], user_id=data['user_id'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201

def update_task(task_id):
    """
    Atualizar uma tarefa existente
    ---
    tags:
      - Tasks
    parameters:
      - in: path
        name: task_id
        type: integer
        required: true
        description: ID da tarefa a ser atualizada
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
            user_id:
              type: integer
            done:
              type: boolean
    responses:
      200:
        description: Tarefa atualizada com sucesso
        schema:
          type: object
          properties:
            id:
              type: integer
            title:
              type: string
            user_id:
              type: integer
            done:
              type: boolean
      400:
        description: Dados inválidos ou usuário não encontrado
      404:
        description: Tarefa não encontrada
    """
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Tarefa não encontrada'}), 404

    data = request.get_json()
    if not data:
        return jsonify({'error': 'Nenhum dado para atualizar'}), 400

    if 'user_id' in data:
        user = User.query.get(data['user_id'])
        if not user:
            return jsonify({'error': 'Usuário não encontrado'}), 400
        task.user_id = data['user_id']

    if 'title' in data:
        task.title = data['title']
    if 'done' in data:
        task.done = data['done']

    db.session.commit()
    return jsonify(task.to_dict()), 200

def delete_task(task_id):
    """
    Excluir uma tarefa
    ---
    tags:
      - Tasks
    parameters:
      - in: path
        name: task_id
        type: integer
        required: true
        description: ID da tarefa a ser excluída
    responses:
      200:
        description: Tarefa excluída com sucesso
      404:
        description: Tarefa não encontrada
    """
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Tarefa não encontrada'}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Tarefa excluída com sucesso'}), 200