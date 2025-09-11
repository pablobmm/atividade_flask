from config import app, db_serv
from users.model_user import User

with app.app_context():
    db_serv.create_all()