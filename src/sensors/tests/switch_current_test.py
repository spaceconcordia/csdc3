import sys
sys.path.append('/root/csdc3/lib/ablib')
sys.path.append('/root/csdc3/src/logs')
sys.path.append('/root/csdc3/src/logs/config_setup')
sys.path.append('/root/csdc3/src/sensors')
from ablib_python3 import Pin
from chomsky import *
from time import sleep
from sensor_entropy import *
from sensor_constants import *
import smbus
import time
import math
from sensor_manager import SensorManager

def main():
    while True:
        payload_current = SensorManager.read_switch_current(PAYLOAD_SWITCH_CURR_SENSE, True)
        radio_current = SensorManager.read_switch_current(RADIO_SWITCH_CURR_SENSE, True)
        print(payload_current, radio_current, "volts")
        time.sleep(1)

if __name__ == '__main__':
    main()
