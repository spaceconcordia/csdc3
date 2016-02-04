from sensor_constants import *
import pprint

class SensorEntropy:
    @staticmethod
    def name (sensor_type):
        """
        returns the actual device name if the sensor_type passed is valid,
        else, return 'None'
        """
        if sensor_type in I2C_DEVICES_LIST:
            return I2C_DEVICES_LOOKUP_TABLE[sensor_type][NAME]
        # else
        return None

    @staticmethod
    def addr(sensor_type):
        """
        returns the i2c base address if the sensor_type passed is valid,
        else, return 'None'
        """
        if sensor_type in I2C_DEVICES_LIST:
            return format(I2C_DEVICES_LOOKUP_TABLE[sensor_type][ADDR],'#04x')
        return None

    @staticmethod
    def reg(sensor_type):
        """
        returns the registers if the sensor_type passed is valid,
        else, return 'None'
        """
        if sensor_type in I2C_DEVICES_LIST:
            return I2C_DEVICES_LOOKUP_TABLE[sensor_type][REG]
        return None

    @staticmethod
    def ch(sensor_type):
        """
        returns the channels if the sensor_type passed is valid,
        else, return 'None'
        """
        if sensor_type in I2C_DEVICES_LIST:
            return I2C_DEVICES_LOOKUP_TABLE[sensor_type][CH]
        return None

if __name__ == "__main__":
    for sensor in I2C_DEVICES_LIST:
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
        print("name: " + SensorEntropy.name(sensor))
        print("addr:" + str(SensorEntropy.addr(sensor)))
        print("reg:" + str(SensorEntropy.reg(sensor)))
        print("ch: " + str(SensorEntropy.ch(sensor)))
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
