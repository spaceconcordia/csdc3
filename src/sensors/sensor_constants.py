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

# i2c devices

GYRO =       'Gyroscope'
MAG =        'Magnetometer'
RTC =        'Real-time Clock'
TEMP =       'Temperature Sensor'
MUX =        'I2C Multiplexer'
ADC =        'ADC Payload'
POWER =      'Power Sensor'

I2C_DEVICES_LIST = [GYRO, MAG, RTC, TEMP, MUX, ADC, POWER]

I2C_DEVICES_LOOKUP_TABLE = {
    GYRO: {
        'name': 'ITG3205',
        'addr': 0x68,
        'reg': {
            'X-H': 0x1D,
            'X-L': 0x1E,
            'Y-H': 0x1F,
            'Y-L': 0x20,
            'Z-H': 0x21,
            'Z-L': 0x22
        },
        'ch': [0, 1, 2]
    },
    MAG: {
        'name': 'HMC5883L',
        'addr': 0x1e,
        'reg': {
            'INIT': 0x02,
            'X-H': 0x03,
            'X-L': 0x04,
            'Y-H': 0x05,
            'Y-L': 0x06,
            'Z-H': 0x07,
            'Z-L': 0x08
        },
        'ch': [0, 1, 2]
    },
    RTC: {
        'name': 'DS3231',
        'addr': 0x68,
        'reg': {
            'sec':   0x00,
            'min':   0x01,
            'hr':    0x02,
            'day':   0x03,
            'date':  0x04,
            'month': 0x05,
            'year':  0x07
        },
        'ch': [3, 4]
    },
    TEMP: {
        'name': "DS1624",
        'addr': 0x48,
        'reg': 0xAA,
        'ch': [0, 1, 2, 3, 4, 5, 6]
    },
    MUX: {
        'name': 'TCA9548A',
        'addr': 0x70,
        'reg': {},
        'ch': [0]
    },
    ADC: {
        'name': 'AD128d818',
        'addr': 0x1D,
        'reg': {},
        'ch': []
    },
    POWER: {
        'name': 'N/A',
        'addr': -1,
        'reg': {},
        'ch': []
    }
}
