from controllers.task_controller import TaskController
from models import db
from flask import redirect, request, render_template, Flask
import os


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)


with app.app_context():
    db.create_all()


task_controller = TaskController()


@app.route('/tasks', methods=['GET'])
def list_tasks():
    return task_controller.list_tasks()


@app.route('/tasks/new', methods=['GET', 'POST'])
def create_task():

    return task_controller.create_task()


@app.route('/tasks/update/<int:task_id>', methods=['POST'])
def update_task_status(task_id):
    return task_controller.update_task_status(task_id)


@app.route('/tasks/delete/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    return task_controller.delete_task(task_id)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)