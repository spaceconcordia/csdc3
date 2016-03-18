import sys
sys.path.append("/root/csdc3/src/sensors/")
sys.path.append("/root/csdc3/src/utils/")
from sensor_manager import SensorManager
from sensor_constants import *
from statistics import median
from SharedLock import Lock
import time

class PowerMonitor:
    def __init__(self):
        self.controlStatus = False
        self.payloadLock = Lock("/root/csdc3/src/utils/payloadLock.tmp")
        self.sensorReadingLock = \
        Lock("/root/csdc3/src/utils/sensorReadingLock.tmp")
        self.pastReadingAboveThresh = True

    def check_health(self):
        """
        Determines whether battery chargers must be set manually
        """
        # Check if sensors are reading data in the system
        if areSensorsAcquiringData():
            return

        # Get temperature inputs
        tempIdentifiers = (TEMP_BAT_1, TEMP_BAT_2, TEMP_BAT_3, TEMP_BAT_4)
        tempValues = []
        for iden in tempIdentifiers:
            SensorManager.init_temp_sensor(iden)
            valueList = []
            # Get median of 5 value readings to remove outliers
            for i in range(0,5):
                valueList.append(SensorManager.read_temp_sensor(iden))
            tempValue = median(valueList)
            print(tempValue)
            SensorManager.stop_temp_sensor(iden)
            # Keep final value of sensor
            tempValues.append(tempValue)

        # Get status identifiers
        statusIdentifiers = (PSS_HTR_STAT_1_GPIO, PSS_HTR_STAT_2_GPIO,\
        PSS_HTR_STAT_3_GPIO, PSS_HTR_STAT_4_GPIO)
        statusValues = []
        for iden in statusIdentifiers:
                statusValues.append(SensorManager.gpio_input(iden,0))
        # Define manual heater identifiers
        heaterIdentifers = (PSS_HTR_EN_1_GPIO, PSS_HTR_EN_2_GPIO,\
        PSS_HTR_EN_3_GPIO, PSS_HTR_EN_4_GPIO)
        print('Status value: ' + str(statusValues[0]))

        # Check if payload is running
        if isPayloadAcquiringData():
            # Shut all battery heaters off
            self.controlStatus = True
            SensorManager.gpio_output(PSS_HTR_MUX_SEL_GPIO, OFF)
            for heater in heaterIdentifers:
                SensorManager.gpio_output(heater, OFF)
            self.lock.release()
            return

        # Take control if required
        for i in range(0,len(tempValues)):
            if self.temp_threshold(tempValues[i], 'GT') and statusValues[i] == 0:
                self.controlStatus = False
                SensorManager.gpio_output(PSS_HTR_MUX_SEL_GPIO, ON)
                return
            elif self.temp_threshold(tempValues[i], 'GT') and statusValues[i] == 1:
                self.controlStatus = True
                SensorManager.gpio_output(PSS_HTR_MUX_SEL_GPIO, OFF)
                SensorManager.gpio_output(heaterIdentifers[i], OFF)
                return
            elif self.temp_threshold(tempValues[i], 'LT') and statusValues[i] == 0:
                self.controlStatus = True
                SensorManager.gpio_output(PSS_HTR_MUX_SEL_GPIO, OFF)
                if self.is_battery_safe():
                    SensorManager.gpio_output(heaterIdentifers[i], ON)
                return
            elif self.temp_threshold(tempValues[i] 'LT') and statusValues[i] == 1:
                self.controlStatus = False
                SensorManager.gpio_output(PSS_HTR_MUX_SEL_GPIO, ON)
                return

    def temp_threshold(self, tempValue, sign):
        """
        Returns boolean for crossed temperature threshold
        """
        tempRef = 12
        thresholdPct = 0.1
        if sign == 'GT':
            result = tempValue > tempRef*(1+thresholdPct)
        elif sign == 'LT':
            result = tempValue < tempRef*(1-thresholdPct)
        else:
            raise Exception("Invalid parameter: must be 'GT' or 'LT'")
        return result

    def is_battery_safe(self):
        """
        Determines if heaters have enough power to heat batteries
        """
        return True


    def isPayloadAcquiringData(self):
        """
        Determines whether the payload experiment is running
        """
        return self.payloadLock.isLocked()

    def areSensorsAcquiringData(self):
        """
        Determines if there are sensor readings in progress
        """
        return self.sensorReadingLock.isLocked()

if __name__ == '__main__':
    powerMonitor = PowerMonitor()
    count = 0
    while count < 15:
        count += 1
        print('Count: ' + str(count))
        powerMonitor.check_health()
        time.sleep(2.5)
    time.sleep(3)
    SensorManager.gpio_output(PSS_HTR_MUX_SEL_GPIO, ON)
