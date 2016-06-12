import sys
sys.path.append('/root/csdc3/lib/ablib')
sys.path.append('/root/csdc3/src/logs')
sys.path.append('/root/csdc3/src/sensors')
sys.path.append('/root/csdc3/src/logs/config_setup')
from time import sleep
from sensor_entropy import *
from sensor_constants import *
from sensor_manager import SensorManager

def main():
    bat_temp = [TEMP_BAT_1,TEMP_BAT_2,TEMP_BAT_3,TEMP_BAT_4]
    brd_temp = [TEMP_EPS_BRD, TEMP_CDH_BRD, TEMP_PAYLOAD_BRD]
    payload_temp = [TEMP_PAYLOAD_A, TEMP_PAYLOAD_B]
    chassis_temp = [TEMP_PAYLOAD_CHASSIS, TEMP_END_CAP]

    for sensor in (bat_temp + brd_temp + payload_temp + chassis_temp):
        SensorManager.init_temp_sensor(sensor)
    while True:
        print "\nBattery temperature"
        for sensor in bat_temp:
            print(SensorManager.read_temp_sensor(sensor)),
        print "\nBoard temperatures"
        for sensor in brd_temp:
            print(SensorManager.read_temp_sensor(sensor)),
        """
        print "Chassis temperatures"
        for sensor in brd_temp:
            print(SensorManager.read_temp_sensor(sensor)),
        print "Payload temperatures"
        for sensor in brd_temp:
            print(SensorManager.read_temp_sensor(sensor)),
        """
        print
        sleep(1)
    for sensor in bat_temp:
        SensorManager.stop_temp_sensor(sensor)

if __name__ == '__main__':
    main()
