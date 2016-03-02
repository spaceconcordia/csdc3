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
        ds1624 = [TEMP_0, TEMP_4]
        SensorManager.init_temp_sensor(ds1624[0])
        value = SensorManager.read_temp_sensor(ds1624[0])
        self.assertNotEqual(value, -1)
            

    def test_gpio(self):
        for i in range(5):
            SensorManager.gpio_output(PAYLOAD_HTR_A_GPIO, ON)
            time.sleep(0.2)
            SensorManager.gpio_output(PAYLOAD_HTR_A_GPIO, OFF)
            time.sleep(0.2)
        
        self.assertEqual(1, 1)

if __name__ == "__main__":
    unittest.main()
