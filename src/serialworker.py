import serial
import time
import multiprocessing

## Change this to match your local settings
SERIAL_PORT = '/dev/ttyUSB0'
SERIAL_BAUDRATE = 115200

input_queue = multiprocessing.Queue()
output_queue = multiprocessing.Queue()

RAM_INTENS_PROC = 0x00
CPU_INTENS_PROC = 0x01
DISK_PARTITION = 0x02
GET_TIME = 0x03
SET_TIME = 0x04
GET_LOGGED_DATA = 0x05
DEL_LOGGED_DATA = 0x06
DEPLOY_ANT = 0x07
PAYLOAD_JOB = 0x08
PAYLOAD_TELEMETRY = 0x09
POWER_TELEMETRY = 0x0A
HEALTH_MONITORING = 0x0B

# to think about
# UPDATE_BIN
# ROLL_BACK_BIN
# TIME_TAG_CMD

class SerialRequestProcess(multiprocessing.Process):
    def __init__(self, input_queue, output_queue):
        multiprocessing.Process.__init__(self)
        self.input_queue = input_queue
        self.output_queue = output_queue
        self.sp = serial.Serial(SERIAL_PORT, SERIAL_BAUDRATE, timeout=1) #1?

    def close(self):
        self.sp.close()

    def writeSerial(self, data):
        self.sp.write(data)
        # time.sleep(1)

    def run(self):
        self.sp.flushInput()
        while True:
            if (self.sp.inWaiting() > 0):
                data = self.read()
                print("reading from serial: " + data)
                # send it back to tornado
                self.output_queue.put(data)

class SerialSysStatusProcess(multiprocessing.Process):
    # will write to serial every 3 secs
    # RAM_USAGE = 0x00
    # CPU_AVG_LOAD = 0x01
    # CPU_UTIL = 0x02
    pass

if __name__ == "__main__":
    sp = serial.Serial(SERIAL_PORT, SERIAL_BAUDRATE, timeout=1)
    sp.flushInput()
        while True:
            if (sp.inWaiting() > 0):
                data = self.read()
                print("reading from serial: " + data)
