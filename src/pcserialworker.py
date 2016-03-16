import serial
import time
import multiprocessing

## Change this to match your local settings
SERIAL_PORT = '/dev/ttyS0'
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
    count = 1
    while True:
        if count % 2 == 1:
            sp.write(str.encode("hello"))
        elif count % 2 == 0:
            sp.write(str.encode("world"))
        count += 1
        time.sleep(1)
