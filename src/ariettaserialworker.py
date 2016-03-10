import serial
import time
import multiprocessing

## Change this to match your local settings
SERIAL_PORT = '/dev/ttyS0'
SERIAL_BAUDRATE = 115200

    def writeSerial(self, data):
        self.sp.write(data+"\n")
        # time.sleep(1)

    def readSerial(self):
        return self.sp.readline().replace("\n", "")

    def run(self):
        self.sp.flushInput()
        while True:
            # look for incoming serial data
            if (self.sp.inWaiting() > 0):
                data = self.readSerial()
                print("reading from serial: " + data)
                # send it back as double the serial device
                self.writeSerial(data+data)

if __name__ == '__main__':
	## start the serial worker in background (as a deamon)
    sp = serial.Serial(SERIAL_PORT, SERIAL_BAUDRATE, timeout=1)
    sp.flushInput()
        while True:
            # look for incoming tornado request
            if (self.sp.inWaiting() > 0):
                data = self.readSerial()
                print("reading from serial: " + data)
