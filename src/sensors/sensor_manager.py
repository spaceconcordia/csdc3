import smbus
import time
import math
import

class SensorManager:

    bus = smbus.SMBus(0)

    """ -------------------- Initialization --------------------- """

    @staticmethod
    def init_i2c_mux():
        pass

    @staticmethod
    def init_gyroscope():
        pass

    @staticmethod
    def init_magnetometer():
        SensorManager.bus.write_byte_data(0x1e, 0x02, 0x01)
        time.sleep(0.01)

    @staticmethod
    def init_real_time_clock():
        pass

    @staticmethod
    def init_temp_sensor():
        pass

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

        address = 0x1e

        # Get the values from the sensor
        valX = (SensorManager.bus.read_byte_data(address, 0x03) << 8) \
            | SensorManager.bus.read_byte_data(address, 0x04)
        valY = (SensorManager.bus.read_byte_data(address, 0x05) << 8) \
            | SensorManager.bus.read_byte_data(address, 0x06)
        valZ = (SensorManager.bus.read_byte_data(address, 0x07) << 8) \
            | SensorManager.bus.read_byte_data(address, 0x08)

        # Update the values to be of two compliment
        valX = SensorManager.twosToInt(valX, 16);
        valY = SensorManager.twosToInt(valY, 16);
        valZ = SensorManager.twosToInt(valZ, 16);

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
        print "{0:-3f}".format(radians), "{0:-3f}".format(degrees)

    @staticmethod
    def read_real_time_clock():
        pass

    @staticmethod
    def read_temp_sensor():
        pass

    @staticmethod
    def read_adc():
        pass

    @staticmethod
    def read_power_sensor():
        pass

    """ ------------- Other ------------- """

    @staticmethod
    def twosToInt(val, len):
        if val & (1 << len - 1):
          val = val - (1 << len)
        return val

def main():
    SensorManager.init_magnetometer()
    SensorManager.read_magnetometer()

if __name__ == "__main__":
    main()
