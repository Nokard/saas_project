# Imagem base do Python 3.13
FROM python:3.13-slim

# Diretório de trabalho
WORKDIR /app

# Poetry install
ENV POETRY_VERSION=2.2.1
RUN pip install "poetry==${POETRY_VERSION}"

#Copiar arquivos de dependência
COPY pyproject.toml poetry.lock* ./

#Configurar Poetry para não criar ambiente virtual (usar o do container)
ENV POETRY_VIRTUALENVS_CREATE=false

# Instalar dependências (sem dev)
RUN poetry install --no-root --no-interaction --no-ansi
# Copiar o código da aplicação
COPY . .

# Porta exposta
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "run.py"]