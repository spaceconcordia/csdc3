import sys
sys.path.append('/root/csdc3/src/sensors')
from sensor_entropy import *
from sensor_constants import *
import time
from sensor_manager import SensorManager

def main():
    while True:
        SensorManager.gpio_output(WATCHDOG_GPIO, ON)
        time.sleep(1)
        SensorManager.gpio_output(WATCHDOG_GPIO, OFF)
        time.sleep(10)

if __name__ == "__main__":
    main()
