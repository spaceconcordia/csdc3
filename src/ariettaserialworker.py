import serial
import time
import multiprocessing

## Change this to match your local settings
SERIAL_PORT = '/dev/ttyUSB0'
SERIAL_BAUDRATE = 115200

if __name__ == '__main__':
	## start the serial worker in background (as a deamon)
    sp = serial.Serial(SERIAL_PORT, SERIAL_BAUDRATE, timeout=1)
    sp.flushInput()
    while True:
    # look for incoming tornado request
        if (sp.inWaiting() > 0):
            data = sp.read()
            print("reading from serial: " + data.decode())
