import sys
sys.path.append('/root/csdc3/lib/ablib')
sys.path.append('/root/csdc3/src/logs')
sys.path.append('/root/csdc3/src/logs/config_setup')
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
    tempSensors = (TEMP_PAYLOAD_A, TEMP_PAYLOAD_B, TEMP_PAYLOAD_BRD, \
    TEMP_PWR_BRD, TEMP_BAT_1, TEMP_BAT_2, TEMP_BAT_3, TEMP_BAT_4, \
    TEMP_EPS_BRD, TEMP_CDH_BRD)

    for sensor in tempSensors:
        SensorManager.init_temp_sensor(sensor)
        time.sleep(3)
        print(SensorManager.read_temp_sensor(sensor))
        time.sleep(3)
        SensorManager.stop_temp_sensor(sensor)
        time.sleep(3)

if __name__ == '__main__':
    main()