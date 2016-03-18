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
    ds1624 = [TEMP_EPS_BRD]
    #ds18b20 = [PANEL0, PANEL1]
    for temp_sensor in ds1624:
        SensorManager.init_temp_sensor(temp_sensor)
    SensorManager.init_power_sensor(POWER)
    with open("/root/csdc3/src/sensors/temp_log.txt", "a") as f:
        for i in range(1):
            start = time.time()
            temperatures = []
            for temp_sensor in ds1624:
                value = SensorManager.read_temp_sensor(temp_sensor)
                temperatures.append(value)

            power = SensorManager.read_power_sensor(POWER)
            temperatures.append(power)
            print(temperatures)

            readtime = time.time() - start
            temperatures.append(readtime)
            f.write(str(temperatures) + '\n')

    for temp_sensor in ds1624:
        SensorManager.stop_temp_sensor(temp_sensor)

if __name__ == "__main__":
    main()
