# Construção de uma API Simples com Flask  

## 📌 Descrição do Projeto  
Este projeto consiste no desenvolvimento de uma **API RESTful simples** utilizando o framework **Flask**.  
O objetivo é gerenciar usuários, permitindo realizar as quatro operações fundamentais de **CRUD** (Create, Read, Update e Delete).  

Os dados dos usuários são armazenados em memória, em uma **lista de dicionários**, simulando um banco de dados básico.  

---

## ⚙️ Funcionalidades  

A API implementa os seguintes endpoints:  

- **POST `/users`** → Cria um novo usuário  
  - Recebe `nome` e `email` no corpo da requisição (JSON).  
  - Gera automaticamente um `id` único para cada usuário.  
  - Retorna o usuário criado com status **201 Created**.  

- **GET `/users`** → Lista todos os usuários  
  - Retorna uma lista com todos os usuários cadastrados.  
  - Caso não existam usuários, retorna uma lista vazia `[]`.  
  - Status **200 OK**.  

- **GET `/users/<int:user_id>`** → Busca um usuário pelo ID  
  - Retorna os dados do usuário se encontrado (status **200 OK**).  
  - Caso não exista, retorna mensagem de erro com status **404 Not Found**.  

- **PUT `/users/<int:user_id>`** → Atualiza um usuário existente  
  - Recebe `nome` e/ou `email` no corpo da requisição (JSON).  
  - Atualiza os dados do usuário, retornando o registro atualizado (status **200 OK**).  
  - Caso o usuário não seja encontrado, retorna mensagem de erro com status **404 Not Found**.  

- **DELETE `/users/<int:user_id>`** → Remove um usuário  
  - Exclui o usuário da lista.  
  - Retorna mensagem de sucesso (status **200 OK**).  
  - Caso o usuário não seja encontrado, retorna mensagem de erro com status **404 Not Found**.  

---

## 🛠️ Requisitos Técnicos  

1. **Estrutura de Dados**: Lista global de dicionários contendo os campos `id`, `nome` e `email`.  
2. **Geração de ID**: Controle feito por um contador (`current_id`) que é incrementado a cada novo usuário criado.  
3. **Flask**: Toda a aplicação deve estar contida em um único arquivo `app.py`.  
4. **Formato de Dados**: Todas as requisições e respostas devem estar no formato **JSON**, utilizando `jsonify` do Flask.  
5. **Tratamento de Erros**: A API deve retornar os códigos de status corretos para cada caso (200, 201, 404).  

---

## ▶️ Como Executar o Projeto  

1. Clone o repositório:  
   ```bash
   git clone <[URL_DO_REPOSITORIO](https://github.com/pablobmm/atividade_flask.git)>
   cd <NOME_DA_PASTA>
