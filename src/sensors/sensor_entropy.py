from sensor_constants import *

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
    def addr(sensorId):
        """
        returns the i2c base address if the sensor_type passed is valid,
        else, return 'None'
        """
        if sensorId in TEMP_IDENTIFIER_DICT:
            return TEMP_IDENTIFIER_DICT[sensorId][ADDR]
        elif sensorId in RTC_IDENTIFIER_DICT:
            return RTC_IDENTIFIER_DICT[sensorId][ADDR]
        elif sensorId in GYRO_IDENTIFIER_DICT:
            return GYRO_IDENTIFIER_DICT[sensorId][ADDR]
        elif sensorId in MAG_IDENTIFIER_DICT:
            return MAG_IDENTIFIER_DICT[sensorId][ADDR]
        elif sensorId == MUX:
            return I2C_DEVICES_LOOKUP_TABLE[MUX][ADDR]
        elif sensorId == ADC:
            return I2C_DEVICES_LOOKUP_TABLE[ADC][ADDR]
        elif sensorId == POWER:
            return I2C_DEVICES_LOOKUP_TABLE[POWER][ADDR]
        return None

    @staticmethod
    def subsystem(sensorId):
        """
        returns the subsytems corresponding to the sensorId
        that is passed as an argument.
        """
        if sensorId in TEMP_IDENTIFIER_DICT:
            return TEMP_IDENTIFIER_DICT[sensorId][SUB]
        elif sensorId in RTC_IDENTIFIER_DICT:
            return RTC_IDENTIFIER_DICT[sensorId][SUB]
        elif sensorId in GYRO_IDENTIFIER_DICT:
            return GYRO_IDENTIFIER_DICT[sensorId][SUB]
        elif sensorId in MAG_IDENTIFIER_DICT:
            return MAG_IDENTIFIER_DICT[sensorId][SUB]
        elif sensorId == ADC:
            return PAYLOAD 
        return None


    @staticmethod
    def addr_deprecated(sensor_type):
        """
        returns the i2c base address if the sensor_type passed is valid,
        else, return 'None' (do not use: see updated method)
        """
        if sensor_type in I2C_DEVICES_LIST:
            return I2C_DEVICES_LOOKUP_TABLE[sensor_type][ADDR]
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

    @staticmethod
    def get_specific_address(sensor_id):
        """
        returns the address for a specified sensor
        """
        if sensor_id in TEMP_IDENTIFIER_DICT:
            return TEMP_IDENTIFIER_DICT[id][ADDR]
        elif sensor_id in RTC_IDENTIFIER_DICT:
            return RTC_IDENTIFIER_DICT[id][ADDR]
        elif sensor_id in GYRO_IDENTIFIER_DICT:
            return GYRO_IDENTIFIER_DICT[id][ADDR]
        elif sensor_id in MAG_IDENTIFIER_DICT:
            return MAG_IDENTIFIER_DICT[id][ADDR]
        else:
            raise Exception('Sensor id does not exist')

    @staticmethod
    def get_gpio_pin(sensorId):
      """
      Returns the pin id for a gpio
      """
      if sensorId in GPIO_LOOKUP_TABLE:
        return GPIO_LOOKUP_TABLE[sensorId][PIN]
        
    def get_gpio_direction(sensorId):
      """
      Returns direction of gpio
      """
      if sensorId in GPIO_LOOKUP_TABLE:
        return GPIO_LOOKUP_TABLE[sensorId][DIR]

if __name__ == "__main__":
    for sensor in I2C_DEVICES_LIST:
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
        print("name: " + SensorEntropy.name(sensor))
        print("addr:" + str(SensorEntropy.addr(sensor)))
        print("reg:" + str(SensorEntropy.reg(sensor)))
        print("ch: " + str(SensorEntropy.ch(sensor)))
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
