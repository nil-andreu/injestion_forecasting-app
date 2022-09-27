import os
from dotenv import load_dotenv

# We load the environmental 
load_dotenv()

KAFKA_API_KEY = os.getenv("KAFKA_API_KEY")
KAFKA_SECRET_API_KEY = os.getenv("KAFKA_SECRET_API_KEY")
KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID")
KAFKA_PRODUCER_ID = os.getenv("KAFKA_PRODUCER_ID")
KAFKA_CONSUMER_ID = os.getenv("KAFKA_CONSUMER_ID")
BOOTSTRAP_SERVER = os.getenv("BOOTSTRAP_SERVER")
SECURITY_PROTOCOL = os.getenv("SECURITY_PROTOCOL")
SASL_MECHANISM = os.getenv("SASL_MECHANISM")
