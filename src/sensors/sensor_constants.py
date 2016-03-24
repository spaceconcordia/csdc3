"""
File contains the constants used by the sensor modules.
"""

#TODO rename this
INA219_PATH = "/sys/class/i2c-dev/i2c-0/device/i2c-dev/i2c-0/device/0-0040/hwmon/hwmon0/"
INA219_CURRENT = "/sys/class/i2c-dev/i2c-0/device/i2c-dev/i2c-0/device/0-0040/hwmon/hwmon0/curr1_input"
INA219_RESISTOR = "/sys/class/i2c-dev/i2c-0/device/i2c-dev/i2c-0/device/0-0040/hwmon/hwmon0/shunt_resistor"
INA219_VOLTAGE = "/sys/class/i2c-dev/i2c-0/device/i2c-dev/i2c-0/device/0-0040/hwmon/hwmon0/in1_input"
INA219_POWER = "/sys/class/i2c-dev/i2c-0/device/i2c-dev/i2c-0/device/0-0040/hwmon/hwmon0/power1_input"
I2C_DEVICE_PATH = "/sys/class/i2c-adapter/i2c-0/new_device"

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
ON = 'on'
OFF = 'off'
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
POWER =      'Power Sensor'
W1TEMP =     'One-Wire Thermistor'

# Unique Sensor Identifiers
ADC_0 =      'I2C0_mux1_ch0_1D'
TEMP_PAYLOAD_A =     'I2C0_mux1_ch0_48'
TEMP_PAYLOAD_B =     'I2C0_mux1_ch0_49'
TEMP_PAYLOAD_BRD =     'I2C0_mux1_ch1_48'
TEMP_PWR_BRD =     'I2C0_mux1_ch4_49'
TEMP_BAT_1 =     'I2C0_mux0_ch4_48'
TEMP_BAT_2 =     'I2C0_mux0_ch4_49'
TEMP_BAT_3 =     'I2C0_mux0_ch4_4a'
TEMP_BAT_4 =     'I2C0_mux0_ch4_4b'
TEMP_EPS_BRD =     'I2C0_mux0_ch4_4c'
TEMP_CDH_BRD =     'I2C0_mux0_ch4_4d'
RTC_0 =      'I2C0_mux0_ch0_68'
RTC_1 =      'I2C1_68'
GYRO_0 =     'I2C0_mux0_ch1_68'
GYRO_1 =     'I2C0_mux0_ch2_68'
GYRO_2 =     'I2C0_mux0_ch3_68'
MAG_0 =      'I2C0_mux0_ch1_1E'
MAG_1 =      'I2C0_mux0_ch2_1E'
MAG_2 =      'I2C0_mux0_ch3_1E'
POWER_0 =    'I2C0_mux0_ch4_0'

# GPIO Identifiers
PSS_HTR_STAT_1_GPIO = "PA27"
PSS_HTR_STAT_2_GPIO = "PA26"
PSS_HTR_STAT_3_GPIO = "PA25"
PSS_HTR_STAT_4_GPIO = "PA24"
RADIO_TX_CURR_SENSE_GPIO = "PB11"
PAYLOAD_CURR_SENSE_GPIO = "PB12"
PSS_HTR_MUX_SEL_GPIO = "PA7"
I2C_MUX_RESET_GPIO = "PA28"
DEPLOYMENT_SW_A_GPIO = "PA22"
DEPLOYMENT_SW_B_GPIO = "PA21"
RADIO_EN_GPIO = "PA5"
PAYLOAD_HTR_A_GPIO = "PC31"
PAYLOAD_HTR_B_GPIO = "PC27"
PAYLOAD_EN_GPIO = "PB13"
PSS_HTR_EN_1_GPIO = "PC4"
PSS_HTR_EN_2_GPIO = "PC28"
PSS_HTR_EN_3_GPIO = "PA6"
PSS_HTR_EN_4_GPIO = "PA8"
WATCHDOG_GPIO = "PA23"
SENSORS_EN_GPIO = "PB14"

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
	PAYLOAD_HTR_A_GPIO: {DIR: OUTPUT, PIN: 'J4.32'},
	PAYLOAD_HTR_B_GPIO: {DIR: OUTPUT, PIN: 'J4.30'},
	PAYLOAD_EN_GPIO: {DIR: OUTPUT, PIN: 'J4.38'},
	PSS_HTR_EN_1_GPIO: {DIR: OUTPUT, PIN: 'J4.31'},
	PSS_HTR_EN_2_GPIO: {DIR: OUTPUT, PIN: 'J4.29'},
	PSS_HTR_EN_3_GPIO: {DIR: OUTPUT, PIN: 'J4.27'},
	PSS_HTR_EN_4_GPIO: {DIR: OUTPUT, PIN: 'J4.25'},
	WATCHDOG_GPIO: {DIR: OUTPUT, PIN: 'J4.7'},
	SENSORS_EN_GPIO: {DIR: OUTPUT, PIN: 'J4.40'}
}

# Subsystems
PAYLOAD =    'payload'
CDH =        'cdh'
POWER =      'power'
SOFTWARE =   'software'
ACS = 		   'acs'
POWER =      'power'

