import sys
sys.path.append('/root/csdc3/lib/ablib')
sys.path.append('/root/csdc3/src/logs')
sys.path.append('/root/csdc3/src/utility')
sys.path.append('/root/csdc3/src/logs/config_setup')
sys.path.append('/root/HE100-lib/Python')
from ablib_python3 import Pin
from chomsky import *
from time import sleep
from sensor_entropy import *
from sensor_constants import *
import smbus
import time
import math
from sensor_manager import SensorManager
import utility
from transclib import *
from transceiver_aleksandr import *

def main():
    ser = init_transceiver()
    SensorManager.gpio_output(RADIO_EN_GPIO, ON)
    time.sleep(5)
    if ser.isOpen():
        for i in range(5):
            curr_time = int(time.time())
            power_tuple = selectTelemetryLog(POWER)
            cdh_brd_temp = selectTelemetryLog(TEMP_CDH_BRD)
            power = power_tuple[0][1]
            temp = cdh_brd_temp[0][1]
            print(temp)
            SC_writeCallback(SC_transmit("POWER:%s| CDH_TEMP:%s | %d" % (power, temp, curr_time)), ser)
            time.sleep(5)
    else:
        ser.open()
    SensorManager.gpio_output(RADIO_EN_GPIO, OFF)
if __name__ == "__main__":
    main()
