# Use a imagem base do Python
FROM python:3.11.3

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo de requisitos para o contêiner
COPY requirements.txt /app/

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do projeto para o contêiner
COPY . /app/

# Define as variáveis de ambiente do Django
ENV DJANGO_SETTINGS_MODULE=proposta.settings

# Expõe a porta em que o aplicativo estará rodando
EXPOSE 8000

# Comandos para executar o aplicativo
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
