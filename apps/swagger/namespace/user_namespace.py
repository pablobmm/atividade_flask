from ..swagger_config import api
from flask_restx import fields

user_ns = api.namespace('users', description='Operações relacionadas a usuários')

user_model = api.model('UserModel', {
    'id': fields.Integer(readonly=True),
    'name': fields.String(required=True, description='Nome do usuário'),
    'email': fields.String(required=True, description='Email do usuário')
})