FROM python:3.10

RUN pip install --upgrade pip
RUN pip install confluent-kafka \
    python-dotenv

WORKDIR /app
COPY * /app/

CMD ["python3", "kafka_consumer.py"]
