from apps.config import db_serv


class User(db_serv.Model):
    __tablename__ = 'users'

    id = db_serv.Column(db_serv.Integer, primary_key=True)
    nome = db_serv.Column(db_serv.String(80), nullable=False)
    email = db_serv.Column(db_serv.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.nome}>'

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email
        }
    

def criar_user(data):
    """Cadastra um novo usuário no banco de dados."""
    try:
        new_user = User(nome=data['nome'], email=data['email'])
        db_serv.session.add(new_user)
        db_serv.session.commit()
        return new_user.to_dict(), None
    except Exception as e:
        db_serv.session.rollback()
        return None, str(e)

def listar_users():
    """Retorna todos os usuários do banco de dados."""
    users = User.query.all()
    return [user.to_dict() for user in users]

def listar_user_id(user_id):
    """Busca um usuário pelo ID."""
    user = User.query.get(user_id)
    if user:
        return user.to_dict()
    return None

def alterar_user(user_id, data):
    """Altera os dados de um usuário existente."""
    user = User.query.get(user_id)
    if not user:
        return None, "Usuário não encontrado"
        
    if 'nome' in data:
        user.nome = data['nome']
    if 'email' in data:
        user.email = data['email']
    
    db_serv.session.commit()
    return user.to_dict(), None

def deletar_user(user_id):
    """Deleta um usuário pelo ID."""
    user = User.query.get(user_id)
    if not user:
        return False, "Usuário não encontrado"
        
    db_serv.session.delete(user)
    db_serv.session.commit()
    return True, None