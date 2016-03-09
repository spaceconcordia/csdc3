import sys
sys.insert.path("/root/csdc3/src/sensors")
from sensor_manager import SensorManager

class PowerMonitor:
    def __init__(self):
        self.controlStatus = False

    def check_health(self):
        # Get temperature inputs
        tempIdentifiers = (TEMP_BAT_1, TEMP_BAT_2, TEMP_BAT_3, TEMP_BAT_4)
        tempValues = []
        for iden in tempIdentifiers:
            SensorManager.init_temp_sensor(iden)
            tempValue = SensorManager.read_temp_sensor(iden)
            SensorManager.stop_temp_sensor(iden)
            tempValues.append(tempValue)

        # Get status identifiers
        statusIdentifiers = (PSS_HTR_STAT_1_GPIO, PSS_HTR_STAT_2_GPIO,\
        PSS_HTR_STAT_3_GPIO, PSS_HTR_STAT_4_GPIO)
        statusValues = []

        # Define manual heater identifiers
        heaterIdentifers = (PSS_HTR_EN_1_GPIO, PSS_HTR_EN_2_GPIO,\
        PSS_HTR_EN_3_GPIO, PSS_HTR_EN_4_GPIO)

        for iden in statusIdentifiers:
                statusValues.append(SensorManager.gpio_input(iden))

        # Take control if required
        for i in range(0,len(tempValues)):
            if tempValues[i] > self.temp_threshold() and statusValues[i] == 0:
                self.controlStatus = False
                SensorManager.gpio_output(PSS_HR_MUX_SEL_GPIO, HIGH)
                return
            elif tempValues[i] > self.temp_threshold() and statusValues[i] == 1:
                self.controlStatus = True
                SensorManager.gpio_output(PSS_HR_MUX_SEL_GPIO, LOW)
                SensorManager.gpio_output(heaterIdentifers[i], LOW)
                return
            elif tempValues[i] < self.temp_threshold() and statusValues[i] == 0:
                self.controlStatus = True
                SensorManager.gpio_output(PSS_HR_MUX_SEL_GPIO, LOW)
                if self.is_battery_safe():
                    SensorManager.gpio_output(heaterIdentifers[i], HIGH)
                return
            elif tempValues[i] < self.temp_threshold() and statusValues[i] == 1:
                self.controlStatus = False
                SensorManager.gpio_output(PSS_HR_MUX_SEL_GPIO, HIGH)
                return

    def temp_threshold(self):
        return 8

    def is_battery_safe(self):
        return True


if __name__ == '__main__':
    powerMonitor = PowerMonitor()
    powerMonitor.check_health()
