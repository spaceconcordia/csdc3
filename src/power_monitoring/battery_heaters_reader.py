# import sys
# sys.path.append("/root/csdc3/src/sensors/")
# sys.path.append("/root/csdc3/src/utils/")
# from sensor_manager import SensorManager
# from sensor_constants import *
# from statistics import median

def BatteryHeatersReader():
    # Get temperature inputs
    # tempIdentifiers = (TEMP_BAT_1,) # TEMP_BAT_2, TEMP_BAT_3, TEMP_BAT_4)
    # tempValues = []
    # for iden in tempIdentifiers:
    #     SensorManager.init_temp_sensor(iden)
    #     valueList = []
    #     # Get median of 5 value readings to remove outliers
    #     for i in range(0,5):
    #         valueList.append(SensorManager.read_temp_sensor(iden))
    #     tempValue = median(valueList)
    #     print(tempValue)
    #     SensorManager.stop_temp_sensor(iden)
    #     # Keep final value of sensor
    #     tempValues.append(tempValue)
    #
    # # Get status identifiers
    # statusIdentifiers = (PSS_HTR_STAT_1_GPIO, PSS_HTR_STAT_2_GPIO,\
    # PSS_HTR_STAT_3_GPIO, PSS_HTR_STAT_4_GPIO)
    # statusValues = []
    # for iden in statusIdentifiers:
    #         statusValues.append(SensorManager.gpio_input(iden,0))

    tempValues = [27.2, 29.2, 31.2, 33.2]
    statusValues = [True, None, False, True]

    # Set up dict containing result
    result = {"control": "OBC", "batteries": []}

    # Populate battery heater list with acquired values
    for i in range(0,len(tempValues)):
        if i < len(tempValues) and i < len(statusValues) \
        and (tempValues[i] is not None) and (statusValues[i] is not None):
            result["batteries"].append({"temp": tempValues[i], "heaters": statusValues[i]})

    return result

def main():
    result = BatteryHeatersReader()
    print(result)

if __name__ == '__main__':
    main()
