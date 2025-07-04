
# Gerenciador de Projetos

Um sistema de gerenciamento de projetos desenvolvido com Django e Django REST Framework, permitindo o controle de projetos, atividades e colaboradores.

## 🚀 Funcionalidades

### Projetos
- Criação, visualização, atualização e exclusão de projetos
- Campos disponíveis:
    - Nome
    - Descrição
    - Data de início
    - Data de fim (opcional)

### Atividades
- Gerenciamento completo de atividades vinculadas a projetos
- Campos disponíveis:
    - Nome
    - Descrição
    - Projeto vinculado
    - Responsável (opcional)
    - Status de conclusão

### Colaboradores
- Cadastro e gerenciamento de colaboradores
- Campos disponíveis:
    - Nome
    - Email (único)

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Django 4.2+
- Django REST Framework 3.14+
- SQLite (banco de dados)
- Django CORS Headers

## 📋 Pré-requisitos

- Python 3.x instalado
- pip (gerenciador de pacotes Python)
- Ambiente virtual (recomendado)

## ⚙️ Configuração e Instalação

1. Clone o repositório:
```bash
git clone https://github.com/jeansillva/GerenciadorProjetosPython.git
cd GerenciadorProjetosPython
```

2. Crie e ative um ambiente virtual:
```bash
# Windows
python -m venv venv venv\Scripts\activate

# Linux/Mac
python3 -m venv venv source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute as migrações:
```bash
python manage.py migrate
```

5. Crie um superusuário (admin):
```bash
python manage.py createsuperuser
```

6. Inicie o servidor:
```bash
python manage.py runserver
```

## 💻 Acessando a Aplicação

### Interface Web
- Acesse `http://localhost:8000` para visualizar a interface web
- A página inicial exibe a lista de projetos cadastrados

### Painel Administrativo
- Acesse `http://localhost:8000/admin` para o painel administrativo
- Use as credenciais do superusuário criado anteriormente
- Gerencie projetos, atividades e colaboradores


## 🔑 Autenticação

O sistema utiliza autenticação baseada em Token. Para obter um token:
```bash
curl -X POST http://localhost:8000/api/api-token-auth/
-H "Content-Type: application/json"
-d '{"username": "seu_usuario", "password": "sua_senha"}'
```

Use o token recebido em todas as requisições subsequentes no header:
```bash
Authorization: Token SEU_TOKEN_AQUI
```

## 📝 Endpoints da API

### Projetos
- `GET /api/projetos/` - Lista todos os projetos
- `POST /api/projetos/` - Cria um novo projeto
- `GET /api/projetos/{id}/` - Obtém detalhes de um projeto
- `PUT /api/projetos/{id}/` - Atualiza um projeto
- `DELETE /api/projetos/{id}/` - Remove um projeto

### Atividades
- `GET /api/atividades/` - Lista todas as atividades
- `POST /api/atividades/` - Cria uma nova atividade
- `GET /api/atividades/{id}/` - Obtém detalhes de uma atividade
- `PUT /api/atividades/{id}/` - Atualiza uma atividade
- `DELETE /api/atividades/{id}/` - Remove uma atividade

### Colaboradores
- `GET /api/colaboradores/` - Lista todos os colaboradores
- `POST /api/colaboradores/` - Cadastra um novo colaborador
- `GET /api/colaboradores/{id}/` - Obtém detalhes de um colaborador
- `PUT /api/colaboradores/{id}/` - Atualiza um colaborador
- `DELETE /api/colaboradores/{id}/` - Remove um colaborador

## 📦 Exemplos de Uso

### Criando um Projeto
```bash
curl -X POST http://localhost:8000/api/projetos/
-H "Authorization: Token seu_token_aqui"
-H "Content-Type: application/json"
-d '{ "nome": "Novo Projeto", "descricao": "Descrição do projeto", "data_inicio": "2024-07-03", "data_fim": "2024-12-31" }'
```

### Criando uma Atividade
```bash
bash curl -X POST [http://localhost:8000/api/atividades/](http://localhost:8000/api/atividades/)
-H "Authorization: Token seu_token_aqui"
-H "Content-Type: application/json"
-d '{ "nome": "Nova Atividade", "descricao": "Descrição da atividade", "projeto": 1, "responsavel": 1, "concluida": false }'
```

### Cadastrando um Colaborador
```bash
curl -X POST [http://localhost:8000/api/colaboradores/](http://localhost:8000/api/colaboradores/)
-H "Authorization: Token seu_token_aqui"
-H "Content-Type: application/json"
-d '{ "nome": "João Silva", "email": "joao@example.com" }'
```