# Desafio Backend do ITAU

Esta API REST foi desenvolvida para registrar transações e apresentar estatísticas sobre as transações realizadas nos últimos 60 segundos.

## Funcionalidades

- **POST /api/v1/transacao/**: Registra uma nova transação.
- **DELETE /api/v1/transacao/**: Remove todas as transações cadastradas.
- **GET /api/v1/estatistica/**: Retorna estatísticas das transações dos últimos 60 segundos (contagem, soma, média, mínimo, máximo).

## Requisitos

- Python 3.13
- Django 5.2
- djangorestframework 3.15.2

## Instalação e Execução

### Executando Localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/strvictor/DESAFIO-ITAU-BACKEND.git
   cd desafio-itau-backend
   ```

2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv .venv
   # No PowerShell do Windows:
   .venv\Scripts\Activate.ps1
   # Ou, no CMD:
   .venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute as migrações:
   ```bash
   python manage.py migrate
   ```

5. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

### Executando com Docker

1. Construa a imagem Docker:
   ```bash
   docker build -t desafio-itau:latest .
   ```

2. Inicie o container mapeando a porta 8000:
   ```bash
   docker run -p 8000:8000 desafio-itau:latest
   ```

## Endpoints da API

- **POST /api/v1/transacao/**  
  Registra uma nova transação.  
  Parâmetros esperados no corpo da requisição:
  - `dataHora`: Data e hora da transação (formato datetime).
  - `valor`: Valor da transação.

- **DELETE /api/v1/transacao/**  
  Remove todas as transações registradas.

- **GET /api/v1/estatistica/**  
  Retorna as estatísticas das transações dos últimos 60 segundos, contendo:
  - `count`: Número total de transações.
  - `sum`: Soma total dos valores.
  - `avg`: Média dos valores.
  - `min`: Menor valor registrado.
  - `max`: Maior valor registrado.

## Link do Repositório

- [GitHub - Desafio Backend do ITAU](https://github.com/feltex/desafio-itau-backend)