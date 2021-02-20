import time
import machine

light = machine.Pin(2, machine.Pin.OUT)

def flash():
    light.value(1)
    time.sleep(1)
    light.value(0)
    time.sleep(1)

def turn(on):
    light.value(on)

