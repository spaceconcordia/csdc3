import sys
sys.path.append('/root/csdc3/lib/ablib')
sys.path.append('/root/csdc3/src/logs')
sys.path.append('/root/csdc3/src/logs/config_setup')
sys.path.append("/root/csdc3/src/utils")
from ablib import Pin
from ablib import DS18B20
from chomsky import *
from time import sleep
from sensor_entropy import *
from sensor_constants import *
import smbus
import time
from SharedLock import Lock
import utility

class SensorManager:

    bus = smbus.SMBus(0)
    payloadbus = smbus.SMBus(1)
    active_gpio_pins = {}
    channel = None
    old_mux = None
    # sensorReadingLock = Lock("/root/csdc3/src/utils/sensorReadingLock.tmp")

    """ -------------------- Initialization --------------------- """

    @staticmethod
    def init_gyroscope(sensorId):
        # SensorManager.sensorReadingLock.acquire()

        insertDebugLog(NOTICE, "Initialized gyroscope: {}".format(sensorId),
        CDH, int(time.time()))

        if not SensorManager.isCorrectSensor(sensorId, GYRO):
            raise Exception('Incorrect sensor specified')

        SensorManager.mux_select(sensorId)

        try:
            SensorManager.bus.write_byte(SensorEntropy.addr(sensorId), 0x00)
        except(IOError, OSError):
            print('[INIT] Error writing to gyroscope at address ' + \
                str(SensorEntropy.addr(sensorId)))
            insertDebugLog(NOTICE, "[INIT] Error writing to gyroscope: {}".format(sensorId),
            CDH, int(time.time()))
            return None
        time.sleep(0.1)

    @staticmethod
    def init_magnetometer(sensorId):
        # SensorManager.sensorReadingLock.acquire()

        insertDebugLog(NOTICE, "Initialized magnetometer: {}".format(sensorId),
        CDH, int(time.time()))

        if not SensorManager.isCorrectSensor(sensorId, MAG):
            raise Exception('Incorrect sensor specified')

        mag_reg = SensorEntropy.reg(MAG)
        SensorManager.mux_select(sensorId)

        try:
            SensorManager.bus.write_byte_data(SensorEntropy.addr(sensorId), \
            mag_reg['INIT'], 0x01)
        except(IOError, OSError):
            print('[INIT] Error writing to magnetometer at address ' + \
                str(SensorEntropy.addr(sensorId)))
            insertDebugLog(NOTICE, "[INIT] Error writing to magnetometer: {}".format(sensorId),
            CDH, int(time.time()))
            return None
        time.sleep(0.1)

    @staticmethod
    def init_rtc():
        pass

    @staticmethod
    def init_temp_sensor(sensorId):
        # SensorManager.sensorReadingLock.acquire()

        insertDebugLog(NOTICE, "Initialized temp sensor: {}".format(sensorId),
        CDH, int(time.time()))

        if not SensorManager.isCorrectSensor(sensorId, TEMP):
            print('Sensor Id: ' + str(sensorId))
            raise Exception('Incorrect sensor specified')

        addr = SensorEntropy.addr(sensorId)
        reg = SensorEntropy.reg(TEMP)

        if sensorId == TEMP_PAYLOAD_A or sensorId == TEMP_PAYLOAD_B:
            bus = SensorManager.payloadbus

        else:
            SensorManager.mux_select(sensorId)
            bus = SensorManager.bus

        try:
            # Start data conversion
            startReg = reg[START]
            configReg = reg[CONFIG]
            bus.write_byte_data(addr, startReg, 0x01)
            # Enable continuous mode
            bus.write_byte_data(addr, configReg, 0x00)
        except(IOError, OSError):
            print("[INIT] Error writing to temperature sensor: {}".format(sensorId))
            insertDebugLog(NOTICE, "[INIT] Error writing to temperature sensor: {}".format(sensorId),
             CDH, int(time.time()))
            return None
        time.sleep(0.1)

    @staticmethod
    def init_adc(sensorId):
        # SensorManager.sensorReadingLock.acquire()

        insertDebugLog(NOTICE, "Initialized ADC: {}".format(sensorId),
        CDH, int(time.time()))

        bus = SensorManager.payloadbus

        addr = SensorEntropy.addr(sensorId)
        adc_reg = SensorEntropy.reg(ADC)
        busy_reg = bus.read_byte_data(addr, \
                                adc_reg['REG_BUSY_STATUS'])
        """
        while busy_reg:
            time.sleep(1)
        """
        try:
            bus.write_byte_data(addr, adc_reg['REG_ADV_CONFIG'], \
                                      adc_reg['CONFIG_EXTERNAL_VREF'])
            bus.write_byte_data(addr, adc_reg['REG_CONV_RATE'], \
                                      adc_reg['CONFIG_CONTINUOUS'])
            bus.write_byte_data(addr, adc_reg['REG_CHANNEL_DISABLE'], \
                                      adc_reg['CONFIG_ENABLE_ALL_CHANNELS'])
            bus.write_byte_data(addr, adc_reg['REG_LIMIT_BASE'], \
                                      adc_reg['CONFIG_LIMIT_BASE'])
            bus.write_byte_data(addr, adc_reg['REG_LIMIT_BASE2'], \
                                      adc_reg['CONFIG_LIMIT_BASE'])
            bus.write_byte_data(addr, adc_reg['REG_CONFIG'], \
                                      adc_reg['CONFIG_NO_INTERRUPTS'])
        except(IOError, OSError):
            print('[INIT] Error writing to ADC at address ' + str(addr))
            insertDebugLog(NOTICE, "[INIT] Error writing to ADC: {}".format(sensorId),
            CDH, int(time.time()))
            return None

    @staticmethod
    def init_power_sensor(sensorId):
        # SensorManager.sensorReadingLock.acquire()

        insertDebugLog(NOTICE, "Initialized power sensor: {}".format(sensorId),
        CDH, int(time.time()))
        SensorManager.mux_select(sensorId)

        try:
            if not os.path.isdir(INA219_PATH):
                with open(I2C_DEVICE_PATH, "w") as f:
                    f.write("ina219 0x40")

            with open(INA219_RESISTOR, "w") as f:
                f.write("2000")

        except(IOError, OSError):
            print('[INIT] Error reading from Power sensor')
            insertDebugLog(NOTICE, "[INIT] Error reading from Power sensor: {}".format(sensorId),
            CDH, int(time.time()))
        return None

    """ -------------------- Stop --------------------- """

    @staticmethod
    def stop_gyroscope(sensorId):
        insertDebugLog(NOTICE, "Stop gyroscope: {}".format(sensorId),
        CDH, int(time.time()))

        if not SensorManager.isCorrectSensor(sensorId, GYRO):
            raise Exception('Incorrect sensor specified')

        SensorManager.mux_select(sensorId)
        addr = SensorEntropy.addr(sensorId)

        try:
            SensorManager.bus.write_byte(addr, 0x01)
        except(IOError, OSError):
            print('[STOP] Error writing to gyroscope at address ' + str(addr))
            insertDebugLog(NOTICE, "[STOP] Error writing to gyroscope: {}".format(sensorId),
            CDH, int(time.time()))
            return None
        # finally:
        #     SensorManager.sensorReadingLock.release()
        time.sleep(0.1)

    @staticmethod
    def stop_magnetometer(sensorId):
        insertDebugLog(NOTICE, "Stop magnetometer: {}".format(sensorId),
        CDH, int(time.time()))
        # SensorManager.sensorReadingLock.release()

    @staticmethod
    def stop_temp_sensor(sensorId):
        insertDebugLog(NOTICE, "Stop temp sensor: {}".format(sensorId),
        CDH, int(time.time()))

        if not SensorManager.isCorrectSensor(sensorId, TEMP):
            raise Exception('Incorrect sensor specified')

        addr = SensorEntropy.addr(sensorId)
        stopReg = SensorEntropy.reg(TEMP)[STOP]
        if sensorId == TEMP_PAYLOAD_A or sensorId == TEMP_PAYLOAD_B:
            bus = SensorManager.payloadbus
        else:
            SensorManager.mux_select(sensorId)
            bus = SensorManager.bus

        try:
            bus.write_byte_data(addr, stopReg, 0x01)
        except(IOError, OSError):
            print('[STOP] Error writing to temperature sensor at address ' + str(addr))
            insertDebugLog(NOTICE, "[STOP] Error writing to temperature sensor: {}".format(sensorId),
            CDH, int(time.time()))
            return None
        # finally:
        #     SensorManager.sensorReadingLock.release()

    @staticmethod
    def stop_adc_sensor(sensorId):
        insertDebugLog(NOTICE, "Stop adc: {}".format(sensorId),
        CDH, int(time.time()))

        SensorManager.mux_select(sensorId)
        addr = SensorEntropy.addr(sensorId)
        configReg = SensorEntropy.reg(ADC)['REG_CONFIG']

        try:
            SensorManager.payloadbus.write_byte_data(addr, configReg, 0x00)
        except (IOError, OSError):
            print('[STOP] Error writing to ADC at address ' + str(addr))
            insertDebugLog(NOTICE, "[STOP] Error writing to ADC: {}".format(sensorId),
            CDH, int(time.time()))
            return None
        # finally:
        #     SensorManager.sensorReadingLock.release()

    @staticmethod
    def stop_rtc(sensorId):
        pass

    @staticmethod
    def stop_power_sensor(sensorId):
        insertDebugLog(NOTICE, "Stop power sensor: {}".format(sensorId),
        CDH, int(time.time()))
        # SensorManager.sensorReadingLock.release()

    """ -------------------- Reading --------------------- """

    @staticmethod
    def read_gyroscope(sensorId):
        insertDebugLog(NOTICE, "Read gyroscope: {}".format(sensorId),
        CDH, int(time.time()))

        if not SensorManager.isCorrectSensor(sensorId, GYRO):
            raise Exception('Incorrect sensor specified')
        SensorManager.mux_select(sensorId)
        address = SensorEntropy.addr(sensorId)
        gyro_reg = SensorEntropy.reg(GYRO)

        # Get the values from the sensor
        reg_x_h = gyro_reg['X-H']
        reg_x_l = gyro_reg['X-L']
        reg_y_h = gyro_reg['Y-H']
        reg_y_l = gyro_reg['Y-L']
        reg_z_h = gyro_reg['Z-H']
        reg_z_l = gyro_reg['Z-L']

        try:
            valX = (SensorManager.bus.read_byte_data(address, reg_x_h) << 8) \
            | SensorManager.bus.read_byte_data(address, reg_x_l)
            sleep(0.1)
            valY = (SensorManager.bus.read_byte_data(address, reg_y_h) << 8) \
            | SensorManager.bus.read_byte_data(address, reg_y_l)
            sleep(0.1)
            valZ = (SensorManager.bus.read_byte_data(address, reg_z_h) << 8) \
            | SensorManager.bus.read_byte_data(address, reg_z_l)
            sleep(0.1)
        except(IOError, OSError):
            print('[READ] Error reading from gyroscope at address ' + \
                str(address))
            insertDebugLog(NOTICE, "[READ] Error reading from gyroscope: {}".format(sensorId),
            CDH, int(time.time()))
            return None

        # Apply two's complement
        valX = utility.twos_to_int(valX)
        valY = utility.twos_to_int(valY)
        valZ = utility.twos_to_int(valZ)

        sleep(0.1)
        # Log data
        value = (valX, valY, valZ)
        sub = SensorEntropy.subsystem(sensorId)
        insertTelemetryLog(sensorId, value, sub, int(time.time()))
        return value

    @staticmethod
    def read_magnetometer(sensorId):
        insertDebugLog(NOTICE, "Read magnetometer: {}".format(sensorId),
        CDH, int(time.time()))

        if not SensorManager.isCorrectSensor(sensorId, MAG):
            raise Exception('Incorrect sensor specified')

        SensorManager.mux_select(sensorId)
        address = SensorEntropy.addr(sensorId)
        mag_reg = SensorEntropy.reg(MAG)

        # Get the values from the sensor
        reg_x_h = mag_reg['X-H']
        reg_x_l = mag_reg['X-L']
        reg_y_h = mag_reg['Y-H']
        reg_y_l = mag_reg['Y-L']
        reg_z_h = mag_reg['Z-H']
        reg_z_l = mag_reg['Z-L']

        try:
            valX = (SensorManager.bus.read_byte_data(address, reg_x_h) << 8) \
                | SensorManager.bus.read_byte_data(address, reg_x_l)
            sleep(0.1)
            valY = (SensorManager.bus.read_byte_data(address, reg_y_h) << 8) \
                | SensorManager.bus.read_byte_data(address, reg_y_l)
            sleep(0.1)
            valZ = (SensorManager.bus.read_byte_data(address, reg_z_h) << 8) \
                | SensorManager.bus.read_byte_data(address, reg_z_l)
        except(IOError, OSError):
            print('[READ] Error reading from magnetometer at address ' + \
                str(address))
            insertDebugLog(NOTICE, "[READ] Error reading from magnetometer: {}".format(sensorId),
            CDH, int(time.time()))
            return None

        # Update the values to be of two compliment
        valX = utility.twos_to_int(valX, 16);
        valY = utility.twos_to_int(valY, 16);
        valZ = utility.twos_to_int(valZ, 16);

        """
        # Change valX and valY to radians
        import math
        radians = math.atan2(valY, valX)
        radians += -0.0197

        # Compensate for errors
        if radians < 0:
            radians += 2*math.pi
        if radians > 2*math.pi:
            radians -= 2*math.pi

        # Turn radians into degrees
        degrees = math.floor(radians * 180 / math.pi)

        # Log data
        value = (radians, degrees)
        """
        value = (valX, valY, valZ)
        sub = SensorEntropy.subsystem(sensorId)
        insertTelemetryLog(sensorId, value, sub, int(time.time()))
        return value

    @staticmethod
    def read_rtc(sensorId):
        insertDebugLog(NOTICE, "Read rtc: {}".format(sensorId),
        CDH, int(time.time()))

        SensorManager.mux_select(sensorId)

        # Set up registers
        seconds_reg = rtc_reg['sec']
        minute_reg = rtc_reg['min']
        hour_reg = rtc_reg['hr']
        day_reg = rtc_reg['day']
        date_reg = rtc_reg['date']
        month_reg = rtc_reg['month']
        year_reg = rtc_reg['year']

        # Retrieve time values
        try:
            second = bus.read_byte_data(addr, seconds_reg)
            minute = bus.read_byte_data(addr, minute_reg)
            hour = bus.read_byte_data(addr, hour_reg)
            day = bus.read_byte_data(addr, day_reg)
            date = bus.read_byte_data(addr, date_reg)
            month = bus.read_byte_data(addr, month_reg)
            year = bus.read_byte_data(addr, year_reg)
        except(IOError, OSError):
            print('[READ] Error reading from RTC at address ' + \
                str(SensorEntropy.addr(sensorId)))
            insertDebugLog(NOTICE, "[READ] Error reading from RTC: {}".format(sensorId),
            CDH, int(time.time()))
            return None

        # Log data
        value = (second, minute, hour, day, date, month, year)
        sub = SensorEntropy.subsystem(sensorId)
        insertTelemetryLog(sensorId, value, sub, int(time.time()))
        return value

    @staticmethod
    def read_temp_sensor(sensorId):
        insertDebugLog(NOTICE, "Read temp sensor: {}".format(sensorId),
        CDH, int(time.time()))

        if not SensorManager.isCorrectSensor(sensorId, TEMP):
            raise Exception('Incorrect sensor specified')
            insertDebugLog(NOTICE, "Incorrect sensor specified: {}".format(sensorId),
            CDH, int(time.time()))
            return None

        addr = SensorEntropy.addr(sensorId)
        if sensorId == TEMP_PAYLOAD_A or sensorId == TEMP_PAYLOAD_B:
            bus = SensorManager.payloadbus
        else:
            SensorManager.mux_select(sensorId)
            bus = SensorManager.bus

        try:
            bus.write_byte(addr, SensorEntropy.reg(TEMP)[VAL])
        except(IOError, OSError):
            print("[READ] Error writing to temperature sensor: {}".format(sensorId))
            insertDebugLog(NOTICE, "[READ] Error writing to temperature sensor: {}".format(sensorId),
            CDH, int(time.time()))
            return None
        try:
            decValue = bus.read_byte(addr)
            fractValue = bus.read_byte(addr)
            sleep(0.02)
        except(IOError, OSError):
            print('[READ] Error reading from temperature sensor at address ' + \
                str(addr))
            insertDebugLog(NOTICE, "[READ] Error reading from temperature sensor: {}".format(sensorId),
            CDH, int(time.time()))
            return None

        # Log data
        value = utility.conv_bin_to_float(decValue, fractValue)
        sub = SensorEntropy.subsystem(sensorId)
        insertTelemetryLog(sensorId, value, sub, int(time.time()))
        return value

    @staticmethod
    def read_adc(experiment, sensorId):
        insertDebugLog(NOTICE, "Read adc: {}".format(sensorId),
        CDH, int(time.time()))

        addr = SensorEntropy.addr(sensorId)
        adc_reg = SensorEntropy.reg(ADC)
        bus = SensorManager.payloadbus

        try:
            bus.write_byte(addr, adc_reg['READ_REG_BASE'] + experiment)
            strain = ((bus.read_byte(addr) << 8) | (bus.read_byte(addr))) & 0xFFF0
            strain = strain >> 4

            bus.write_byte(addr, adc_reg['READ_REG_BASE'] + experiment + 1)
            force = ((bus.read_byte(addr) << 8) | (bus.read_byte(addr))) & 0xFFF0
            force = force >> 4

            bus.write_byte(addr, adc_reg['READ_REG_BASE'] + 7)
            temp = ((bus.read_byte(addr) << 8) | (bus.read_byte(addr))) & 0xFF80
            temp = temp >> 7

        except(IOError, OSError):
            print('[READ] Error reading from ADC at address ' + \
                str(addr))
            insertDebugLog(NOTICE, "[READ] Error reading from ADC: {}".format(sensorId),
            CDH, int(time.time()))
            return None, None, None

        if temp & 0x100 == 0:
            temp /= 2.
        else:
            temp = -((512 - temp) / 2.)

        sleep(0.01)

        # Log data
        value = (strain, force, temp)
        sub = SensorEntropy.subsystem(sensorId)
        insertTelemetryLog(ADC_0, value, sub, int(time.time()))
        return value

    @staticmethod
    def read_power_sensor(sensorId, getRaw=True):
        insertDebugLog(NOTICE, "Read power sensor: {}".format(sensorId),
        CDH, int(time.time()))

        SensorManager.mux_select(sensorId)
        value = 0, 0, 0

        try:
            with open(INA219_VOLTAGE) as v, open(INA219_CURRENT) as a, open(INA219_POWER) as p:
                voltage = int(v.read())
                amps = int(a.read())
                power  = int(p.read())

            if not getRaw:
                voltage = voltage / 1000.
                amps = amps / 1000.0
                power = power/ 1000000.0

            value = (voltage, amps, power)

            sub = POWER
            insertTelemetryLog(sensorId, value, sub, int(time.time()))
        except(IOError, OSError):
            insertDebugLog(NOTICE, "[READ] Error reading from power sensor: {}".format(sensorId),
            CDH, int(time.time()))

        return value

    @staticmethod
    def read_switch_current(num, getRaw=True):
        insertDebugLog(NOTICE, "Read adc current switch: {}".format(num), CDH, int(time.time()))

        try:
            with open(SWITCH_CURRENT_PATH + "in_voltage%d_raw" % num) as f:
                value = int(f.read())

            # Convert to millivolts
            if not getRaw:
                value = value * IN_VOLTAGE_SCALE / 1000.
                current = value*3.24*2/float(1024*3)
                value = (value, current)
            sub = CDH
            if num == 0:
                sensorId = PAYLOAD_SWITCH
            elif num == 1:
                sensorId = RADIO_SWITCH
            else:
                sensorId = "Invalid Id"
            insertTelemetryLog(sensorId, value, sub, int(time.time()))
        except:
            insertDebugLog(NOTICE, "[READ] Error reading from adc: {}".format(num), CDH, int(time.time()))
        return value

    """ -------------------- 1Wire --------------------- """

    @staticmethod
    def get_panel_data(panelId):
        insertDebugLog(NOTICE, "Get panel data: {}".format(panelId),
        CDH, int(time.time()))

        if not panelId in SIDE_PANEL_ONE_WIRE_DICT:
            raise Exception('Incorrect sensor specified')
            insertDebugLog(NOTICE, "Incorrect sensor specified: {}".format(panelId),
            CDH, int(time.time()))
        try:
            addr = SIDE_PANEL_ONE_WIRE_DICT[panelId]
            sensor = DS18B20(addr)
            value = sensor.getTemp()
            insertTelemetryLog(panelId, value, CDH, int(time.time()))
        except (IOError, OSError):
            print("[READ] Error reading from 1-wire DS18B20")
            insertDebugLog(NOTICE, "[READ] Error reading: {}".format(panelId),
            CDH, int(time.time()))
            return None
        return value

    """ -------------------- GPIO --------------------- """

    @staticmethod
    def gpio_output(pinId, pinStatus):
        """ Outputs a logic value on a GPIO pin """
        insertDebugLog(NOTICE, "GPIO output from: {}".format(pinId),
        CDH, int(time.time()))

        pinId = SensorEntropy.get_gpio_pin(pinId)
        led = Pin(pinId,'OUTPUT')
        if pinStatus == ON:
            led.on()
            return True
        elif pinStatus == OFF:
            led.off()
            return True
        else:
            raise Exception('Incorrect GPIO status')
            return False

    @staticmethod
    def gpio_input(pinId, inputTime):
        """ Receive a logic value from a GPIO pin """
        """
        TODO: Don't change pin to input, but read file instead
        """
        insertDebugLog(NOTICE, "GPIO input from: {}".format(pinId),
        CDH, int(time.time()))

        pinId = SensorEntropy.get_gpio_pin(pinId)
        pin = Pin(pinId,'INPUT')
        return pin.digitalRead() != 0

    """ -------------------- Other --------------------- """

    @staticmethod
    def mux_select(sensorId):
        insertDebugLog(NOTICE, "MUX select: {}".format(sensorId),
        CDH, int(time.time()))

        newChannel = None
        if sensorId in TEMP_IDENTIFIER_DICT:
            newChannel = TEMP_IDENTIFIER_DICT[sensorId][CH]
            mux_address = TEMP_IDENTIFIER_DICT[sensorId][MUX]
        elif sensorId in RTC_IDENTIFIER_DICT:
            newChannel = RTC_IDENTIFIER_DICT[sensorId][CH]
            mux_address = RTC_IDENTIFIER_DICT[sensorId][MUX]
        elif sensorId in GYRO_IDENTIFIER_DICT:
            newChannel = GYRO_IDENTIFIER_DICT[sensorId][CH]
            mux_address = GYRO_IDENTIFIER_DICT[sensorId][MUX]
        elif sensorId in MAG_IDENTIFIER_DICT:
            newChannel = MAG_IDENTIFIER_DICT[sensorId][CH]
            mux_address = MAG_IDENTIFIER_DICT[sensorId][MUX]
        elif sensorId == POWER:
            newChannel = I2C_DEVICES_LOOKUP_TABLE[POWER][CH][0]
            mux_address = I2C_DEVICES_LOOKUP_TABLE[POWER][MUX]
        elif sensorId == ADC:
            newChannel = I2C_DEVICES_LOOKUP_TABLE[ADC][CH][0]
            mux_address = I2C_DEVICES_LOOKUP_TABLE[ADC][MUX]
        else:
            print('Could not find sensorId', sensorId)
            insertDebugLog(NOTICE, "[mux_select] Could not find sensorId: {}".format(sensorId), CDH, int(time.time()))

        if newChannel is None or newChannel < 0 or newChannel > 7:
            return False

        if newChannel != SensorManager.channel or mux_address != SensorManager.old_mux:
            SensorManager.channel = newChannel
            SensorManager.old_mux = mux_address
            SensorManager.bus.write_byte(mux_address, 1 << newChannel)
            return True

    @staticmethod
    def isCorrectSensor(sensorId, SensorType):
        if SensorType == TEMP:
            return sensorId in TEMP_IDENTIFIER_DICT
        elif SensorType == RTC:
            return sensorId in RTC_IDENTIFIER_DICT
        elif SensorType == GYRO:
            return sensorId in GYRO_IDENTIFIER_DICT
        elif SensorType == MAG:
            return sensorId in MAG_IDENTIFIER_DICT
        return False

def main():
    # I2C Example
    while True:
        value = SensorManager.read_switch_current(PAYLOAD_SWITCH_ADC_ID, True)
        print(value, "A")
        time.sleep(1)

if __name__ == "__main__":
    main()
