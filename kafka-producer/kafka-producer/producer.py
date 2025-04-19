from kafka import KafkaProducer
import json
import time
import csv

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

with open('/data/us_accidents.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for i, row in enumerate(reader):
        producer.send('accidents', row)
        time.sleep(0.01)
        if i >= 1000000:
            break

print("an Kafka gesendet")

