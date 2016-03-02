import unittest
import time
from sensors import sensor_manager.SensorManager
from sensors import sensor_constants

class TestSensors(unittest.TestCase):
    def read_temperature(self):
        SensorManager.init_temp_sensor(TEMP_4)
        for i in range(5):
            temp_value = SensorManager.read_temp_sensor(TEMP_4)
            print(temp_value)
            time.sleep(1)
        SensorManager.stop_temp_sensor(TEMP_4)

    def read_adc(self):
        SensorManager.init_adc()
        for i in range(5):
            strain, force, adc_temp = SensorManager.read_adc(self.experiment)
            print(strain, force, adc_temp)
            time.sleep(1)
        SensorManager.stop_adc()

    def battery_heater(self):
        heater = Pin('J4.31','OUTPUT')
        heater.on()

        temp_value = -999

        SensorManager.init_temp_sensor(TEMP_4)
        start = time.time()
        with open("log.txt", "w") as f:
            while temp_value <= 18.5:
                temp_value = SensorManager.read_temp_sensor(TEMP_4)
                #print(temp_value)
                f.write(str(temp_value) + '\n')
                f.flush()
                time.sleep(1)
        SensorManager.stop_temp_sensor(TEMP_4)

    def gpio_toggle(self):
        heater = Pin('J4.31','OUTPUT')
        for i in range(5):
            heater.on()
            time.sleep(0.5)
            heater.off()
            time.sleep(0.5)

    def read_mag(self):
        SensorManager.init_magnetometer()
        for i in range(5):
            x, y, z = SensorManager.read_magnetometer()
            print(x, y, z)
            time.sleep(1)

    def read_power(self):
        SensorManager.init_power_sensor()
        for i in range(5):
            current, shunt, bus, power = read_power_sensor()
            time.sleep(1)
        SensorManager.stop_power_sensor()

   def mux_switch(self):
       pass

   def gpio_toggle(self):
       for i in range(5):
           SensorManager.gpio_output('J4.31', ON)
           time.sleep(1)
           SensorManager.gpio_output('J4.31', OFF)
           time.sleep(1)

   def w1_read(self):
       for i in range(5):
           for panel in panels:
               temperature = SensorManager.get_panel_data(panel)
               print(temperature, end=',')
           print()

if __name__ == "__main__":
    unittest.main()
