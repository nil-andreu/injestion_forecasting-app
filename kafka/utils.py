from confluent_kafka import KafkaError, KafkaException

from kafka.env import (
    KAFKA_API_KEY, 
    KAFKA_SECRET_API_KEY, 
    BOOTSTRAP_SERVER, 
    SECURITY_PROTOCOL, 
    SASL_MECHANISM
)


def error_cb(err):
    """ The error callback is used for generic client errors. These
        errors are generally to be considered informational as the client will
        automatically try to recover from all errors, and no extra action
        is typically required by the application.
        For this example however, we terminate the application if the client
        is unable to connect to any broker (_ALL_BROKERS_DOWN) and on
        authentication errors (_AUTHENTICATION). """

    print("Client error: {}".format(err))
    if err.code() == KafkaError._ALL_BROKERS_DOWN or \
       err.code() == KafkaError._AUTHENTICATION:
        # Any exception raised from this callback will be re-raised from the
        # triggering flush() or poll() call.
        raise KafkaException(err)


kafka_config = {
    'sasl.username': KAFKA_API_KEY,
    'sasl.password': KAFKA_SECRET_API_KEY,
    'bootstrap.servers': BOOTSTRAP_SERVER,
    'security.protocol': SECURITY_PROTOCOL,
    'sasl.mechanism': SASL_MECHANISM,
    'error_cb': error_cb,
}
