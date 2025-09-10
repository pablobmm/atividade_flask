@app.route('/tasks', methods=['GET'])
def list_tasks_route():
    """
    Lista todas as tarefas
    Este endpoint retorna uma lista de todas as tarefas cadastradas.
    ---
    tags:
      - Tasks
    responses:
      200:
        description: Uma lista de tarefas.
    """
    return TaskController.list_tasks()

@app.route('/tasks', methods=['POST'])
def create_task_route():
    """
    Cria uma nova tarefa
    Este endpoint cria uma nova tarefa com base nos dados fornecidos.
    ---
    tags:
      - Tasks
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - title
            - user_id
          properties:
            title:
              type: string
            description:
              type: string
            user_id:
              type: integer
    responses:
      201:
        description: Tarefa criada com sucesso.
    """
    return TaskController.create_task()

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task_route(task_id):
    """
    Atualiza uma tarefa existente
    Este endpoint atualiza os dados de uma tarefa específica.
    ---
    tags:
      - Tasks
    parameters:
      - name: task_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
            description:
              type: string
            status:
              type: string
    responses:
      200:
        description: Tarefa atualizada com sucesso.
      404:
        description: Tarefa não encontrada.
    """
    return TaskController.update_task(task_id)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task_route(task_id):
    """
    Exclui uma tarefa
    Este endpoint remove uma tarefa do banco de dados.
    ---
    tags:
      - Tasks
    parameters:
      - name: task_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Tarefa excluída com sucesso.
      404:
        description: Tarefa não encontrada.
    """
    return TaskController.delete_task(task_id)

if __name__ == '__main__':
    app.run(debug=True)