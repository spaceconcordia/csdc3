#!/usr/bin/python

'''
Application to run the three-point bending test payload
'''
import sys
sys.path.append("/root/csdc3/src/sensors")
import time
import os
from sensor_entropy import *
from sensor_manager import SensorManager

class Payload():
    PAYLOAD_MAX_TIME = 30
    PAYLOAD_MAX_STRAIN = 9999
    PAYLOAD_SAMPLING_FREQ = 2

    PAYLOAD_MIN_SPACE = 10440
    PAYLOAD_MIN_VBAT = 3
    def __init__(self, experiment, max_time=PAYLOAD_MIN_SPACE, \
                  max_strain=PAYLOAD_MAX_STRAIN, sampling_freq=PAYLOAD_SAMPLING_FREQ):
        self.experiment = experiment
        self.max_time = max_time
        self.max_strain = max_strain
        self.sampling_freq = sampling_freq

    def check_initial_conditions(self):
        # Check battery voltage
        vbat = 3.3
        # Check available memory
        free_space = get_disk_usage('/')
        print(free_space)
        if free_space >= self.PAYLOAD_MIN_SPACE and vbat >= self.PAYLOAD_MIN_VBAT:
            return True
        else:
            return False

    def init_sensors(self):
        SensorManager.init_adc(ADC)
        #SensorManager.init_temp_sensor()

    def start(self):
        f = open("/var/tmp/payload.txt", "w")
        f.close()

        if not self.check_initial_conditions():
            return False
        print("Starting payload...")
        self.init_sensors()
        self.set_power(True)
        start_time = time.time()
        self.set_heaters(self.experiment, True)
        while True:
            elapsed = time.time() - start_time
            print("[" + str(round(elapsed, 3)) + " s] ", end='')
            strain, force, adc_temp = SensorManager.read_adc(self.experiment, ADC)
            print(strain, force, adc_temp)

            time.sleep(self.sampling_freq)

            if self.is_end_condition(strain, elapsed):
                break

        self.end()
        return True

    def end(self):
        os.system("rm /var/tmp/payload.txt")
        print("Payload ending...")
        self.set_heaters(self.experiment, False)
        self.set_power(False)
        # Turn off ADC
        SensorManager.stop_adc_sensor(ADC)

    def set_heaters(self, experiment=0, state=False):
        print("Turning heaters", state, "for experiment #", experiment)
        if state == False:
            SensorManager.gpio_output(PAYLOAD_HTR_A_GPIO, OFF)
        else:
            SensorManager.gpio_output(PAYLOAD_HTR_A_GPIO, ON)

        return True

    def set_power(self, isOn=False):
        print("Setting power for payload: ", isOn)
        if isOn == False:
            SensorManager.gpio_output(PAYLOAD_EN_GPIO, OFF)
        else:
            SensorManager.gpio_output(PAYLOAD_EN_GPIO, ON)
        return True

    def is_end_condition(self, strain, elapsed):
        if strain >= self.PAYLOAD_MAX_STRAIN or elapsed >= self.PAYLOAD_MAX_TIME:
            return True
        else:
            return False

def get_disk_usage(path):
    st = os.statvfs(path)
    free = (st.f_bavail * st.f_frsize)
    total = (st.f_blocks * st.f_frsize)
    used = (st.f_blocks - st.f_bfree) * st.f_frsize
    return free


def main():
    payload = Payload(2)
    payload.start()

if __name__ == "__main__":
    main()
