import sys
sys.path.append('/root/csdc3/lib/ablib')
sys.path.append('/root/csdc3/src/logs')
sys.path.append('/root/csdc3/src/logs/config_setup')
from sensor_manager import SensorManager
from sensor_constants import *
from sensor_entropy import *
from time import sleep

def main():
    ds18b20 = [PANEL0, PANEL1, PANEL2, PANEL3]
    while True:
        for temp_sensor in ds18b20:
            value = SensorManager.get_panel_data(temp_sensor)
            print value,
        print

if __name__ == "__main__":
    main()
