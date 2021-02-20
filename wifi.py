import network
import config

def do_connect():
    # Set to station mode for connecting to network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to network...')
        sta_if.active(True)
        sta_if.connect(config.SSID, config.PASSWORD)

        # Wait until connected
        while not sta_if.isconnected():
            pass
        print('Network connected!')