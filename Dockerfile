FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --user -r requirements.txt

COPY apps/ . .

EXPOSE 5002

CMD python -m apps.app