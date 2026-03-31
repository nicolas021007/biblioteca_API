

# 📚 Biblioteca API


API REST para gerenciamento de uma biblioteca, desenvolvida em **Python 3.12** com **FastAPI**, seguindo a arquitetura **Domain-Driven Design (DDD)**. Permite cadastrar e listar **leitores** e **livros**, com regras de negócio aplicadas diretamente no domínio.

---

## 📋 Sumário

- [Sobre o Projeto](#sobre-o-projeto)
- [Tecnologias](#tecnologias)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Regras de Negócio](#regras-de-negócio)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Endpoints](#endpoints)

---

## 💡 Sobre o Projeto

A **Biblioteca API** é uma API RESTful que gerencia o cadastro de leitores e livros. O projeto aplica os conceitos de DDD separando claramente as camadas de **domínio**, **serviços**, **repositórios**, **schemas** e **rotas**, garantindo organização e facilidade de manutenção.

---

## 🛠 Tecnologias

| Tecnologia | Descrição |
|---|---|
| [Python 3.12](https://www.python.org/) | Linguagem principal |
| [FastAPI](https://fastapi.tiangolo.com/) | Framework web para criação da API |
| [Pydantic](https://docs.pydantic.dev/) | Validação e serialização de dados |
| [Uvicorn](https://www.uvicorn.org/) | Servidor ASGI para rodar a aplicação |

---

## 🗂 Estrutura do Projeto

```
BIBLIOTECA_API/
│
├── main.py                          # Ponto de entrada — instancia o FastAPI e registra os routers
│
├── domain/                          # Camada de Domínio (entidades e regras de negócio)
│   ├── __init__.py
│   ├── livro.py                     # Entidade Livro com validações e cálculo de preço final
│   └── leitor.py                    # Value Object Leitor (dataclass imutável)
│
├── schemas/                         # Schemas Pydantic (contratos de entrada e saída da API)
│   ├── __init__.py
│   ├── livro.py                     # LivroCreate e LivroOut
│   └── leitor.py                    # LeitorCreate e LeitorOut
│
├── repositories/                    # Camada de Repositório (persistência em memória)
│   ├── __init__.py
│   └── memory.py                    # Classe DB — armazena leitores e livros em dicionários
│
├── services/                        # Camada de Serviços (casos de uso / lógica de aplicação)
│   ├── __init__.py
│   └── biblioteca_service.py        # Funções: criar/listar leitores, criar/listar/buscar/alterar livros
│
├── api/
│   └── router/
│       ├── leitores.py              # Rotas de Leitores
│       └── livros.py                # Rotas de Livros
│
├── .venv/                           # Ambiente virtual Python
├── .gitignore
└── README.md
```

---

## 📐 Regras de Negócio

### Livro

A entidade `Livro` aplica as seguintes validações ao ser criada:

- **Preço** não pode ser negativo.
- **Desconto percentual** deve estar entre `0` e `100`.
- **Tipo** aceita apenas dois valores:
  - `1` → Livro **gratuito** (preço final sempre `0.0`)
  - `2` → Livro **pago** (preço final calculado com desconto)

**Cálculo do preço final:**
```
preco_final = preco - (preco * desconto_percentual / 100)
```

### Leitor

O `Leitor` é um **Value Object** imutável (`dataclass frozen=True`) com os campos:
- `id` (int)
- `nome` (str)
- `email` (str validado via `EmailStr` do Pydantic)

---

## ⚙️ Instalação

### Pré-requisitos

- Python 3.12+
- pip

### Passos

**1. Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/Biblioteca_API.git
cd python_aula
```

**2. Crie e ative o ambiente virtual:**
```bash
python -m venv .venv

# Linux/macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

**3. Instale as dependências:**
```bash
pip install fastapi uvicorn pydantic[email]
```

**4. Inicie o servidor:**
```bash
uvicorn main:app --reload
```

A API estará disponível em: `http://localhost:8000`

---

## 🚀 Como Usar

### Documentação interativa

Com o servidor rodando, acesse:

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

---

## 🔗 Endpoints

### Geral

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/` | Verifica se a API está funcionando |

### Leitores

| Método | Rota | Descrição |
|---|---|---|
| `POST` | `/leitores` | Cadastra um novo leitor |
| `GET` | `/leitores` | Lista todos os leitores |

**Exemplo de payload — criar leitor:**
```json
{
  "id": 1,
  "nome": "João Silva",
  "email": "joao@email.com"
}
```

### Livros

| Método | Rota | Descrição |
|---|---|---|
| `POST` | `/livros` | Cadastra um novo livro |
| `GET` | `/livros` | Lista todos os livros |
| `GET` | `/livros/{codigo}` | Busca um livro pelo código |
| `PATCH` | `/livros/{codigo}/preco` | Altera o preço de um livro |

**Exemplo de payload — criar livro:**
```json
{
  "codigo": 101,
  "titulo": "Clean Code",
  "preco": 89.90,
  "tipo": 2,
  "desconto_percentual": 10
}
```

## 👨‍💻 Desenvolvedores



Este projeto foi desenvolvido pelos alunos:
 
- **Nicolas R. Santos**
- **Felipe Gonçalves**
 
---