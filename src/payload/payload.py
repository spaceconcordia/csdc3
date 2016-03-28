#!/usr/bin/python

'''
Application to run the three-point bending test payload
'''
import sys
sys.path.append("/root/csdc3/src/sensors")
sys.path.append("/root/csdc3/src/utils/")
sys.path.append("/root/csdc3/src/logs/")
sys.path.append("/root/csdc3/src/logs/config_setup")
from sensor_entropy import *
from sensor_manager import SensorManager
from SharedLock import Lock
from chomsky import *
import argparse
import utility
import time
import os

class Payload():
    PAYLOAD_MAX_TIME = 450
    PAYLOAD_ACTUATE_TIME = 255.0
    PAYLOAD_MAX_LOADCELL = 9999
    PAYLOAD_SAMPLING_FREQ = 3

    PAYLOAD_MIN_SPACE = 10440
    PAYLOAD_MIN_VBAT = 3.0
    MAX_ACTUATE_TEMP = 40.
    HEATER_ON_TIME = 3
    def __init__(self, experiment, max_time=PAYLOAD_MIN_SPACE, \
                 max_loadcell=PAYLOAD_MAX_LOADCELL, sampling_freq=PAYLOAD_SAMPLING_FREQ, \
                 max_temp=MAX_ACTUATE_TEMP, heater_period=HEATER_ON_TIME, actuate_time=PAYLOAD_ACTUATE_TIME):
        self.experiment = experiment
        if self.experiment == 1:
            self.heater = PAYLOAD_HTR_B_GPIO
            self.temp_sensor = TEMP_PAYLOAD_B
        else:
            self.heater = PAYLOAD_HTR_A_GPIO
            self.temp_sensor = TEMP_PAYLOAD_A
        self.max_time = max_time
        self.max_loadcell = max_loadcell
        self.sampling_freq = sampling_freq
        self.heater_period = heater_period
        self.max_temp = max_temp
        self.actuate_time = actuate_time
        self.lock = Lock("/root/csdc3/src/utils/payloadLock.tmp")

    def check_initial_conditions(self):
        # Check battery voltage
        SensorManager.init_power_sensor(POWER)
        power = SensorManager.read_power_sensor(POWER)
        vbat = power[0] / 1000.
        # Check available memory
        free_space = utility.get_disk_usage('/')
        #print("Free space", free_space)
        if free_space >= self.PAYLOAD_MIN_SPACE and vbat >= self.PAYLOAD_MIN_VBAT:
            return True
        else:
            print("Experiment cancelled")
            print(free_space, vbat)
            insertDebugLog(NOTICE, "Cancelled. Free space: %d, vbat: %.2f" % \
                (free_space, vbat, PAYLOAD, int(time.time())))
            return False

    def init_sensors(self):
        SensorManager.init_adc(ADC)
        SensorManager.init_temp_sensor(self.temp_sensor)

    def start(self):
        insertDebugLog(NOTICE, "Starting. Runtime: %ds, Actuate time: %ds, Max strain: %d, Sampling Freq: %d." % \
            (self.max_time, self.actuate_time, self.max_loadcell, \
             self.heater_period), PAYLOAD, int(time.time()))
        print("Starting payload...")
        print("Runtime: %ds, Actuate time: %ds, Max strain: %d, Sampling period: %ds" % \
            (self.max_time, self.actuate_time, self.max_loadcell, \
             self.heater_period))

        if not self.check_initial_conditions():
            return False
        self.lock.acquire()
        self.set_power(True)
        self.init_sensors()
        start_time = time.time()
        elapsed = 0
        while True:
            heater_temp = 0
            if elapsed <= self.actuate_time or heater_temp < self.max_temp:
                self.set_heaters(self.experiment, True)
                time.sleep(self.heater_period)
            else:
                print("No longer turning heaters on")
                time.sleep(self.heater_period)
                self.set_heaters(self.experiment, False)
            self.set_heaters(self.experiment, False)
            elapsed = time.time() - start_time
            off_time = time.time()
            print("[" + str(round(elapsed, 3)) + " s] ", end='')
            strain, force, adc_temp = SensorManager.read_adc(self.experiment, ADC)
            heater_temp = SensorManager.read_temp_sensor(self.temp_sensor)
            print(strain, force, adc_temp, heater_temp)
            sleep_time = time.time() - off_time
            elapsed = time.time() - start_time
            time.sleep(abs(self.heater_period - sleep_time))
            elapsed = time.time() - start_time
            strain, force, adc_temp = SensorManager.read_adc(self.experiment, ADC)
            heater_temp = SensorManager.read_temp_sensor(self.temp_sensor)
            print("[" + str(round(elapsed, 3)) + " s] ", end='')
            print(strain, force, adc_temp, heater_temp)

            if self.is_end_condition(strain, elapsed):
                break
        if self.experiment:
            exp = 'B'
        else:
            exp = 'A'
        insertPayloadLog(int(start_time), int(time.time()), exp)
        self.end()
        self.lock.release()
        return True

    def end(self):
        print("Payload ending...")
        insertDebugLog(NOTICE, "Ending", PAYLOAD, int(time.time()))

        SensorManager.stop_temp_sensor(self.temp_sensor)
        SensorManager.stop_adc_sensor(ADC)

        self.set_heaters(self.experiment, False)
        self.set_power(False)

    def set_heaters(self, experiment=0, state=False):
        if state == False:
            SensorManager.gpio_output(self.heater, OFF)
        else:
            SensorManager.gpio_output(self.heater, ON)

        return True

    def set_power(self, isOn=False):
        insertDebugLog(NOTICE, "Power to %d" % (isOn), PAYLOAD, int(time.time()))
        print("Setting power for payload: ", isOn)
        if isOn == False:
            SensorManager.gpio_output(PAYLOAD_EN_GPIO, OFF)
            SensorManager.gpio_output(OLD_PAYLOAD_EN_GPIO, OFF)
        else:
            SensorManager.gpio_output(PAYLOAD_EN_GPIO, ON)
            SensorManager.gpio_output(OLD_PAYLOAD_EN_GPIO, ON)
            SensorManager.gpio_output(SENSORS_EN_GPIO, ON)
        return True

    def is_end_condition(self, strain, elapsed):
        if strain >= self.max_loadcell or elapsed >= self.max_time:
            return True
        else:
            return False

def main():
    parser = argparse.ArgumentParser(description="Payload experiment to perform a 3-point bending test on a self-healing material",
                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("-b", "--runb", action="store_true", help="Select second experiment to run")
    parser.add_argument("-f", "--frequency", type=int, default=3, help="Period for sampling and heater pwm. E.g. -f 3 -> samples every 3 seconds")
    parser.add_argument("-t", "--runtime", type=int, default=450, help="Total run time of experiment in seconds")
    parser.add_argument("-a", "--actuatetime", type=int, default=250, help="Total run time to keep heaters on")
    parser.add_argument("-l", "--loadcell", type=int, default=3000, help="Max load cell value to reach")
    parser.add_argument("-m", "--maxtemp", type=float, default=40.0, help="Max temperature for heaters to be on")
    args = parser.parse_args()
    experiment_num = args.runb
    frequency = args.frequency
    runtime = args.runtime
    actuatetime = args.actuatetime
    loadcell = args.loadcell
    maxtemp = args.maxtemp

    payload = Payload(experiment=experiment_num, heater_period=frequency, \
                      max_time=runtime, actuate_time=actuatetime, max_loadcell=loadcell)
    payload.start()

if __name__ == "__main__":
    main()
