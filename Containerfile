FROM docker.io/library/python:3.12.10-slim-bookworm

WORKDIR /app

COPY . /app

CMD ["python", "main.py"]
