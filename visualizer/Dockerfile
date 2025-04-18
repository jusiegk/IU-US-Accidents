FROM python:3.10-slim

RUN pip install pandas matplotlib

WORKDIR /app
COPY . .

CMD ["python", "process_batch.py"]

