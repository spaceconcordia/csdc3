#!/usr/bin/env python


import time
import serial


ser = serial.Serial(
   port='/dev/ttyS0',
   baudrate = 115200,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
)

counter=0

ser.write('what the actual fuck\n')
time.sleep(1)
counter += 1
