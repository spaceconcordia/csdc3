import sys
sys.path.append('/root/csdc3/src/sensors')
import unittest
import time
from sensor_manager import SensorManager
from sensor_entropy import SensorEntropy
from sensor_constants import *

class PayloadTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_adc_init(self):
        SensorManager.mux_select(ADC)
        SensorManager.init_adc(ADC)
        addr = SensorEntropy.addr(ADC)
        adc_reg = SensorEntropy.reg(ADC)
        bus = SensorManager.bus

        config = bus.read_byte_data(addr, adc_reg['CONFIG_REG'])
        mode = bus.read_byte_data(addr, adc_reg['ADV_CONFIG_REG'])
        conv = bus.read_byte_data(addr, adc_reg['CONV_RATE_REG'])
        ch = bus.read_byte_data(addr, adc_reg['CHANNEL_DISABLE_REG'])
        limits = bus.read_byte_data(addr, adc_reg['LIMIT_REG_BASE'])

        self.assertEqual(config, 0x01)
        self.assertEqual(mode, 0x04)
        self.assertEqual(conv, 0x01)
        self.assertEqual(ch, 0x00)
        self.assertEqual(limits, 0x05)

    def test_adc_read(self):
        experiment = 2
        strain, force, adc_temp = SensorManager.read_adc(experiment, ADC)
        self.assertNotEqual(strain, -1)
        self.assertNotEqual(force, -1)
        self.assertNotEqual(adc_temp, -1)

    def test_temp_sensor(self):
        ds1624 = [TEMP_PAYLOAD_A, TEMP_PAYLOAD_B, TEMP_PAYLOAD_BRD]
        for sensor in ds1624:
            SensorManager.init_temp_sensor(sensor)
            value = SensorManager.read_temp_sensor(sensor)
            self.assertNotEqual(value, -1)

    def test_payload_switches(self):
        SensorManager.gpio_output(PAYLOAD_EN_GPIO, ON)
        SensorManager.gpio_output(PAYLOAD_HTR_A_GPIO, ON)
        time.sleep(1)
        SensorManager.gpio_output(PAYLOAD_EN_GPIO, OFF)
        SensorManager.gpio_output(PAYLOAD_HTR_A_GPIO, OFF)

    def test_adc_stop(self):
        SensorManager.mux_select(ADC)
        SensorManager.stop_adc_sensor(ADC)
        SensorManager.mux_select(ADC)
        SensorManager.init_adc(ADC)
        addr = SensorEntropy.addr(ADC)
        adc_reg = SensorEntropy.reg(ADC)
        bus = SensorManager.bus

        config = bus.read_byte_data(addr, adc_reg['CONFIG_REG'])
        self.assertEqual(config, 0x00)

if __name__ == "__main__":
    unittest.main()
