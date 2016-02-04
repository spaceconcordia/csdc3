from sensor_constants import *

class SensorEntropy:
    @staticmethod
    def _get_sensor_name (sensor_type):
        """
        returns the actual device name if sensor_type passed is valid,
        else, return 'None'
        """
        if sensor_type in I2C_DEVICES_LIST:
            return I2C_LOOKUP_TABLE[sensor_type]["name"]

        return None

if __name__ == "__main__":
    #print(SensorEntropy._get_sensor_name(GYRO))