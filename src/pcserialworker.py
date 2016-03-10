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
    while True:
        if (sp.inWaiting() > 0):
            data = self.read()
            print("reading data sent from board: " + data)
        time.sleep(5)
