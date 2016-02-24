import sys
sys.path.append('/root/csdc3/lib/ablib')
from ablib_python3 import Pin
from time import sleep
from sensor_entropy import *
from sensor_constants import *
import smbus
import time
import math

class SensorManager:

    bus = smbus.SMBus(0)
    active_gpio_pins = {}

    """ -------------------- Initialization --------------------- """

    @staticmethod
    def init_gyroscope(sensorId):
        SensorManager.mux_select(sensorId)
        try:
            SensorManager.bus.write_byte(SensorEntropy.addr(GYRO), 0x00)
        except IOError:
            print('[INIT] Error writing to gyroscope at address ' + \
                str(SensorEntropy.addr(GYRO))
            return -1
        time.sleep(0.1)

    @staticmethod
    def init_magnetometer(sensorId):
        SensorManager.mux_select(sensorId)
        try:
            SensorManager.bus.write_byte_data(SensorEntropy.addr(MAG), \
            SensorEntropy.reg(MAG)['INIT'], 0x01)
        except IOError:
            print('[INIT] Error writing to magnetometer at address ' + \
                str(SensorEntropy.addr(MAG))
            return -1
        time.sleep(0.1)

    @staticmethod
    def init_rtc():
        pass

    @staticmethod
    def init_temp_sensor(sensorId):
        #SensorManager.mux_select(sensorId)

        try:
            # Start data conversion
            SensorManager.bus.write_byte_data(SensorEntropy.addr(TEMP), \
            SensorEntropy.reg(TEMP)[START], 0x01)
            # Enable continuous mode
            SensorManager.bus.write_byte_data(SensorEntropy.addr(TEMP), \
            SensorEntropy.reg(TEMP)[CONFIG], 0x00)
        except IOError:
            print('[INIT] Error writing to temperature sensor at address ' + \
                str(SensorEntropy.addr(TEMP)))
            return -1

        time.sleep(0.1)

    @staticmethod
    def init_adc(sensorId):
        SensorManager.mux_select(sensorId)
        addr = SensorEntropy.addr(ADC)
        adc_reg = SensorEntropy.reg(ADC)
        bus = SensorManager.bus
        busy_reg = SensorManager.bus.read_byte_data(addr, \
        adc_reg['BUSY_STATUS_REG'])

        try:
            # Use internal Vref
            bus.write_byte_data(addr, adc_reg['ADV_CONFIG_REG'], 0x04)
            # Set continuous mode
            bus.write_byte_data(addr, adc_reg['CONV_RATE_REG'], 0x01)
            # Enable all channels
            bus.write_byte_data(addr, adc_reg['CHANNEL_DISABLE_REG'], 0x0)
            # Set high limits
            bus.write_byte_data(addr, adc_reg['LIMIT_REG_BASE'], 0x05)
            bus.write_byte_data(addr, adc_reg['LIMIT_REG_BASE2'], 0x05)
            # Start conversion without interrupts
            bus.write_byte_data(addr, adc_reg['CONFIG_REG'], 0x01)
        except IOError:
            print('[INIT] Error writing to ADC at address ' + \
                str(addr))
            return -1

        try:
            print('*' * 50)
            print("Config:", format(bus.read_byte_data(addr, adc_reg['CONFIG_REG']), '#04x'))
            print("Mode:", format(bus.read_byte_data(addr, adc_reg['ADV_CONFIG_REG']), '#04x'))
            print("Conversion:", format(bus.read_byte_data(addr, adc_reg['CONV_RATE_REG']), '#04x'))
            print("Channels:", format(bus.read_byte_data(addr, adc_reg['CHANNEL_DISABLE_REG']), '#04x'))
            print("Limits:", format(bus.read_byte_data(addr, adc_reg['LIMIT_REG_BASE']), '#04x'))
            print("Interrupts:", format(bus.read_byte_data(addr, 0x1), '#04x'))
        except IOError:
            print('[INIT] Error reading from ADC at address ' + \
                str(addr))
            return -1

        sleep(0.01)

    @staticmethod
    def init_power_sensor():
        pass

    """ -------------------- Stop --------------------- """

    @staticmethod
    def stop_gyroscope(sensorId):
        SensorManager.mux_select(sensorId)
        try:
            SensorManager.bus.write_byte(SensorEntropy.addr(GYRO), 0x01)
        except IOError:
            print('[STOP] Error writing to gyroscope at address ' + \
                str(SensorEntropy.addr(GYRO)))
            return -1
        time.sleep(0.1)

    @staticmethod
    def stop_temp_sensor(sensorId):
        SensorManager.mux_select(sensorId)
        try:
            SensorManager.bus.write_byte_data(SensorEntropy.addr(TEMP), \
            SensorEntropy.reg(TEMP)[STOP], 0x01)
        except IOError:
            print('[STOP] Error writing to temperature sensor at address ' + \
                str(SensorEntropy.addr(TEMP)))
            return -1

    @staticmethod
    def stop_rtc():
        pass

    @staticmethod
    def stop_adc_sensor(sensorId):
        SensorManager.mux_select(sensorId)
        try:
            SensorManager.bus.write_byte_data(SensorEntropy.addr(ADC), \
		          SensorEntropy.reg(ADC)['CONFIG_REG'], 0x00)
        except IOError:
            print('[STOP] Error writing to ADC at address ' + \
                str(SensorEntropy.addr(ADC)))
            return -1

    @staticmethod
    def stop_power_sensor():
        pass

    """ -------------------- Reading --------------------- """

    @staticmethod
    def read_gyroscope(sensorId):
        SensorManager.mux_select(sensorId)
        address = SensorEntropy.addr(GYRO)

        # Get the values from the sensor
        reg_x_h = SensorEntropy.reg(GYRO)['X-H']
        reg_x_l = SensorEntropy.reg(GYRO)['X-L']
        reg_y_h = SensorEntropy.reg(GYRO)['Y-H']
        reg_y_l = SensorEntropy.reg(GYRO)['Y-L']
        reg_z_h = SensorEntropy.reg(GYRO)['Z-H']
        reg_z_l = SensorEntropy.reg(GYRO)['Z-L']

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
        except IOError:
            print('[READ] Error reading from gyroscope at address ' + \
                str(address))
            return -1

        # Apply two's complement
        valX = twos_to_int(valX)
        valY = twos_to_int(valY)
        valZ = twos_to_int(valZ)

        print(valX, valY, valZ)

    @staticmethod
    def read_magnetometer(sensorId):
        SensorManager.mux_select(sensorId)
        address = SensorEntropy.addr(MAG)

        # Get the values from the sensor
        reg_x_h = SensorEntropy.reg(MAG)['X-H']
        reg_x_l = SensorEntropy.reg(MAG)['X-L']
        reg_y_h = SensorEntropy.reg(MAG)['Y-H']
        reg_y_l = SensorEntropy.reg(MAG)['Y-L']
        reg_z_h = SensorEntropy.reg(MAG)['Z-H']
        reg_z_l = SensorEntropy.reg(MAG)['Z-L']

        try:
            valX = (SensorManager.bus.read_byte_data(address, reg_x_h) << 8) \
                | SensorManager.bus.read_byte_data(address, reg_x_l)
            sleep(0.1)
            valY = (SensorManager.bus.read_byte_data(address, reg_y_h) << 8) \
                | SensorManager.bus.read_byte_data(address, reg_y_l)
            sleep(0.1)
            valZ = (SensorManager.bus.read_byte_data(address, reg_z_h) << 8) \
                | SensorManager.bus.read_byte_data(address, reg_z_l)
        except IOError:
            print('[READ] Error reading from magnetometer at address ' + \
                str(address))
            return -1

        sleep(0.1)

        # Update the values to be of two compliment
        valX = SensorManager.twos_to_int(valX, 16);
        valY = SensorManager.twos_to_int(valY, 16);
        valZ = SensorManager.twos_to_int(valZ, 16);

        # Change valX and valY to radians
        radians = math.atan2(valY, valX)
        radians += -0.0197

        # Compensate for errors
        if radians < 0:
            radians += 2*math.pi
        if radians > 2*math.pi:
            radians -= 2*math.pi

        # Turn radians into degrees
        degrees = math.floor(radians * 180 / math.pi)

        # Print the value to the output
        return (radians, degrees)

    @staticmethod
    def read_rtc(sensorId):
        SensorManager.mux_select(sensorId)

        # Set up registers
        seconds_reg = SensorEntropy.reg(RTC)['sec']
        minute_reg = SensorEntropy.reg(RTC)['min']
        hour_reg = SensorEntropy.reg(RTC)['hr']
        day_reg = SensorEntropy.reg(RTC)['day']
        date_reg = SensorEntropy.reg(RTC)['date']
        month_reg = SensorEntropy.reg(RTC)['month']
        year_reg = SensorEntropy.reg(RTC)['year']

        # Retrieve time values
        try:
            second = SensorManager.bus.read_byte_data(SensorEntropy.addr(RTC), seconds_reg)
            minute = SensorManager.bus.read_byte_data(SensorEntropy.addr(RTC), minute_reg)
            hour = SensorManager.bus.read_byte_data(SensorEntropy.addr(RTC), hour_reg)
            day = SensorManager.bus.read_byte_data(SensorEntropy.addr(RTC), day_reg)
            date = SensorManager.bus.read_byte_data(SensorEntropy.addr(RTC), date_reg)
            month = SensorManager.bus.read_byte_data(SensorEntropy.addr(RTC), month_reg)
            year = SensorManager.bus.read_byte_data(SensorEntropy.addr(RTC), year_reg)
        except IOError:
            print('[READ] Error reading from RTC at address ' + \
                str(SensorEntropy.addr(RTC)))
            return -1

        return (second, minute, hour, day, date, month, year)

    @staticmethod
    def read_temp_sensor(sensorId):
        SensorManager.mux_select(sensorId)

        try:
            SensorManager.bus.write_byte(SensorEntropy.addr(TEMP), SensorEntropy.reg(TEMP)[VAL])
        except IOError:
            print('[READ] Error writing to temperature sensor at address ' + \
                str(SensorEntropy.addr(TEMP))
            return -1
        try:
            decValue = SensorManager.bus.read_byte(SensorEntropy.addr(TEMP))
            fractValue = SensorManager.bus.read_byte(SensorEntropy.addr(TEMP))
            sleep(0.1)
        except IOError:
            print('[READ] Error reading from temperature sensor at address ' + \
                str(SensorEntropy.addr(TEMP))
            return -1

        return SensorManager.conv_bin_to_int(decValue, fractValue)

    @staticmethod
    def read_adc(experiment, sensorId):
        SensorManager.mux_select(sensorId)
        addr = SensorEntropy.addr(ADC)
        adc_reg = SensorEntropy.reg(ADC)
        bus = SensorManager.bus

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
        except IOError:
            print('[READ] Error reading from ADC at address ' + \
                str(addr)
            return -1

        if temp & 0x100 == 0:
            temp /= 2.
        else:
            temp = -((512 - temp) / 2.)

        sleep(0.01)
        return (strain, force, temp)

    @staticmethod
    def read_power_sensor():
        pass

    """ -------------------- GPIO --------------------- """

    def gpio_output(pinId, onTime, offTime):
        if not (pinId in SensorManager.active_gpio_pins):
            SensorManager.active_gpio_pins[pinId] = 'off'

        led = Pin(pinId,'OUTPUT')

        if onTime == 0 and offTime == 0:
            return
        elif onTime == 0:
            if SensorManager.active_gpio_pins[pinId] == 'on':
                led.off()
                SensorManager.active_gpio_pins[pinId] == 'off'
            else:
                led.off()
        elif offTime == 0:
            if SensorManager.active_gpio_pins[pinId] == 'off':
                led.on()
                SensorManager.active_gpio_pins[pinId] = 'on'
            else:
                led.on()
        else:
            led.on()
            SensorManager.active_gpio_pins[pinId] = 'on'
            sleep(onTime)
            led.off()
            SensorManager.active_gpio_pins[pinId] = 'off'
            sleep(offTime)

    def gpio_input(pinId, inputTime):
        pass

    """ -------------------- Other --------------------- """

    @staticmethod
    def mux_select(sensorId):
        channel = None
        if sensorId in TEMP_IDENTIFIER_DICT:
            channel = TEMP_IDENTIFIER_DICT[sensorId][CH]
        elif sensorId in RTC_IDENTIFIER_DICT:
            channel = RTC_IDENTIFIER_DICT[sensorId][CH]
        elif sensorId in GYRO_IDENTIFIER_DICT:
            channel = GYRO_IDENTIFIER_DICT[sensorId][CH]
        elif sensorId in MAG_IDENTIFIER_DICT:
            channel = MAG_IDENTIFIER_DICT[sensorId][CH]

        if channel < 0 or channel > 7 or (not channel):
            return False

        mux_address = SensorEntropy.addr(MUX)
        SensorManager.bus.write_byte(mux_address, 1 << channel)

    @staticmethod
    def twos_to_int(val, len):
        if val & (1 << len - 1):
          val = val - (1 << len)
        return val

    @staticmethod
    def conv_bin_to_int(decimalBin, fractionalBin):
        result = 0
        isNegative = (decimalBin >> 7) & 0x1
        if isNegative:
            result = (decimalBin ^ 0xff) + 1
            result *= -1
        else:
            result = decimalBin
        tempFract = fractionalBin
        count = 1
        fract = 0
        while count <= 8:
            fract += ((tempFract >> 7) & 0x1) * pow(2, -count)
            tempFract = tempFract << 1
            count += 1
        result += fract
        return result

def main():
    SensorManager.init_temp_sensor(TEMP_4)
    temp_value = SensorManager.read_temp_sensor(TEMP_4)
    SensorManager.stop_temp_sensor(TEMP_4)
    print(temp_value)

if __name__ == "__main__":
    main()
