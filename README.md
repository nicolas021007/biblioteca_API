# Biblioteca API

API REST para gerenciamento de uma biblioteca, desenvolvida em **Python** com **FastAPI**, seguindo os princípios de **DDD (Domain-Driven Design)**. O armazenamento dos dados é feito **em memória**, sem uso de banco de dados externo.

## 🚀 Tecnologias

- **Python 3.12**
- **FastAPI** — framework para construção da API REST
- **Pydantic** — validação de dados e schemas
- **Uvicorn** — servidor ASGI

## 🏗️ Arquitetura

O projeto segue a arquitetura DDD, separado em camadas:

```
biblioteca_API/
├── api/                  # Rotas (controllers) da API
│   ├── leitores.py
│   └── livros.py
├── domain/                # Entidades de negócio e regras de domínio
│   ├── leitor.py
│   └── livro.py
├── schemas/               # Schemas Pydantic (entrada/saída da API)
│   ├── leitor.py
│   └── livro.py
├── services/              # Casos de uso / lógica de aplicação
│   └── biblioteca_service.py
├── repositories/          # Armazenamento dos dados (em memória)
│   └── memory.py
└── main.py                # Ponto de entrada da aplicação
```

- **domain/**: contém as entidades de negócio (`Leitor`, `Livro`) e suas regras (ex: cálculo de preço final, validações).
- **schemas/**: define o formato dos dados que entram (`*Create`) e saem (`*Out`) da API, usando Pydantic.
- **services/**: orquestra a lógica entre rotas, entidades de domínio e repositório (criação de IDs, validações de aplicação).
- **repositories/**: simula um banco de dados usando dicionários em memória (`DB`).
- **api/**: define os endpoints REST, conectando rotas aos serviços.

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/nicolas021007/biblioteca_API.git
cd biblioteca_API
```

Crie e ative um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

Instale as dependências:

```bash
pip install fastapi uvicorn "pydantic[email]"
```

## ▶️ Executando o projeto

```bash
uvicorn main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`.

A documentação interativa (Swagger UI) pode ser acessada em:

```
http://127.0.0.1:8000/docs
```

## 📚 Endpoints

### Leitores

| Método | Rota          | Descrição                     |
|--------|---------------|--------------------------------|
| POST   | `/leitores`   | Cadastra um novo leitor        |
| GET    | `/leitores`   | Lista todos os leitores        |

**Exemplo de corpo (POST /leitores):**

```json
{
  "nome": "Maria Silva",
  "email": "maria@email.com"
}
```

### Livros

| Método | Rota                          | Descrição                                    |
|--------|-------------------------------|-----------------------------------------------|
| POST   | `/livros`                     | Cadastra um novo livro                        |
| GET    | `/livros`                     | Lista todos os livros                          |
| GET    | `/livros/{codigo}`            | Busca um livro pelo código (UUID)             |
| PUT    | `/livros/{codigo}/preco`      | Atualiza o preço de um livro                  |
| GET    | `/livros/{codigo}/preco_final`| Retorna o livro com o preço final calculado   |

**Exemplo de corpo (POST /livros):**

```json
{
  "titulo": "Dom Casmurro",
  "preco": 30.0,
  "tipo": 2,
  "desconto_percentual": 10
}
```

> `tipo`: `1` = Gratuito · `2` = Pago

## 📐 Regras de negócio

- O **id/código** de leitores e livros é gerado automaticamente pelo sistema usando **UUID**, não sendo informado na criação.
- O **preço** de um livro não pode ser negativo.
- O **desconto percentual** deve estar entre `0` e `100`.
- Um livro do tipo **Gratuito** deve obrigatoriamente ter `preco` igual a `0`. Caso contrário, a API retorna erro `400`.
- O **preço final** de um livro gratuito é sempre `0.0`, independentemente do desconto cadastrado.
- O preço final de um livro pago é calculado como: `preco - (preco * desconto_percentual / 100)`.

## 🧪 Testando a API

A forma mais simples de testar é através do Swagger UI (`/docs`), onde é possível executar cada endpoint diretamente pelo navegador através do botão **"Try it out"**.

## 👤 Autores

Desenvolvido por **Nicolas R. Santos** e **Felipe Figueiredo** como parte dos estudos do curso de **Análise e Desenvolvimento de Sistemas**.