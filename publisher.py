from umqtt.robust import MQTTClient
import time

client = MQTTClient(CLIENT_ID, SERVER)
client.connect()


while True:
    client.publish(TOPIC, 'helloworld')
    time.sleep(1)