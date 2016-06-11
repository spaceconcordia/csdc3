import sys
sys.path.append('/root/csdc3/lib/ablib')
sys.path.append('/root/csdc3/src/logs')
sys.path.append('/root/csdc3/src/sensors')
sys.path.append('/root/csdc3/src/logs/config_setup')
from time import sleep
from sensor_entropy import *
from sensor_constants import *
from sensor_manager import SensorManager

def main():
    SensorManager.init_power_sensor(POWER)
    while True:
        print(SensorManager.read_power_sensor(POWER))
        sleep(1)

if __name__ == '__main__':
    main()
