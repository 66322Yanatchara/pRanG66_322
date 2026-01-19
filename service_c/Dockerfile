FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install fastapi uvicorn

EXPOSE 8002

CMD ["python", "main.py"]
