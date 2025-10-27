FROM python:3.13.9

# criando a pasta
WORKDIR /app

# copiando apenas os requirements
COPY requirements.txt /app/

# instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt

# copiando todo o resto do código
COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]