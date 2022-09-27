import json
import time
from confluent_kafka import Producer, KafkaError, KafkaException

from forecasting.kafka_forecasting.utils import kafka_config


# Check the following Documentation: https://github.com/confluentinc/confluent-kafka-python/blob/master/examples/confluent_cloud.py
producer = Producer({
    **kafka_config,
    'partitioner': 'consistent_random'  # in the case we would have more than one partition
})


def get_topics():
    topics = producer.list_topics()
    print(topics)
    return topics


def delivery_callback(err, msg):
    """ 
    Called once for each message produced to indicate delivery result.
    Triggered by poll() or flush(). 
    """

    if err is not None:
        print('Message delivery failed: {}'.format(err))

    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


def produce_kafka_message(data):
    message = json.dumps(data)

    producer.produce(
        topic='financials', 
        value=message.encode('utf-8'), 
        callback=delivery_callback
    )

    # Trigger any available delivery report callbacks from previous produce() calls
    producer.poll(0)
    time.sleep(1)


if __name__ == '__main__':
    data = {"side":"SELL","quantity":212,"symbol":"ZJZZT","price":551,"account":"ABC123","userid":"User_4"}
    produce_kafka_message(data)
