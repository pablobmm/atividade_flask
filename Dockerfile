# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# A porta 5000 é a padrão do Flask, mas você pode usar outra
EXPOSE 5000

CMD ["python", "app.py"]