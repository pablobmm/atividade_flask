from flask import request, jsonify
from models.user import User, db

def list_users():
    """
    Listar todos os usuários
    ---
    tags:
      - Users
    responses:
      200:
        description: Lista de usuários
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              username:
                type: string
              email:
                type: string
    """
    users = User.query.all()
    users_list = [user.to_dict() for user in users]
    return jsonify(users_list), 200

def create_user():
    """
    Criar um novo usuário
    ---
    tags:
      - Users
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - username
            - email
          properties:
            username:
              type: string
            email:
              type: string
    responses:
      201:
        description: Usuário criado com sucesso
        schema:
          type: object
          properties:
            id:
              type: integer
            username:
              type: string
            email:
              type: string
      400:
        description: Dados inválidos ou usuário já existe
    """
    data = request.get_json()
    if not data or 'username' not in data or 'email' not in data:
        return jsonify({'error': 'username e email são obrigatórios'}), 400

    if User.query.filter((User .username == data['username']) | (User .email == data['email'])).first():
        return jsonify({'error': 'Usuário com username ou email já existe'}), 400

    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

def update_user(user_id):
    """
    Atualizar um usuário existente
    ---
    tags:
      - Users
    parameters:
      - in: path
        name: user_id
        type: integer
        required: true
        description: ID do usuário a ser atualizado
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
            email:
              type: string
    responses:
      200:
        description: Usuário atualizado com sucesso
        schema:
          type: object
          properties:
            id:
              type: integer
            username:
              type: string
            email:
              type: string
      404:
        description: Usuário não encontrado
    """
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'Usuário não encontrado'}), 404

    data = request.get_json()
    if not data:
        return jsonify({'error': 'Nenhum dado para atualizar'}), 400

    if 'username' in data:
        user.username = data['username']
    if 'email' in data:
        user.email = data['email']

    db.session.commit()
    return jsonify(user.to_dict()), 200

def delete_user(user_id):
    """
    Excluir um usuário
    ---
    tags:
      - Users
    parameters:
      - in: path
        name: user_id
        type: integer
        required: true
        description: ID do usuário a ser excluído
    responses:
      200:
        description: Usuário excluído com sucesso
      404:
        description: Usuário não encontrado
    """
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'Usuário não encontrado'}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'Usuário excluído com sucesso'}), 200