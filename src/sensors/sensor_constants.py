"""
File contains the constants used by the different parts of the project.
"""

# different sensor classes (Range: 0x00 - 0x02)
I2C =        0x00
GPIO =       0x01
ONE_WIRE =   0x02

# I/O const
INPUT =      'INPUT'
OUTPUT =     'OUTPUT'

# i2c devices type names as strings
GYRO =       'Gyroscope'
MAG =        'Magnetometer'
RTC =        'Real-time Clock'
TEMP =       'Temperature Sensor'
MUX =        'I2C Multiplexer'
ADC =        'ADC Payload'
POWER =      'Power Sensor'

I2C_DEVICES_LIST = [GYRO, MAG, RTC, TEMP, MUX, ADC, POWER]

I2C_LOOKUP_TABLE = {
    GYRO: {
       "name": "ITG3205",
       "address": 0x68,
       "register": 
       "quantity": 3,
       "channels": [0, 1, 2]
    },
    MAG: {
       "name": "HMC5883L",
       "address": 0x1e,
       "quantity": 3,
       "channels": [0, 1, 2]
    },
    RTC: {
       "name": "DS3231",
       "address": 0x68,
       "quantity": 2,
       "channels": [3, 4]
    },
    TEMP: {
       "name": "DS1624",
       "address": 0x48,
       "quantity": 7,
       "channels": [0, 1, 2, 3, 4, 5, 6, 7]
    },
    MUX: {
       "name": "TCA9548A",
       "address": 0x70,
       "quantity": 1,
       "channels": [0]
    },
    ADC: {
       "name": "AD128d818",
       "address": 0x1D,
       "quantity": 1,
       "channels": [0]
    },
    POWER: {
       "name": "INA219",
       "address": -1,
       "quantity": -1,
       "channels": [-1]
    }
}
