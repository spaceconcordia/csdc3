from sensor_constants import *
from time import time
from sensor_manager import SensorManager
from SharedLock import Lock
import cProfile

def main():
    lock = Lock(SENSOR_LOCK)

    try:
        lock.acquire()

        # Create sensor lists
        print("Creating sensor lists")
        tempSensorList = [TEMP_EPS_BRD, TEMP_CDH_BRD, TEMP_PAYLOAD_BRD]
        # TEMP_PAYLOAD_CHASSIS, TEMP_END_CAP
        batteryTempSensorList = [TEMP_BAT_1, TEMP_BAT_2, TEMP_BAT_3, TEMP_BAT_4]
        magSensorList= [MAG_0, MAG_1, MAG_2]
        adcSwitchCurrentList = [PAYLOAD_SWITCH_ADC_ID, RADIO_SWITCH_ADC_ID]
        powerSensorList = [POWER]
        panelTempSensorList = [PANEL0, PANEL1, PANEL2, PANEL3]


        masterList = list(set(tempSensorList) | set(magSensorList)
        | set(powerSensorList) | set(batteryTempSensorList) \
        | set(adcSwitchCurrentList))

        functionsDict = {}
        # Declare functions used for initialization
        print("Getting functions for initialization")
        functionsDict["init_temp"] = SensorManager.init_temp_sensor
        functionsDict["init_mag"] = SensorManager.init_magnetometer
        functionsDict["init_power"] = SensorManager.init_power_sensor

        # Declare functions used for reading
        print("Getting functions for reading")
        functionsDict["read_temp"] = SensorManager.read_temp_sensor
        functionsDict["read_mag"] = SensorManager.read_magnetometer
        functionsDict["read_power"] = SensorManager.read_power_sensor
        functionsDict["read_switch"] = SensorManager.read_switch_current

        # Declare functions used for stopping
        print("Getting functions for stopping")
        functionsDict["stop_temp"] = SensorManager.stop_temp_sensor
        functionsDict["stop_mag"] = SensorManager.stop_magnetometer
        functionsDict["stop_power"] = SensorManager.stop_power_sensor

        # Initialize sensors
        print("Initializing sensors")
        for sensor in masterList:
            if sensor in tempSensorList or sensor in batteryTempSensorList:
                functionsDict["init_temp"](sensor)
            elif sensor in magSensorList:
                functionsDict["init_mag"](sensor)
            elif sensor in powerSensorList:
                functionsDict["init_power"](sensor)

        #with open("/root/csdc3/src/sensors/temp_log.txt", "a") as f:
        for i in range(3):
            start = time()
            #sensorValueDict = {}

            # Get sensor values
            print("Getting sensor values")
            for sensor in masterList:
                if sensor in tempSensorList or sensor in batteryTempSensorList:
                    result = functionsDict["read_temp"](sensor)
                elif sensor in magSensorList:
                    result = functionsDict["read_mag"](sensor)
                elif sensor in powerSensorList:
                    result = functionsDict["read_power"](sensor)
                elif sensor in adcSwitchCurrentList:
                    result = functionsDict["read_switch"](sensor)
                #sensorValueDict[sensor] = result

            # Get time it took to complete operations
            readtime = time() - start
            #sensorValueDict["Time"] = readtime
            print("Getting completion time: {}".format(readtime))
        #f.write(str(sensorValueDict) + '\n')

        # Stop sensors
        print("Stopping sensors")
        for sensor in masterList:
            if sensor in tempSensorList or sensor in batteryTempSensorList:
                functionsDict["stop_temp"](sensor)
            elif sensor in magSensorList:
                functionsDict["stop_mag"](sensor)
            elif sensor in powerSensorList:
                functionsDict["stop_power"](sensor)

    finally:
        lock.release()
        pass

if __name__ == "__main__":
    main()
    #cProfile.run("main()")
