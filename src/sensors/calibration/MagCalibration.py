#!/usr/bin/python
import sys
sys.path.append('/root/csdc3/src/sensors')
from sensor_manager import SensorManager
from sensor_constants import *
import smbus
import time
import math

bus = smbus.SMBus(0)
address = 0x1e

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def write_byte(adr, value):
    bus.write_byte_data(address, adr, value)

def main():
    magSensorList= [MAG_0, MAG_1, MAG_2]
    SensorManager.mux_select(magSensorList[0])
    bus = smbus.SMBus(0)
    address = 0x1e

    write_byte(0, 0b01110000) # Set to 8 samples @ 15Hz
    write_byte(1, 0b00100000) # 1.3 gain LSb / Gauss 1090 (default)
    write_byte(2, 0b00000000) # Continuous sampling

    scale = 0.92
    """ ***************** """

    # for i in range(0,500):
    #     x_out = read_word_2c(3)
    #     y_out = read_word_2c(7)
    #     z_out = read_word_2c(5)
    #
    #     bearing  = math.atan2(y_out, x_out)
    #     if (bearing < 0):
    #         bearing += 2 * math.pi
    #
    #     print x_out, y_out, (x_out * scale), (y_out * scale)
    #     time.sleep(0.1)

    """ ***************** """

    x_out = read_word_2c(3) * scale
    y_out = read_word_2c(7) * scale
    z_out = read_word_2c(5) * scale

    bearing  = math.atan2(y_out, x_out)
    if (bearing < 0):
        bearing += 2 * math.pi

    print("Bearing: {}".format(math.degrees(bearing)))

    """ ***************** """

if __name__ == '__main__':
    main()
