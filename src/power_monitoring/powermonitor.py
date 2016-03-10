import sys
sys.path.append("/root/csdc3/src/sensors/")
from sensor_manager import SensorManager
from sensor_constants import *
from statistics import median
import time

class PowerMonitor:
    def __init__(self):
        self.controlStatus = False

    def check_health(self):
        """
        Determines whether battery chargers must be set manually
        """
        # Get temperature inputs
        tempIdentifiers = (TEMP_BAT_1,)#, TEMP_BAT_2, TEMP_BAT_3, TEMP_BAT_4)
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
        print(statusValues)
        # Define manual heater identifiers
        heaterIdentifers = (PSS_HTR_EN_1_GPIO, PSS_HTR_EN_2_GPIO,\
        PSS_HTR_EN_3_GPIO, PSS_HTR_EN_4_GPIO)
        print('Status value: ' + str(statusValues[0]))
        # Take control if required
        for i in range(0,len(tempValues)):
            if tempValues[i] > self.temp_threshold() and statusValues[i] == 0:
                self.controlStatus = False
                SensorManager.gpio_output(PSS_HTR_MUX_SEL_GPIO, ON)
                return
            elif tempValues[i] > self.temp_threshold() and statusValues[i] == 1:
                self.controlStatus = True
                SensorManager.gpio_output(PSS_HTR_MUX_SEL_GPIO, OFF)
                SensorManager.gpio_output(heaterIdentifers[i], OFF)
                return
            elif tempValues[i] < self.temp_threshold() and statusValues[i] == 0:
                self.controlStatus = True
                SensorManager.gpio_output(PSS_HTR_MUX_SEL_GPIO, OFF)
                if self.is_battery_safe():
                    SensorManager.gpio_output(heaterIdentifers[i], ON)
                return
            elif tempValues[i] < self.temp_threshold() and statusValues[i] == 1:
                self.controlStatus = False
                SensorManager.gpio_output(PSS_HTR_MUX_SEL_GPIO, ON)
                return

    def temp_threshold(self):
        """
        Computes the proper threshold value for the temperature
        """
        return 15

    def is_battery_safe(self):
        """
        Determines if heaters have enough power to heat batteries
        """
        return True


if __name__ == '__main__':
    powerMonitor = PowerMonitor()
    count = 0
    while True:
        count = count +1
        print('Count: ' + str(count))
        powerMonitor.check_health()
        time.sleep(2.5)
    time.sleep(3)
    SensorManager.gpio_output(PSS_HTR_MUX_SEL_GPIO, ON)
