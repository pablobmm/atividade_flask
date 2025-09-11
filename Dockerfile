FROM python:3.11-slim

WORKDIR /projeto

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia a pasta 'apps', 'instance' e os arquivos da raiz
COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]