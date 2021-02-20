from umqtt.robust import MQTTClient
import time
import config

def mqtt_callback(topic, msg):
    print('topic: {}'.format(topic))
    print('msg: {}'.format(msg))

def connect(callback=mqtt_callback):
    print('try to connect')
    global client
    client = MQTTClient(config.CLIENT_ID, config.MQTTSERVER, config.MQTTPORT, config.MQTTUSER, config.MQTTPSW)
    client.set_callback(callback)
    client.connect()
    time.sleep(10)
    print('connect!')

def subscribe(topic):
    client.subscribe(topic)

def check():
    global client
    client.check_msg()