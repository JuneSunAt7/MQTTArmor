import ssl
import paho.mqtt.client as mqtt

mqtt_broker = "mqtt.example.com"
mqtt_port = 8883  # ssl port
mqtt_username = "username"
mqtt_password = "password"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


def on_message(client, userdata, message):
    print("Received message '" + str(message.payload) + "' on topic '" + message.topic + "'")


# Создаем объект клиента MQTT
client = mqtt.Client()
client.username_pw_set(username=mqtt_username, password=mqtt_password)

# Включаем SSL
client.tls_set(ca_certs="ca.crt", certfile="client.crt", keyfile="client.key", tls_version=ssl.PROTOCOL_TLSv1_2)

client.on_connect = on_connect
client.on_message = on_message

# Подключаемся к брокеру
client.connect(mqtt_broker, mqtt_port, 60)

# Подписываемся на топик
client.subscribe("topic/test")

# Запускаем цикл обработки сообщений
client.loop_forever()
