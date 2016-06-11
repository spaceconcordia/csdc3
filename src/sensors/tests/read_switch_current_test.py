import sys
sys.path.append('/root/csdc3/lib/ablib')
sys.path.append('/root/csdc3/src/logs')
sys.path.append('/root/csdc3/src/logs/config_setup')
sys.path.append('/root/csdc3/src/sensors')
from time import sleep
from sensor_constants import *
from sensor_manager import SensorManager

def main():
    while True:
        payload_current = SensorManager.read_switch_current(PAYLOAD_SWITCH_ADC_ID, True)
        radio_current = SensorManager.read_switch_current(RADIO_SWITCH_ADC_ID, True)
        print(payload_current, radio_current)
        sleep(1)

if __name__ == '__main__':
    main()
