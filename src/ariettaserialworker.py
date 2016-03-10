import serial
import time
import multiprocessing

## Change this to match your local settings
SERIAL_PORT = '/dev/ttyS0'
SERIAL_BAUDRATE = 115200

input_queue = multiprocessing.Queue()
output_queue = multiprocessing.Queue()

RAM_INTENS_PROC = "RAMIP-"
CPU_INTENS_PROC = "CPUIP-"
DISK_PARTITION = "DISPA-"
GET_TIME = "GETTI-"
SET_TIME = "SETTI-"
GET_LOGGED_DATA = "GETLO-"
DEL_LOGGED_DATA = "DELLO-"
a = "TIMTA-"
b = "UPDBI-"
c = "ROLBA-"
DEPLOY_ANT = "DEPAN-"
PAYLOAD_JOB = "PAYJO-"
PAYLOAD_TELEMETRY = "PAYTE-"
POWER_TELEMETRY = "POWTE-"
HEALTH_MONITORING = "HEAMO-"
END = "END"

if __name__ == "__main__":
    sp = serial.Serial(
       port='/dev/ttyS0',
       baudrate = 115200,
       parity=serial.PARITY_NONE,
       stopbits=serial.STOPBITS_ONE,
       bytesize=serial.EIGHTBITS,
       timeout=1
    )
    sp.flushInput()
    while True:
        if sp.inWaiting() > 0:
            data = sp.read()
            sp.write(data+data)
