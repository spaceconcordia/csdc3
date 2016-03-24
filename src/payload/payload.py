#!/usr/bin/python

'''
Application to run the three-point bending test payload
'''
import sys
sys.path.append("/root/csdc3/src/sensors")
sys.path.append("/root/csdc3/src/utils/")
sys.path.append("/root/csdc3/src/logs/")
sys.path.append("/root/csdc3/src/logs/config_setup")
import time
import os
from sensor_entropy import *
from sensor_manager import SensorManager
from SharedLock import Lock
from chomsky import *

class Payload():
    PAYLOAD_MAX_TIME = 180
    PAYLOAD_ACTUATE_TIME = 60.0
    PAYLOAD_MAX_STRAIN = 9999
    PAYLOAD_SAMPLING_FREQ = 3

    PAYLOAD_MIN_SPACE = 10440
    PAYLOAD_MIN_VBAT = 3
    HEATER_ON_TIME = 3
    def __init__(self, experiment, max_time=PAYLOAD_MIN_SPACE, \
                  max_strain=PAYLOAD_MAX_STRAIN, sampling_freq=PAYLOAD_SAMPLING_FREQ):
        self.experiment = experiment
        self.max_time = max_time
        self.max_strain = max_strain
        self.sampling_freq = sampling_freq
        self.lock = Lock("/root/csdc3/src/utils/payloadLock.tmp")

    def check_initial_conditions(self):
        # Check battery voltage
        vbat = 3.3
        # Check available memory
        free_space = get_disk_usage('/')
        print("Free space", free_space)
        if free_space >= self.PAYLOAD_MIN_SPACE and vbat >= self.PAYLOAD_MIN_VBAT:
            return True
        else:
            return False

    def init_sensors(self):
        SensorManager.init_adc(ADC)
        #SensorManager.init_temp_sensor()

    def start(self):
        insertDebugLog(NOTICE, "Starting. Runtime: %ds, Actuate time: %ds, Max strain: %d, Sampling Freq: %d." % \
            (self.PAYLOAD_MAX_TIME, self.PAYLOAD_ACTUATE_TIME, self.PAYLOAD_MAX_STRAIN, \
             self.HEATER_ON_TIME), PAYLOAD, int(time.time()))

        if not self.check_initial_conditions():
            return False
        print("Starting payload...")
        self.lock.acquire()
        self.set_power(True)
        self.init_sensors()
        start_time = time.time()
        elapsed = 0
        while True:
            if elapsed <= self.PAYLOAD_ACTUATE_TIME:
                self.set_heaters(self.experiment, True)
                time.sleep(self.HEATER_ON_TIME)
            else:
                print("No longer turning heaters on")
                time.sleep(self.HEATER_ON_TIME)
                self.set_heaters(self.experiment, False)
            self.set_heaters(self.experiment, False)
            elapsed = time.time() - start_time
            off_time = time.time()
            print("[" + str(round(elapsed, 3)) + " s] ", end='')
            strain, force, adc_temp, heater_temp = SensorManager.read_adc(self.experiment, ADC)
            print(strain, force, adc_temp, heater_temp)
            sleep_time = time.time() - off_time
            elapsed = time.time() - start_time
            time.sleep(abs(self.HEATER_ON_TIME - sleep_time))
            elapsed = time.time() - start_time
            strain, force, adc_temp, heater_temp = SensorManager.read_adc(self.experiment, ADC)
            print("[" + str(round(elapsed, 3)) + " s] ", end='')
            print(strain, force, adc_temp, heater_temp)

            if self.is_end_condition(strain, elapsed):
                break
        self.end()
        self.lock.release()
        return True

    def end(self):
        print("Payload ending...")
        # Turn off ADC
        SensorManager.stop_adc_sensor(ADC)
        self.set_heaters(self.experiment, False)
        self.set_power(False)
        insertDebugLog(NOTICE, "Ending", PAYLOAD, int(time.time()))

    def set_heaters(self, experiment=0, state=False):
        if state == False:
            SensorManager.gpio_output(PAYLOAD_HTR_A_GPIO, OFF)
        else:
            SensorManager.gpio_output(PAYLOAD_HTR_A_GPIO, ON)

        return True

    def set_power(self, isOn=False):
        insertDebugLog(NOTICE, "Power to %d" % (isOn), PAYLOAD, int(time.time()))
        print("Setting power for payload: ", isOn)
        if isOn == False:
            SensorManager.gpio_output(PAYLOAD_EN_GPIO, OFF)
        else:
            SensorManager.gpio_output(PAYLOAD_EN_GPIO, ON)
            SensorManager.gpio_output(SENSORS_EN_GPIO, ON)
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
    #time.sleep(480)
    payload = Payload(0)
    payload.start()

if __name__ == "__main__":
    main()
