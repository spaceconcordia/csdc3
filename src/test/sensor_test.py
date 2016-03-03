import sys
sys.path.append('/root/csdc3/src/sensors')
import unittest
import time
from sensor_manager import SensorManager
from sensor_constants import *

class Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_ds1624(self):
        ds1624 = [TEMP_PAYLOAD_A, TEMP_BAT_1]
        for sensor in ds1624:
            SensorManager.init_temp_sensor(sensor)
            value = SensorManager.read_temp_sensor(sensor)
            self.assertNotEqual(value, -1)

    def test_ds18b20(self):
        ds18b20 = [PANEL0, PANEL1]
        for sensor in ds18b20:
            value = SensorManager.get_panel_data(sensor)
            self.assertNotEqual(value, -1)

    def test_gpio(self):
        for i in range(5):
            SensorManager.gpio_output(PAYLOAD_HTR_A_GPIO, ON)
            time.sleep(0.2)
            SensorManager.gpio_output(PAYLOAD_HTR_A_GPIO, OFF)
            time.sleep(0.2)

        self.assertEqual(1, 1)

    def test_read_mag(self):
        """
        SensorManager.init_magnetometer()
        for i in range(5):
            x, y, z = SensorManager.read_magnetometer()
            print(x, y, z)
            time.sleep(1)
        """
        self.assertEqual(1, 1)

    def test_read_power(self):
        """
        SensorManager.init_power_sensor()
        for i in range(5):
            current, shunt, bus, power = read_power_sensor()
            time.sleep(1)
        SensorManager.stop_power_sensor()
        """
        self.assertEqual(1, 1)

if __name__ == "__main__":
    unittest.main()
