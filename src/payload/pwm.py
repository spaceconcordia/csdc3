import sys
sys.path.append('/root/csdc3/src/sensors')
sys.path.append('/root/csdc3/lib/ablib')
from ablib_python3 import Pin
from time import sleep
import smbus
import time
import math
from sensor_manager import SensorManager
from sensor_constants import *

DUTY_CYCLE = 0.5
PERIOD = 1/1000.

def main():
    while True:
        SensorManager.gpio_output(PAYLOAD_EN_GPIO, ON)
        time.sleep(2)
        SensorManager.gpio_output(PAYLOAD_EN_GPIO, OFF)
        time.sleep(2)

if __name__ == "__main__":
    main()
