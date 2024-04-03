
import random

from paho.mqtt import client as mqtt_client
from logger.printer import *
from logger.journal import *

broker = 'broker.emqx.io'
port = 1883
topics = []

with open('test.conf', 'r') as file:
    for line in file:
        topic = line.strip()
        topics.append(topic)

# Generate a Client ID with the subscribe prefix.
client_id = f'subscribe-{random.randint(0, 100)}'

logger = Logger()

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            logger.succes("Connected to MQTT Broker!")
        else:
            logger.error("Failed to connect, return code %d", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        logger.succes(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        write_log(str(msg.payload))
    for topic in topics:
        client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()

