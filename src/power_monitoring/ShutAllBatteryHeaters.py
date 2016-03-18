import sys
sys.path.append("/root/csdc3/src/sensors/")
sys.path.append("/root/csdc3/src/utils/")
from sensor_manager import SensorManager
from sensor_constants import *
from time import sleep
from SharedLock import Lock

def ShutAllBatteryHeaters():
    """ shut all heaters off """
    heaterIdentifers = (PSS_HTR_EN_1_GPIO, PSS_HTR_EN_2_GPIO,\
    PSS_HTR_EN_3_GPIO, PSS_HTR_EN_4_GPIO)
    SensorManager.gpio_output(PSS_HTR_MUX_SEL_GPIO, OFF)
    for iden in heaterIdentifers:
        SensorManager.gpio_output(heaterIdentifers[i], OFF)

def main():
    lock = Lock("/root/csdc3/src/utils/payloadLock.tmp")
    lock.acquire()
    print("Lock has been acquired by ShutAllBatteryHeaters.py")
    sleep(600)
    lock.release()
    print("Lock has been released by ShutAllBatteryHeaters.py")
    # ShutAllBatteryHeaters()

if __name__ == '__main__':
    main()
