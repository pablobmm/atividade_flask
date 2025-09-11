from apps.app import create_app
from apps.database import db
from apps.users.model_user import User

# Cria a aplicação para ter o contexto
app = create_app()

with app.app_context():
    # Apaga tudo para um começo limpo (cuidado em produção!)
    db.drop_all()
    db.create_all()

    # Cria usuários de exemplo
    user1 = User(name='Carlos', email='carlos@email.com')
    user2 = User(name='Daniela', email='daniela@email.com')

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    print("Banco de dados inicializado com usuários de exemplo!")