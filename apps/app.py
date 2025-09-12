from . config import app, db_serv
from .users.route_user import bd_user

db_serv.init_app(app)

app.register_blueprint(bd_user)



if __name__ == "__main__":
    app.run(host=app.config['HOST'], port=app.config['PORT'],debug=app.config['DEBUG'])