import sys
sys.path.append('/root/csdc3/src/sensors')
import unittest
import time
from sensor_manager import SensorManager
from sensor_constants import *

class Tests(unittest.TestCase):
    gpioState = ON
    def setUp(self):
        pass

    def test_magnetometer(self):
        hmc5883 = [MAG_0, MAG_1, MAG_2]
        for sensor in hmc5883:
            SensorManager.init_magnetometer(sensor)
            value = SensorManager.read_magnetometer(sensor)
            self.assertNotEqual(value, -1)
            SensorManager.stop_magnetometer(sensor)

    """
    def test_gyroscope(self):
        itg3400 = [GYRO_0, GYRO_1, GYRO_2]
        for sensor in itg3400:
            SensorManager.init_gyroscope(sensor)
            value = SensorManager.read_gyroscope(sensor)
            self.assertNotEqual(value, -1)
            SensorManager.stop_gyroscope(sensor)
    """

    def test_ds1624(self):
        ds1624 = [TEMP_CDH_BRD]
        for sensor in ds1624:
            SensorManager.init_temp_sensor(sensor)
            value = SensorManager.read_temp_sensor(sensor)
            self.assertNotEqual(value, -1)

    def test_payload_gpio(self):
        gpios = [PAYLOAD_HTR_A_GPIO, PAYLOAD_HTR_B_GPIO, PAYLOAD_EN_GPIO]
        for gpio in gpios:
            retval = SensorManager.gpio_output(gpio, self.gpioState)
            self.assertEqual(True, retval)

    def test_pss_gpio(self):
        gpios = [PSS_HTR_EN_1_GPIO, PSS_HTR_EN_2_GPIO, PSS_HTR_EN_3_GPIO, \
                 PSS_HTR_EN_4_GPIO, PSS_HTR_MUX_SEL_GPIO]

        for gpio in gpios:
            retval = SensorManager.gpio_output(gpio, self.gpioState)
            self.assertEqual(True, retval)

    def test_cdh_gpio(self):
        gpios = [WATCHDOG_GPIO, SENSORS_EN_GPIO, RADIO_EN_GPIO, I2C_MUX_RESET_GPIO]
        for gpio in gpios:
            retval = SensorManager.gpio_output(gpio, self.gpioState)
            self.assertEqual(True, retval)

    def test_deployment_gpio(self):
        gpios = [DEPLOYMENT_SW_A_GPIO, DEPLOYMENT_SW_B_GPIO]
        for gpio in gpios:
            retval = SensorManager.gpio_output(gpio, self.gpioState)
            self.assertEqual(True, retval)

if __name__ == "__main__":
    unittest.main()
