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
    try:
        while True:
            strain, force, adc_temp = SensorManager.read_adc(0, ADC)
            elapsed = time.time() - start_time
            print("[" + str(round(elapsed, 3)) + " s] ")
            print(strain, force, adc_temp)
            time.sleep(2)
    except KeyboardInterrupt:
        SensorManager.stop_adc_sensor(ADC)
        SensorManager.gpio_output(PAYLOAD_EN_GPIO, OFF)

def payload_test():
    SensorManager.gpio_output(PAYLOAD_EN_GPIO, ON)
    SensorManager.init_adc(ADC)
    start_time = time.time()
    try:
        while True:
            strain, force, heater_temp, adc_temp = SensorManager.read_payload(0, TEMP_BAT_1)
            elapsed = time.time() - start_time
            print("[" + str(round(elapsed, 3)) + " s] ")
            print(strain, force, heater_temp, adc_temp)
            time.sleep(2)
    except KeyboardInterrupt:
        SensorManager.stop_adc_sensor(ADC)
        SensorManager.gpio_output(PAYLOAD_EN_GPIO, OFF)

def adc_driver_test():
    SensorManager.gpio_output(PAYLOAD_EN_GPIO, ON)
    SensorManager.init_adc_driver()
    try:
        while True:
            for i in range(7):
                value = SensorManager.read_adc_driver(i)
                print value,
            print
            time.sleep(1)
    except KeyboardInterrupt:
        SensorManager.gpio_output(PAYLOAD_EN_GPIO, OFF)

if __name__ == "__main__":
    main()
    #payload_test()
    #adc_driver_test()
