import sys
sys.path.append("/root/csdc3/src/sensors")
sys.path.append("/root/csdc3/src/logs/")
sys.path.append("/root/csdc3/src/logs/config_setup")
import time
import os
from sensor_entropy import *
from sensor_manager import SensorManager

def main():
    SensorManager.gpio_output(PAYLOAD_EN_GPIO, ON)
    SensorManager.init_adc(ADC)
    start_time = time.time()
    while True:
        strain, force, adc_temp = SensorManager.read_adc(0, ADC)
        elapsed = time.time() - start_time
        print("[" + str(round(elapsed, 3)) + " s] ")
        print(strain, force, adc_temp)
        time.sleep(2)

if __name__ == "__main__":
    main()
