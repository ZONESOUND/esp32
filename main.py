import urequests
import time
import machine

import config
import wifi
import lighting
import subscriber

def get_data():
    print('Getting data...')
    try:
        res = urequests.get(config.URL)
        print('Response: {}'.format(res.text))
        print(res.json()['light'])
        lighting.turn(res.json()['light'])
    except Exception as e:
        print(e)
    
def send_data(data):
    print('Sending data...')
    res = urequests.put(config.URL, json=data)
    print('Response: {}'.format(res.text))
    #flash_led() # Indicate successful data transmission

def turn_light(topic, msg):
    print('turn_light '+topic.decode('UTF-8'))
    if (topic == config.TOPIC_light):
        print('light:'+msg.decode('UTF-8'))
        lighting.turn(int(msg.decode('UTF-8')))

def main():
    print('main!')
    # Connect to network
    wifi.do_connect()
    subscriber.connect(turn_light)
    subscriber.subscribe(config.TOPIC_light)
    lighting.flash()
    
    while True:
        #get_data()
        #print('get...')
        subscriber.check()
        time.sleep(0.5)

main()
