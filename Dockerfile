FROM python:3.10

# Define o diretório de trabalho no container
WORKDIR /code

# Instala o Poetry
RUN pip install poetry

# Copia apenas os arquivos relevantes para a instalação de dependências
# Isso aproveita a cache das camadas do Docker
COPY pyproject.toml poetry.lock* /code/

# Configura o Poetry para instalar as dependências diretamente no sistema
# Isso é recomendado para imagens Docker, para evitar camadas extras
RUN poetry config virtualenvs.create false

# Instala as dependências do projeto usando o Poetry
RUN poetry install --no-dev

# Copia o restante do código do projeto
COPY ./app /code/app

# Comando para rodar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]
