import smbus
import time
import math

class SensorManager:
    def __init__(self):
        self.bus = smbus.SMBus(0)

        # initialize I2C MUX
        pass

    """ -------------------- Initialization --------------------- """

    def init_gyroscope(self):
        pass

    def init_magnetometer(self):
        bus.write_byte_data(0x1e, 0x02, 0x00)
        time.sleep(0.01)

    def init_real_time_clock(self):
        pass

    def init_temp_sensor(self):
        pass

    def init_adc(self):
        pass

    def init_power_sensor(self):
        pass

    """ -------------------- Reading --------------------- """

    def read_gyroscope(self):
        pass

    def read_magnetometer(self):
        # Get the values from the sensor
        valX = (bus.read_byte_data(address, 0x03) << 8) \
            | bus.read_byte_data(address, 0x04)
        valY = (bus.read_byte_data(address, 0x05) << 8) \
            | bus.read_byte_data(address, 0x06)
        valZ = (bus.read_byte_data(address, 0x07) << 8) \
            | bus.read_byte_data(address, 0x08)

        # Update the values to be of two compliment
        valX = twosToInt(valX, 16);
        valY = twosToInt(valY, 16);
        valZ = twosToInt(valZ, 16);

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

    def read_real_time_clock(self):
        pass

    def read_temp_sensor(self):
        pass

    def read_adc(self):
        pass

    def read_power_sensor(self):
        pass


def main():
    sensorManager = SensorManager()
    print sensorManager

if __name__ == "__main__":
    main()
