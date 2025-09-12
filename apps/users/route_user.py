from flask import Blueprint, request, jsonify
import users.model_user as modUser

bd_user = Blueprint('User', __name__)


@bd_user.route("/user", methods=["POST"])
def criar_user():
    """
    Rota para adicionar um novo usuário.
    Recebe os dados via JSON, chama a função de criação
    e retorna o novo usuário ou uma mensagem de erro.
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
    Rota para listar todos os usuários.
    Chama a função que busca todos os usuários no banco
    e retorna uma lista em formato JSON.
    """
    users = modUser.listar_users()
    return jsonify(users), 200

@bd_user.route("/user/<int:id>", methods=["GET"])
def lista_user_id(id):
    """
    Rota para buscar um único usuário por ID.
    Chama a função que busca no banco, se encontrado,
    retorna o usuário.
    """
    user = modUser.listar_user_id(id)
    if user:
        return jsonify(user), 200
    return jsonify({'message': 'Usuário não encontrado'}), 404


@bd_user.route("/user/<int:id>", methods=["PUT"])
def alterar_user(id):
    """
    Rota para atualizar os dados de um usuário por ID.
    Recebe os novos dados, chama a função de atualização
    e retorna o usuário com os dados alterados.
    """
    data = request.json
    updated_user, error = modUser.alterar_user(id, data)

    if error:
        return jsonify({'message': 'Erro ao atualizar', 'error': error}), 404
    
    return jsonify(updated_user), 200

@bd_user.route("/user/<int:id>", methods=["DELETE"])
def deletra_user(id):
    """
    Rota para deletar um usuário por ID.
    Chama a função de deleção e retorna uma mensagem
    de sucesso ou erro.
    """
    success, error = modUser.deletar_user(id)
    if not success:
        return jsonify({'message': 'Erro ao deletar', 'error': error}), 404
        
    return jsonify({'message': 'Usuário excluído com sucesso'}), 200