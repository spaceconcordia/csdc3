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
W1TEMP =     'One-Wire Thermistor'

# Unique Sensor Identifiers
ADC_0 = 'I2C0_mux1_ch0_1D'
TEMP_0 = 'I2C0_mux1_ch0_48'
TEMP_1 = 'I2C0_mux1_ch0_49'
TEMP_2 = 'I2C0_mux1_ch1_48'
TEMP_3 = 'I2C0_mux1_ch4_49'
TEMP_4 = 'I2C0_mux0_ch4_48'
TEMP_5 = 'I2C0_mux0_ch4_49'
TEMP_6 = 'I2C0_mux0_ch4_4a'
TEMP_7 = 'I2C0_mux0_ch4_4b'
TEMP_8 = 'I2C0_mux0_ch4_4c'
TEMP_9 = 'I2C0_mux0_ch4_4d'
RTC_0 = 'I2C0_mux0_ch0_68'
RTC_1 = 'I2C1_68'
GYRO_0 = 'I2C0_mux0_ch1_68'
GYRO_1 = 'I2C0_mux0_ch2_68'
GYRO_2 = 'I2C0_mux0_ch3_68'
MAG_0 = 'I2C0_mux0_ch1_1E'
MAG_1 = 'I2C0_mux0_ch2_1E'
MAG_2 = 'I2C0_mux0_ch3_1E'
POWER_0 = 'I2C0_mux0_ch4_0'

TEMP_IDENTIFIER_LIST = [TEMP_0, TEMP_1, TEMP_2, TEMP_3, \
TEMP_4, TEMP_5, TEMP_6, TEMP_7, TEMP_8, TEMP_9]
RTC_IDENTIFIER_LIST = [RTC_0, RTC_1]
GYRO_IDENTIFIER_LIST = [GYRO_0, GYRO_1, GYRO_2]
MAG_IDENTIFIER_LIST = [MAG_0, MAG_1, MAG_2]

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
			      STOP: 0x22,
            CONFIG: 0xAC
        },
        CH: [0, 1, 2, 3, 4, 5, 6]
    },
    W1TEMP: {
        NAME: "DS18B20",
        ADDR: 0x48,
        REG: {
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
