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
    SensorManager.gpio_output(PAYLOAD_EN_GPIO, OFF)
    SensorManager.gpio_output(DEPLOYMENT_SW_A_GPIO, OFF)
    SensorManager.gpio_output(DEPLOYMENT_SW_B_GPIO, OFF)
    SensorManager.gpio_output(PAYLOAD_HTR_A_GPIO, OFF)
    SensorManager.gpio_output(PAYLOAD_HTR_B_GPIO, OFF)
    SensorManager.gpio_output(PSS_HTR_EN_1_GPIO, OFF)
    SensorManager.gpio_output(PSS_HTR_EN_2_GPIO, OFF)
    SensorManager.gpio_output(PSS_HTR_EN_3_GPIO, OFF)
    SensorManager.gpio_output(PSS_HTR_EN_4_GPIO, OFF)
    SensorManager.gpio_output(PSS_HTR_MUX_SEL_GPIO, OFF)
    SensorManager.gpio_output(PSS_HTR_EN_1_GPIO, OFF)
    SensorManager.gpio_output(RADIO_EN_GPIO, OFF)
    SensorManager.gpio_output(SENSORS_EN_GPIO, OFF)  
    time.sleep(2)
    SensorManager.gpio_output(SENSORS_EN_GPIO, ON)
    SensorManager.gpio_output(RADIO_EN_GPIO, OFF)
if __name__ == "__main__":
    main()
