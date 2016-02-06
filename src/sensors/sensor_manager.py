import sys
sys.path.append('/root/csdc3/lib/ablib')
from ablib_python3 import Pin
from time import sleep
from sensor_entropy import *
import smbus
import time
import math

class SensorManager:

    bus = smbus.SMBus(0)
    active_gpio_pins = {}

    """ -------------------- Initialization --------------------- """

    @staticmethod
    def init_i2c_mux():
        pass

    @staticmethod
    def init_gyroscope():
        pass

    @staticmethod
    def init_magnetometer():
        # SensorManager.bus.write_byte_data(0x1e, 0x02, 0x01)
        SensorManager.bus.write_byte_data(SensorEntropy.addr(MAG), \
        SensorEntropy.reg(MAG)['INIT'], 0x01)
        time.sleep(0.1)

    @staticmethod
    def init_real_time_clock():
        pass

    @staticmethod
    def init_temp_sensor():
        SensorManager.bus.write_byte_data(0x48, \
        0xEE, 0x01)
        SensorManager.bus.write_byte_data(0x48, \
        0xAC, 0x00)
        time.sleep(0.1)

    @staticmethod
    def init_adc():
        pass

    @staticmethod
    def init_power_sensor():
        pass

    """ -------------------- Reading --------------------- """

    @staticmethod
    def read_gyroscope():
        pass

    @staticmethod
    def read_magnetometer():

        address = SensorEntropy.addr(MAG)

        # Get the values from the sensor
        reg_x_h = SensorEntropy.reg(MAG)['X-H']
        reg_x_l = SensorEntropy.reg(MAG)['X-L']
        reg_y_h = SensorEntropy.reg(MAG)['Y-H']
        reg_y_l = SensorEntropy.reg(MAG)['Y-L']
        reg_z_h = SensorEntropy.reg(MAG)['Z-H']
        reg_z_l = SensorEntropy.reg(MAG)['Z-L']
        valX = (SensorManager.bus.read_byte_data(address, reg_x_h) << 8) \
            | SensorManager.bus.read_byte_data(address, reg_x_l)
        valY = (SensorManager.bus.read_byte_data(address, reg_y_h) << 8) \
            | SensorManager.bus.read_byte_data(address, reg_y_l)
        valZ = (SensorManager.bus.read_byte_data(address, reg_z_h) << 8) \
            | SensorManager.bus.read_byte_data(address, reg_z_l)

        # Update the values to be of two compliment
        valX = SensorManager.twos_to_int(valX, 16);
        valY = SensorManager.twos_to_int(valY, 16);
        valZ = SensorManager.twos_to_int(valZ, 16);

        # Change valX and valY to radians
        radians = math.atan2(valY, valX)
        radians += -0.0197

        # Compensate for errors
        if radians < 0:
            radians += 2*math.pi
        if radians > 2*math.pi:
            radians -= 2*math.pi

        # Turn radians into degrees
        degrees = math.floor(radians * 180 / math.pi)

        # Print the value to the output
        print(str(radians) + " " + str(degrees))

    @staticmethod
    def read_real_time_clock():
        pass

    @staticmethod
    def read_temp_sensor():
        SensorManager.bus.write_byte(0x48, 0xAA)
        decValue = SensorManager.bus.read_byte(0x48)
        fractValue = SensorManager.bus.read_byte(0x48)
        sleep(0.1)
        return SensorManager.conv_bin_to_int(decValue, fractValue)

    @staticmethod
    def read_adc():
        pass

    @staticmethod
    def read_power_sensor():
        pass

    """ -------------------- GPIO --------------------- """

    def gpio_output(pinId, onTime, offTime):

        if not (pinId in SensorManager.active_gpio_pins):
            SensorManager.active_gpio_pins[pinId] = 'off'

        led = Pin(pinId,'OUTPUT')

        if onTime == 0 and offTime == 0:
            return
        elif onTime == 0:
            if SensorManager.active_gpio_pins[pinId] == 'on':
                led.off()
                SensorManager.active_gpio_pins[pinId] == 'off'
            else:
                led.off()
        elif offTime == 0:
            if SensorManager.active_gpio_pins[pinId] == 'off':
                led.on()
                SensorManager.active_gpio_pins[pinId] = 'on'
            else:
                led.on()
        else:
            led.on()
            SensorManager.active_gpio_pins[pinId] = 'on'
            sleep(onTime)
            led.off()
            SensorManager.active_gpio_pins[pinId] = 'off'
            sleep(offTime)

    def gpio_input(pinId, inputTime):
        pass

    """ -------------------- Other --------------------- """

    @staticmethod
    def twos_to_int(val, len):
        if val & (1 << len - 1):
          val = val - (1 << len)
        return val

    @staticmethod
    def conv_bin_to_int(decimalBin, fractionalBin):
        result = 0
        isNegative = (decimalBin >> 7) & 0x1
        if isNegative:
            result = (decimalBin ^ 0xff) + 1
            result *= -1
        else:
            result = decimalBin
        tempFract = fractionalBin
        count = 1
        fract = 0
        while count <= 8:
            fract += ((tempFract >> 7) & 0x1) * pow(2, -count)
            tempFract = tempFract << 1
            count += 1
        result += fract
        return result

def main():
    # SensorManager.init_magnetometer()
    # SensorManager.read_magnetometer()
    SensorManager.init_temp_sensor()
    while 1:
        print(SensorManager.read_temp_sensor())
    # SensorManager.read_temp_sensor()

if __name__ == "__main__":
    main()
