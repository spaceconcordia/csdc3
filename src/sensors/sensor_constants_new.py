"""
File contains the constants used by the sensor modules.
"""

# Power sensor
INA219_PATH = "/sys/class/i2c-dev/i2c-0/device/i2c-dev/i2c-0/device/0-0040/hwmon/hwmon0/"
INA219_CURRENT = "/sys/class/i2c-dev/i2c-0/device/i2c-dev/i2c-0/device/0-0040/hwmon/hwmon0/curr1_input"
INA219_RESISTOR = "/sys/class/i2c-dev/i2c-0/device/i2c-dev/i2c-0/device/0-0040/hwmon/hwmon0/shunt_resistor"
INA219_VOLTAGE = "/sys/class/i2c-dev/i2c-0/device/i2c-dev/i2c-0/device/0-0040/hwmon/hwmon0/in1_input"
INA219_POWER = "/sys/class/i2c-dev/i2c-0/device/i2c-dev/i2c-0/device/0-0040/hwmon/hwmon0/power1_input"
I2C_DEVICE_PATH = "/sys/class/i2c-adapter/i2c-0/new_device"

# Analog-to-digital converter
SWITCH_CURRENT_PATH = "/sys/bus/iio/devices/iio:device0/"
PAYLOAD_SWITCH_ADC_ID = 0
RADIO_SWITCH_ADC_ID = 1

# Paths for locks
PAYLOAD_LOCK = "/root/csdc3/src/utils/payloadLock.tmp"
SENSOR_LOCK = "/root/csdc3/src/utils/sensorReadingLock.tmp"

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
I2C =        'I2C'
MUX =        'MUX'
SUB =        'SUBSYSTEM'

# GPIO Status
ON = 1
OFF = 0
DIR = 'direction'
PIN = 'pin'

# One Wire Addresses
PANEL0 = 'one_wire_panel0'
PANEL1 = 'one_wire_panel1'
PANEL2 = 'one_wire_panel2'
PANEL3 = 'one_wire_panel3'

SIDE_PANEL_ONE_WIRE_DICT = {
    PANEL0: '000001885520',
    PANEL1: '000001aaf87d',
    PANEL2: '000001aaf9e5',
    PANEL3: '000001aaf1cb'
}

# i2c devices
GYRO =       'Gyroscope'
MAG =        'Magnetometer'
RTC =        'Real-time Clock'
TEMP =       'Temperature Sensor'
MUX =        'I2C Multiplexer'
ADC =        'ADC Payload'
POWER =      'Power'
W1TEMP =     'One-Wire Thermistor'

PAYLOAD_MUX = 0x70
CDH_MUX = 0x71

# Unique Sensor Identifiers
ADC_0            =    'ADC'
TEMP_PAYLOAD_A   =    'TEMP_A'
TEMP_PAYLOAD_B   =    'TEMP_B'
TEMP_PAYLOAD_BRD =    'TEMP_PAYLOAD_BRD'
TEMP_PWR_BRD     =    'TEMP_PWR_BRD'
TEMP_BAT_1       =    'TEMP_BAT_1'
TEMP_BAT_2       =    'TEMP_BAT_2'
TEMP_BAT_3       =    'TEMP_BAT_3'
TEMP_BAT_4       =    'TEMP_BAT_4'
TEMP_EPS_BRD     =    'TEMP_EPS_BRD'
TEMP_CDH_BRD     =    'TEMP_CDH_BRD'
TEMP_PAYLOAD_CHASSIS = 'TEMP_PAYLOAD_CHASSIS'
TEMP_END_CAP     =    'TEMP_END_CAP'
RTC_0            =    'RTC_0'
RTC_1            =    'RTC_1'
GYRO_0           =    'GYRO_0'
GYRO_1           =    'GYRO_1'
GYRO_2           =    'GYRO_2'
MAG_0            =    'MAG_0'
MAG_1            =    'MAG_1'
MAG_2            =    'MAG_2'
POWER_0          =    'POWER'
RADIO_SWITCH     =    'RADIO_SWITCH'
PAYLOAD_SWITCH   =    'PAYLOAD_SWITCH'