TEMP_IDENTIFIER_DICT = {
    TEMP_PAYLOAD_A: {I2C: 0, MUX: 0x70, CH: 0, SUB: PAYLOAD, ADDR: 0x48},
    TEMP_PAYLOAD_B: {I2C: 0, MUX: 0x70, CH: 0, SUB: PAYLOAD, ADDR: 0x49},
    TEMP_PAYLOAD_BRD: {I2C: 0, MUX: 0x70, CH: 4, SUB: PAYLOAD, ADDR: 0x48},
    TEMP_PWR_BRD: {I2C: 0, MUX: 0x70, CH: 4, SUB: POWER, ADDR: 0x49},
    TEMP_BAT_1: {I2C: 0, MUX: 0x71, CH: 4, SUB: POWER, ADDR: 0x48},
    TEMP_BAT_2: {I2C: 0, MUX: 0x71, CH: 4, SUB: POWER, ADDR: 0x49},
    TEMP_BAT_3: {I2C: 0, MUX: 0x71, CH: 4, SUB: POWER, ADDR: 0x4a},
    TEMP_BAT_4: {I2C: 0, MUX: 0x71, CH: 4, SUB: POWER, ADDR: 0x4b},
    TEMP_EPS_BRD: {I2C: 0, MUX: 0x71, CH: 4, SUB: POWER, ADDR: 0x4c},
    TEMP_CDH_BRD: {I2C: 0, MUX: 0x71, CH: 4, SUB: CDH, ADDR: 0x4d}
}

RTC_IDENTIFIER_DICT = {
    RTC_0: {I2C: 0, MUX: 0x71, CH: 0, SUB: CDH, ADDR: 0x68},
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
        REG: {
            'REG_CONFIG'                      : 0x00,
            'REG_SHUNTVOLTAGE'                : 0x01,
            'REG_BUSVOLTAGE'                  : 0x02,
            'REG_POWER'                       : 0x03,
            'REG_CURRENT'                     : 0x04,
            'REG_CALIBRATION'                 : 0x05,

	        'CONFIG_RESET'                    : 0x8000,  # Reset Bit
	        'CONFIG_BVOLTAGERANGE_MASK'       : 0x2000,  # Bus Voltage Range Mask
	        'CONFIG_BVOLTAGERANGE_16V'        : 0x0000,  # 0-16V Range
	        'CONFIG_BVOLTAGERANGE_32V'        : 0x2000,  # 0-32V Range

	        'CONFIG_GAIN_MASK'                : 0x1800,  # Gain Mask
	        'CONFIG_GAIN_1_40MV'              : 0x0000,  # Gain 1, 40mV Range
	        'CONFIG_GAIN_2_80MV'              : 0x0800,  # Gain 2, 80mV Range
	        'CONFIG_GAIN_4_160MV'             : 0x1000,  # Gain 4, 160mV Range
	        'CONFIG_GAIN_8_320MV'             : 0x1800,  # Gain 8, 320mV Range

	        'CONFIG_BADCRES_MASK'             : 0x0780,  # Bus ADC Resolution Mask
	        'CONFIG_BADCRES_9BIT'             : 0x0080,  # 9-bit bus res : 0..511
	        'CONFIG_BADCRES_10BIT'            : 0x0100,  # 10-bit bus res : 0..1023
	        'CONFIG_BADCRES_11BIT'            : 0x0200,  # 11-bit bus res : 0..2047
	        'CONFIG_BADCRES_12BIT'            : 0x0400,  # 12-bit bus res : 0..4097

	        'CONFIG_SADCRES_MASK'             : 0x0078,  # Shunt ADC Resolution and Averaging Mask
	        'CONFIG_SADCRES_9BIT_1S_84US'     : 0x0000,  # 1 x 9-bit shunt sample
	        'CONFIG_SADCRES_10BIT_1S_148US'   : 0x0008,  # 1 x 10-bit shunt sample
	        'CONFIG_SADCRES_11BIT_1S_276US'   : 0x0010,  # 1 x 11-bit shunt sample
	        'CONFIG_SADCRES_12BIT_1S_532US'   : 0x0018,  # 1 x 12-bit shunt sample
	        'CONFIG_SADCRES_12BIT_2S_1060US'  : 0x0048,  # 2 x 12-bit shunt samples averaged together
	        'CONFIG_SADCRES_12BIT_4S_2130US'  : 0x0050,  # 4 x 12-bit shunt samples averaged together
	        'CONFIG_SADCRES_12BIT_8S_4260US'  : 0x0058,  # 8 x 12-bit shunt samples averaged together
	        'CONFIG_SADCRES_12BIT_16S_8510US' : 0x0060,  # 16 x 12-bit shunt samples averaged together
	        'CONFIG_SADCRES_12BIT_32S_17MS'   : 0x0068,  # 32 x 12-bit shunt samples averaged together
	        'CONFIG_SADCRES_12BIT_64S_34MS'   : 0x0070,  # 64 x 12-bit shunt samples averaged together
	        'CONFIG_SADCRES_12BIT_128S_69MS'  : 0x0078,  # 128 x 12-bit shunt samples averaged together

	        'CONFIG_MODE_MASK'                : 0x0007,  # Operating Mode Mask
	        'CONFIG_MODE_POWERDOWN'           : 0x0000,
	        'CONFIG_MODE_SVOLT_TRIGGERED'     : 0x0001,
	        'CONFIG_MODE_BVOLT_TRIGGERED'     : 0x0002,
	        'CONFIG_MODE_SANDBVOLT_TRIGGERED' : 0x0003,
	        'CONFIG_MODE_ADCOFF'              : 0x0004,
	        'CONFIG_MODE_SVOLT_CONTINUOUS'    : 0x0005,
	        'CONFIG_MODE_BVOLT_CONTINUOUS'    : 0x0006,
	        'CONFIG_MODE_SANDBVOLT_CONTINUOUS': 0x0007
	    },
        CH: [4]
    }
}
