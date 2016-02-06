"""
File contains the constants used by the sensor modules.
"""

# different sensor classes (Range: 0x00 - 0x02)
I2C =        0x00
GPIO =       0x01
ONE_WIRE =   0x02

# i/o, i2c devices literals
INPUT =      'INPUT'
OUTPUT =     'OUTPUT'
NAME =       'NAME'
ADDR =       'BASE_ADDR'
REG =        'REGISTERS'
CH =         'CHANNELS'
VAL =        'VALUE'
START =      'START'
STOP =       'STOP'
CONFIG =     'CONFIG'

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
        NAME: 'ITG3205',
        ADDR: 0x68,
        REG: {
            'X-H': 0x1D,
            'X-L': 0x1E,
            'Y-H': 0x1F,
            'Y-L': 0x20,
            'Z-H': 0x21,
            'Z-L': 0x22
        },
        CH: [0, 1, 2]
    },
    MAG: {
        NAME: 'HMC5883L',
        ADDR: 0x1E,
        REG: {
            'INIT': 0x02,
            'X-H': 0x03,
            'X-L': 0x04,
            'Y-H': 0x05,
            'Y-L': 0x06,
            'Z-H': 0x07,
            'Z-L': 0x08
        },
        CH: [0, 1, 2]
    },
    RTC: {
        NAME: 'DS3231',
        ADDR: 0x68,
        REG: {
            'sec':   0x00,
            'min':   0x01,
            'hr':    0x02,
            'day':   0x03,
            'date':  0x04,
            'month': 0x05,
            'year':  0x07
        },
        CH: [3, 4]
    },
    TEMP: {
        NAME: "DS1624",
        ADDR: 0x48,
        REG: {
            VAL: 0xAA,
            START: 0xEE,
            CONFIG: 0xAC
        },
        CH: [0, 1, 2, 3, 4, 5, 6]
    },
    MUX: {
        NAME: 'TCA9548A',
        ADDR: 0x70,
        REG: {},
        CH: [0]
    },
    ADC: {
        NAME: 'AD128d818',
        ADDR: 0x1D,
        REG: {
            'CONFIG_REG'          : 0x00,
            'CONV_RATE_REG'       : 0x07,
            'CHANNEL_DISABLE_REG' : 0x08,
            'ADV_CONFIG_REG'      : 0x0B,
            'BUSY_STATUS_REG'     : 0x0C,
            'READ_REG_BASE'       : 0x20,
            'LIMIT_REG_BASE'      : 0x2A,
            'LIMIT_REG_BASE2'     : 0x2C,
            'TEMP_REGISTER'       : 0x27
        },
        CH: [0]
    },
    POWER: {
        NAME: 'N/A',
        ADDR: -1,
        REG: {},
        CH: []
    }
}
