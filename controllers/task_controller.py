from models.task import db 
from models.users import db






from flask import Flask, request, jsonify

app = Flask(__name__)

users = []
current_id = 1

@app.route('/users', methods=['POST'])
def criarUsuario():
    global current_id
    dados = request.get_json()
    nome = dados.get('nome')
    email = dados.get('email')

    if not nome or not email:
        return jsonify({"erro": "O campo nome e email devem ser preenchidos"}), 400

    novo_usuario = {
        'id': current_id,
        'nome': nome,
        'email': email
    }

    users.append(novo_usuario)
    current_id += 1

    return jsonify(novo_usuario), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    for user in users:
        if user['id'] == user_id:
            return jsonify(user), 200
    return jsonify({"erro": "Usuário não encontrado"}), 404

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    dados = request.get_json()
    nome = dados.get('nome')
    email = dados.get('email')

    for user in users:
        if user['id'] == user_id:
            if nome:
                user['nome'] = nome
            if email:
                user['email'] = email
            return jsonify(user), 200

    return jsonify({"erro": "Usuário não encontrado"}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def deletar_usuario(user_id):
    for i, user in enumerate(users):
        if user['id'] == user_id:
            users.pop(i)
            return jsonify({"message": "Usuário excluído com sucesso"}), 200
    return jsonify({"erro": "Usuário não encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)

