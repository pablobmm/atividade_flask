# Dockerfile

FROM python:3.11-slim

WORKDIR /app

# Adiciona a pasta 'apps' ao PYTHONPATH
ENV PYTHONPATH=/app/apps

COPY requirements.txt .
RUN pip install --user -r requirements.txt

COPY . .

EXPOSE 5002

CMD ["python", "-m", "apps.app"]