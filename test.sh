#!/bin/bash
ampy --port /dev/tty.SLAB_USBtoUART put $1
ampy --port /dev/tty.SLAB_USBtoUART reset
picocom -b 115200 /dev/tty.SLAB_USBtoUART