# GPIO Identifiers
PSS_HTR_STAT_1_GPIO       = "PA27"
PSS_HTR_STAT_2_GPIO       = "PA26"
PSS_HTR_STAT_3_GPIO       = "PA25"
PSS_HTR_STAT_4_GPIO       = "PA24"
RADIO_TX_CURR_SENSE_GPIO  = "PB11"
PAYLOAD_CURR_SENSE_GPIO   = "PB12"
PSS_HTR_MUX_SEL_GPIO      = "PA7"
I2C_MUX_RESET_GPIO        = "PA28"
DEPLOYMENT_SW_A_GPIO      = "PA22"
DEPLOYMENT_SW_B_GPIO      = "PA21"
RADIO_EN_GPIO             = "PA5"
PAYLOAD_EN_GPIO           = "PC3"
PSS_HTR_EN_1_GPIO         = "PC4"
PSS_HTR_EN_2_GPIO         = "PC28"
PSS_HTR_EN_3_GPIO         = "PA6"
PSS_HTR_EN_4_GPIO         = "PA8"
WATCHDOG_GPIO             = "PA23"
PAYLOAD_HTR_A_GPIO = "PB14"
PAYLOAD_HTR_B_GPIO = "PB13"
SENSORS_EN_GPIO = "PC27"
RTC_INT_GPIO = "PC31"
ADC_INT_GPIO = "PA29"
"""
---- New CDH PCB ----
"""

GPIO_LOOKUP_TABLE = {
	PSS_HTR_STAT_1_GPIO: {DIR: INPUT, PIN: 'J4.17'},
	PSS_HTR_STAT_2_GPIO: {DIR: INPUT, PIN: 'J4.15'},
	PSS_HTR_STAT_3_GPIO: {DIR: INPUT, PIN: 'J4.13'},
	PSS_HTR_STAT_4_GPIO: {DIR: INPUT, PIN: 'J4.11'},
	RADIO_TX_CURR_SENSE_GPIO: {DIR: INPUT, PIN: 'J4.34'},
	PAYLOAD_CURR_SENSE_GPIO: {DIR: INPUT, PIN: 'J4.36'},

	PSS_HTR_MUX_SEL_GPIO: {DIR: OUTPUT, PIN: 'J4.26'},
	I2C_MUX_RESET_GPIO: {DIR: OUTPUT, PIN: 'J4.19'},
	DEPLOYMENT_SW_A_GPIO: {DIR: OUTPUT, PIN: 'J4.8'},
	DEPLOYMENT_SW_B_GPIO: {DIR: OUTPUT, PIN: 'J4.10'},
	RADIO_EN_GPIO: {DIR: OUTPUT, PIN: 'J4.28'},
	PAYLOAD_EN_GPIO: {DIR: OUTPUT, PIN: 'J4.33'},
	PSS_HTR_EN_1_GPIO: {DIR: OUTPUT, PIN: 'J4.31'},
	PSS_HTR_EN_2_GPIO: {DIR: OUTPUT, PIN: 'J4.29'},
	PSS_HTR_EN_3_GPIO: {DIR: OUTPUT, PIN: 'J4.27'},
	PSS_HTR_EN_4_GPIO: {DIR: OUTPUT, PIN: 'J4.25'},
	WATCHDOG_GPIO: {DIR: OUTPUT, PIN: 'J4.7'},
  SENSORS_EN_GPIO: {DIR: OUTPUT, PIN: 'J4.30'},
  PAYLOAD_HTR_A_GPIO: {DIR: OUTPUT, PIN: 'J4.40'},
  PAYLOAD_HTR_B_GPIO: {DIR: OUTPUT, PIN: 'J4.38'},
  RTC_INT_GPIO : {DIR: OUTPUT, PIN: 'J4.32'},
  ADC_INT_GPIO : {DIR: OUTPUT, PIN: 'J4.21'}
}

# Subsystems
PAYLOAD =    'payload'
CDH =        'cdh'
SOFTWARE =   'software'
ACS = 		   'acs'

