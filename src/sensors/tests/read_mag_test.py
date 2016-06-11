import sys
sys.path.append('/root/csdc3/lib/ablib')
sys.path.append('/root/csdc3/src/logs')
sys.path.append('/root/csdc3/src/sensors')
sys.path.append('/root/csdc3/src/logs/config_setup')
from time import sleep
from sensor_constants import *
from sensor_manager import SensorManager

def main():
    hmc5883 = [MAG_0, MAG_1, MAG_2]
    for sensor in hmc5883:
        SensorManager.init_magnetometer(sensor)
    while True:
        for sensor in hmc5883:
            value = SensorManager.read_magnetometer(sensor)
            print(value)
        print
        sleep(1)

if __name__ == "__main__":
    main()
