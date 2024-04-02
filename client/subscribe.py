import paho.mqtt.client as mqtt
import json

class MqttSubscriber:
    def __init__(self, config_file):
        with open(config_file, 'r') as file:
            config = json.load(file)

        self.broker_address = config['broker_address']
        self.client_id = config['client_id']
        self.topics = config['topics']

        # Connect to MQTT broker
        self.client = mqtt.Client(self.client_id)
        self.client.connect(self.broker_address)

        # Subscribe to topics
        for topic in self.topics:
            self.client.subscribe(topic)

        # Set callback for incoming messages
        self.client.on_message = self.on_message

        # Start MQTT loop
        self.client.loop_forever()

    def on_message(self, client, userdata, message):
        # Process incoming message
        print("Received message on topic: " + message.topic + " with payload: " + message.payload)