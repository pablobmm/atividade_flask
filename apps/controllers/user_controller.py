from flask import Blueprint, request, jsonify
from ..models import model_user as modUser

bd_user = Blueprint('User', __name__)


@bd_user.route("/user", methods=["POST"])
def criar_user():
    """
    Cria um novo usuário.
    Esta rota adiciona um novo usuário ao banco de dados.
    ---
    tags:
      - Usuários
    parameters:
      - in: body
        name: body
        required: true
        schema:
          id: User
          required:
            - nome
            - email
          properties:
            nome:
              type: string
              description: O nome do usuário.
            email:
              type: string
              description: O e-mail do usuário.
    responses:
      201:
        description: Usuário criado com sucesso.
      400:
        description: Dados inválidos (nome ou e-mail faltando).
    """
    data = request.json
    if not data or 'nome' not in data or 'email' not in data:
        return jsonify({'message': 'Dados de usuário inválidos'}), 400

    new_user, error = modUser.criar_user(data)
    if error:
        return jsonify({'message': 'Erro ao criar usuário', 'error': error}), 500

    return jsonify(new_user), 201

@bd_user.route("/user", methods=["GET"])
def listar_user():
    """
    Lista todos os usuários.
    Retorna uma lista com todos os usuários cadastrados no banco de dados.
    ---
    tags:
      - Usuários
    responses:
      200:
        description: Uma lista de usuários.
        schema:
          type: array
          items:
            $ref: '#/definitions/User'
    """
    users = modUser.listar_users()
    return jsonify(users), 200

@bd_user.route("/user/<int:id>", methods=["GET"])
def lista_user_id(id):
    """
    Busca um usuário por ID.
    Retorna os dados de um usuário específico a partir do seu ID.
    ---
    tags:
      - Usuários
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do usuário a ser buscado.
    responses:
      200:
        description: Dados do usuário encontrado.
        schema:
          $ref: '#/definitions/User'
      404:
        description: Usuário não encontrado.
    """
    user = modUser.listar_user_id(id)
    if user:
        return jsonify(user), 200
    return jsonify({'message': 'Usuário não encontrado'}), 404


@bd_user.route("/user/<int:id>", methods=["PUT"])
def alterar_user(id):
    """
    Atualiza um usuário existente.
    Altera os dados (nome e/ou email) de um usuário a partir do seu ID.
    ---
    tags:
      - Usuários
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do usuário a ser atualizado.
      - in: body
        name: body
        required: true
        schema:
          properties:
            nome:
              type: string
              description: O novo nome do usuário.
            email:
              type: string
              description: O novo e-mail do usuário.
    responses:
      200:
        description: Usuário atualizado com sucesso.
      404:
        description: Usuário não encontrado.
    """
    data = request.json
    updated_user, error = modUser.alterar_user(id, data)

    if error:
        return jsonify({'message': 'Erro ao atualizar', 'error': error}), 404
    
    return jsonify(updated_user), 200

@bd_user.route("/user/<int:id>", methods=["DELETE"])
def deletra_user(id):
    """
    Deleta um usuário.
    Remove um usuário do banco de dados a partir do seu ID.
    ---
    tags:
      - Usuários
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do usuário a ser deletado.
    responses:
      200:
        description: Usuário deletado com sucesso.
      404:
        description: Usuário não encontrado.
    """
    success, error = modUser.deletar_user(id)
    if not success:
        return jsonify({'message': 'Erro ao deletar', 'error': error}), 404
        
    return jsonify({'message': 'Usuário excluído com sucesso'}), 200