import sys
sys.insert.path("/root/csdc3/src/sensors")
from sensor_manager import SensorManager

class PowerMonitor:
    def check_health(self):
        # Get temperature inputs
        tempIdentifiers = (TEMP_BAT_1, TEMP_BAT_2, TEMP_BAT_3, TEMP_BAT_4)
        tempValues = []
        for iden in tempIdentifiers:
            SensorManager.init_temp_sensor(iden)
            tempValue = SensorManager.read_temp_sensor(iden)
            SensorManager.stop_temp_sensor(iden)
            tempValues.append(tempValue)

        # Perform logic
        pass

        # Output data
        SensorManager.gpio_output(PSS_HTR_EN_1_GPIO, ON)
        SensorManager.gpio_output(PSS_HTR_EN_2_GPIO, ON)
        SensorManager.gpio_output(PSS_HTR_EN_3_GPIO, ON)
        SensorManager.gpio_output(PSS_HTR_EN_4_GPIO, ON)
        SensorManager.gpio_output(PSS_HR_MUX_SEL_GPIO, ON)
