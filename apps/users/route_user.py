from flask_restx import Resource
from .route_user import user_ns, user_model
from ..database import db
from .model_user import User

@user_ns.route('/')
class UserList(Resource):
    @user_ns.marshal_list_with(user_model)
    def get(self):
        """Lista todos os usuários"""
        return User.query.all()

    @user_ns.expect(user_model)
    @user_ns.marshal_with(user_model, code=201)
    def post(self):
        """Cria um novo usuário"""
        data = user_ns.payload
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return new_user, 201