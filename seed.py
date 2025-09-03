from app import app, db
from models.users import User
users_to_add = [
    User(name='Alice', email='alicedasilva123@example.com'),
    User(name='Carla', email='carlapereira@example.com')
]
with app.app_context():
    db.session.query(User).delete() 
    db.session.add_all(users_to_add)
    db.session.commit()
