from flask_restx import Api

api = Api(
    version='1.0',
    title='API Gerenciador de Tarefas',
    description='Uma API para gerenciar usuários e suas tarefas.',
    doc='/swagger/'
)