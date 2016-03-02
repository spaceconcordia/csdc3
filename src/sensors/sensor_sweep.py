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
    ds1624 = [TEMP_0, TEMP_4]
    ds18b20 = [PANEL0, PANEL1]
    for temp_sensor in ds1624:
        SensorManager.init_temp_sensor(temp_sensor)
    SensorManager.gpio_output(PSS_HTR_EN_1_GPIO, ON)
    with open("/root/csdc3/src/sensors/temp_log.txt", "a") as f:
        for i in range(1):
            start = time.time()
            temperatures = []
            for temp_sensor in ds1624:
                value = SensorManager.read_temp_sensor(temp_sensor)
                temperatures.append(value)

            
            for temp_sensor in ds18b20:
                value = SensorManager.get_panel_data(temp_sensor)
                temperatures.append(value)
            

            readtime = time.time() - start
            temperatures.append(readtime)
            f.write(str(temperatures) + '\n')

    SensorManager.gpio_output(PSS_HTR_EN_1_GPIO, OFF)
    for temp_sensor in ds1624:
        SensorManager.stop_temp_sensor(temp_sensor)

if __name__ == "__main__":
    main()
