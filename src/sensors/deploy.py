import sys
sys.path.append('/root/csdc3/lib/ablib')
sys.path.append('/root/csdc3/src/logs')
sys.path.append('/root/csdc3/src/utility')
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
import utility

def main():
    SensorManager.gpio_output(DEPLOYMENT_SW_A_GPIO, ON)
    time.sleep(10)
    SensorManager.gpio_output(DEPLOYMENT_SW_A_GPIO, OFF)

if __name__ == "__main__":
    main()
