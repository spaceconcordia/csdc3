from sensor_constants import *

class SensorEntropy:
    @staticmethod
    def name (sensor_type):
        """
        returns the actual device name if sensor_type passed is valid,
        else, return 'None'
        """
        if sensor_type in I2C_DEVICES_LIST:
            return I2C_DEVICES_LOOKUP_TABLE[sensor_type]["name"]
        # else
        return None

    def addr(sensor_type):
        if sensor_type in I2C_DEVICES_LIST:
            return I2C_DEVICES_LOOKUP_TABLE[sensor_type]["addr"]
        return None
    
    def reg(sensor_type):
        if sensor_type in I2C_DEVICES_LIST:
            return I2C_DEVICES_LOOKUP_TABLE[sensor_type]["reg"]
        return None

    def ch(sensor_type):
        if sensor_type in I2C_DEVICES_LIST:
            return I2C_DEVICES_LOOKUP_TABLE[sensor_type]["ch"]
        return None

if __name__ == "__main__":
    print(SensorEntropy.name(GYRO))
    print(SensorEntropy.addr(GYRO))
    print(SensorEntropy.reg(GYRO))
    print(SensorEntropy.ch(GYRO))