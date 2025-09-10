from flask import Flask
from flask_migrate import Migrate
from flasgger import Swagger
from config import Config
from models import db  
from controllers import task_controller, user_controller

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)
swagger = Swagger(app)

# Rotas Tasks
app.add_url_rule('/tasks', 'list_tasks', task_controller.list_tasks, methods=['GET'])
app.add_url_rule('/tasks', 'create_task', task_controller.create_task, methods=['POST'])
app.add_url_rule('/tasks/<int:task_id>', 'update_task', task_controller.update_task, methods=['PUT'])
app.add_url_rule('/tasks/<int:task_id>', 'delete_task', task_controller.delete_task, methods=['DELETE'])

# Rotas Users
app.add_url_rule('/users', 'list_users', user_controller.list_users, methods=['GET'])
app.add_url_rule('/users', 'create_user', user_controller.create_user, methods=['POST'])
app.add_url_rule('/users/<int:user_id>', 'update_user', user_controller.update_user, methods=['PUT'])
app.add_url_rule('/users/<int:user_id>', 'delete_user', user_controller.delete_user, methods=['DELETE'])

if __name__ == '__main__':
    app.run(debug=True)