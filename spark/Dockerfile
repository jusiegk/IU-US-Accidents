FROM bitnami/spark:latest

USER root

RUN install_packages python3-pip
RUN pip install pandas matplotlib kafka-python pyspark psycopg2-binary

COPY . /opt/spark-apps
WORKDIR /opt/spark-apps

CMD ["spark-submit", "process_batch.py"]