TEMP_IDENTIFIER_DICT = {
    TEMP_PAYLOAD_A: {I2C: 1, MUX: PAYLOAD_MUX, CH: 0, SUB: PAYLOAD, ADDR: 0x48},
    TEMP_PAYLOAD_B: {I2C: 1, MUX: PAYLOAD_MUX, CH: 0, SUB: PAYLOAD, ADDR: 0x49},
    TEMP_PAYLOAD_BRD: {I2C: 0, MUX: PAYLOAD_MUX, CH: 4, SUB: PAYLOAD, ADDR: 0x48},
    TEMP_PAYLOAD_CHASSIS: {I2C: 0, MUX: PAYLOAD_MUX, CH: 1, SUB: PAYLOAD, ADDR: 0x4d},
    TEMP_END_CAP: {I2C: 0, MUX: PAYLOAD_MUX, CH: 1, SUB: POWER, ADDR: 0x4c},
    TEMP_BAT_1: {I2C: 0, MUX: CDH_MUX, CH: 4, SUB: POWER, ADDR: 0x4e},
    TEMP_BAT_2: {I2C: 0, MUX: CDH_MUX, CH: 4, SUB: POWER, ADDR: 0x4f},
    TEMP_BAT_3: {I2C: 0, MUX: CDH_MUX, CH: 4, SUB: POWER, ADDR: 0x4a},
    TEMP_BAT_4: {I2C: 0, MUX: CDH_MUX, CH: 4, SUB: POWER, ADDR: 0x4b},
    TEMP_EPS_BRD: {I2C: 0, MUX: CDH_MUX, CH: 4, SUB: POWER, ADDR: 0x4c},
    TEMP_CDH_BRD: {I2C: 0, MUX: CDH_MUX, CH: 4, SUB: CDH, ADDR: 0x4d}
}

RTC_IDENTIFIER_DICT = {
    RTC_0: {I2C: 0, MUX: None, CH: None, SUB: CDH, ADDR: 0x68},
    RTC_1: {I2C: 1, MUX: None, CH: None, SUB: CDH, ADDR: 0x68}
}

GYRO_IDENTIFIER_DICT = {
    GYRO_0: {I2C: 0, MUX: 0x71, CH: 1, SUB: ACS, ADDR: 0x68},
    GYRO_1: {I2C: 0, MUX: 0x71, CH: 1, SUB: ACS, ADDR: 0x68},
    GYRO_2: {I2C: 0, MUX: 0x71, CH: 1, SUB: ACS, ADDR: 0x68}
}

MAG_IDENTIFIER_DICT = {
    MAG_0: {I2C: 0, MUX: 0x71, CH: 1, SUB: ACS, ADDR: 0x1E},
    MAG_1: {I2C: 0, MUX: 0x71, CH: 2, SUB: ACS, ADDR: 0x1E},
    MAG_2: {I2C: 0, MUX: 0x71, CH: 3, SUB: ACS, ADDR: 0x1E}
}

I2C_DEVICES_LIST = [GYRO, MAG, RTC, TEMP, MUX, ADC, POWER]

I2C_DEVICES_LOOKUP_TABLE = {
    GYRO: {
        NAME: 'ITG3400',
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
        NAME: 'DS3232',
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
        CH: []
    },
    MUX: {
        NAME: 'TCA9548A',
        ADDR: 0x70,
        REG: {},
        CH: [0]
    },
    ADC: {
        NAME: 'AD128D818',
        ADDR: 0x1D,
        MUX: 0x70,
        REG: {
            'REG_CONFIG'          : 0x00,
            'REG_CONV_RATE'       : 0x07,
            'REG_CHANNEL_DISABLE' : 0x08,
            'REG_ADV_CONFIG'      : 0x0B,
            'REG_BUSY_STATUS'     : 0x0C,
            'READ_REG_BASE'       : 0x20,
            'REG_LIMIT_BASE'      : 0x2A,
            'REG_LIMIT_BASE2'     : 0x2C,
            'REG_TEMP'            : 0x27,
            'CONFIG_INTERNAL_VREF': 0x04,
            'CONFIG_EXTERNAL_VREF': 0x05,
            'CONFIG_LIMIT_BASE'   : 0x05,
            'CONFIG_CONTINUOUS'   : 0x01,
            'CONFIG_ENABLE_ALL_CHANNELS'   : 0x0,
            'CONFIG_NO_INTERRUPTS': 0x01
        },
        CH: [0]
    },
    POWER: {
        NAME: 'INA219',
        ADDR: 0x40,
        MUX: 0x71,
        CH: [4]
    }
}
