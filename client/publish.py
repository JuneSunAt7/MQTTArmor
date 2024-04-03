

import random
import time
import configparser

from paho.mqtt import client as mqtt_client
from logger.printer import *

broker = 'broker.emqx.io'
port = 1883

topics = []
with open('test.conf', 'r') as file:
    for line in file:
        topic = line.strip()
        topics.append(topic)

client_id = f'publish-{random.randint(0, 1000)}'
logger = Logger()

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            logger.succes("Connected to MQTT Broker!")
        else:
            logger.error(f"Failed to connect, return code {rc}\n")

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client, topic):
    msg_count = 1
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        status = result[0]
        if status == 0:
            logger.succes(f"Send `{msg}` to topic `{topic}`")
        else:
            logger.warning(f"Failed to send message to topic {topic}")
        msg_count += 1
        if msg_count > 5:
            break

def run():
    client = connect_mqtt()
    client.loop_start()
    for topic in topics:
        publish(client, topic)
    client.loop_stop()

if __name__ == '__main__':
    run()