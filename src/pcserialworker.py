import serial
import time
import multiprocessing

## Change this to match your local settings
SERIAL_PORT = '/dev/ttyUSB0'
SERIAL_BAUDRATE = 115200

input_queue = multiprocessing.Queue()
output_queue = multiprocessing.Queue()

if __name__ == "__main__":
    sp = serial.Serial(
       port=SERIAL_PORT,
       baudrate =SERIAL_BAUDRATE,
       parity=serial.PARITY_NONE,
       stopbits=serial.STOPBITS_ONE,
       bytesize=serial.EIGHTBITS,
       timeout=1
    )
    sp.flushInput()
    count = 1000
    while True:
        sp.write("hello")
        time.sleep(5)
