 
FROM python:3.10-slim

RUN pip install kafka-python

WORKDIR /app
COPY . .

CMD ["python", "producer.py"]

