# controllers/task_controller.py

from flask import render_template, request, redirect, url_for
from models.task import Task
from models.users import User
from models.task import db

class TaskController:

    @staticmethod
    def list_tasks():
        tasks = Task.query.all()
        return render_template('tasks.html', tasks=tasks)

    @staticmethod
    def create_task():
        if request.method == 'POST':
            
            title = request.form.get('title')
            description = request.form.get('description')
            user_id = request.form.get('user_id')

            
            new_task = Task(title=title, description=description, user_id=user_id)
            db.session.add(new_task)
            db.session.commit()

            return redirect(url_for('list_tasks'))
        else: 
            users = User.query.all()
            return render_template('create_task.html', users=users)

    @staticmethod
    def update_task_status(task_id):
        
        task = Task.query.get(task_id)
        if task:
            task.status = 'Concluído' if task.status == 'Pendente' else 'Pendente'
            db.session.commit()
        return redirect(url_for('list_tasks'))

    @staticmethod
    def delete_task(task_id):
        
        task = Task.query.get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
        return redirect(url_for('list_tasks'))