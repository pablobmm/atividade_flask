from . config import app, db_serv
from .controllers.user_controller import bd_user
from flask import render_template
from flasgger import Swagger

db_serv.init_app(app)
swagger = Swagger(app)
app.register_blueprint(bd_user)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host=app.config['HOST'], port=app.config['PORT'],debug=app.config['DEBUG'])