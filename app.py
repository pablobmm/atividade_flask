from controllers.task_controller import TaskController
from models import db
from flask import redirect,request,render_template,Flask
import os


task_controller = TaskController()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db.init_app(app)

with app.app_context():
    db.create_all()



class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
    

@app.route('/tasks/new', methods=['GET', 'POST'])
def create_task():
    if request.method == 'POST':
        return redirect('/tasks') 
    else:
        return render_template('create_task.html')
    


# Rota para listar tarefas
@app.route('/tasks', methods=['GET'])
def list_tasks():
    return task_controller.list_tasks()

# Rota para criar tarefa (GET mostra formulário, POST cria)
@app.route('/tasks/new', methods=['GET', 'POST'])
def create_task():
    if request.method == 'POST':
        return task_controller.create_task()
    else:
        return task_controller.create_task_get()  # Caso você tenha método separado para mostrar o formulário

# Rota para atualizar status da tarefa
@app.route('/tasks/update/<int:task_id>', methods=['POST'])
def update_task_status(task_id):
    return task_controller.update_task_status(task_id)

# Rota para deletar tarefa
@app.route('/tasks/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    return task_controller.delete_task(task_id)

if __name__ == '__main__':
    app.run(debug=True)