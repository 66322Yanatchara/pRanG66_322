FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install fastapi uvicorn grpcio grpcio-tools

EXPOSE 8000
EXPOSE 50051

CMD ["python", "main.py"]
