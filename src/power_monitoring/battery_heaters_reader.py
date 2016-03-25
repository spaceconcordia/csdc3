import sys
sys.path.append("/root/csdc3/src/sensors/")
sys.path.append("/root/csdc3/src/utils/")
from sensor_manager import SensorManager
from sensor_constants import *
from statistics import median

def BatteryHeatersReader():
    # Get temperature inputs
    tempIdentifiers = (TEMP_BAT_1,) # TEMP_BAT_2, TEMP_BAT_3, TEMP_BAT_4)
    tempValues = []
    for iden in tempIdentifiers:
        SensorManager.init_temp_sensor(iden)
        valueList = []
        # Get median of 5 value readings to remove outliers
        for i in range(0,5):
            valueList.append(SensorManager.read_temp_sensor(iden))
        tempValue = median(valueList)
        print(tempValue)
        SensorManager.stop_temp_sensor(iden)
        # Keep final value of sensor
        tempValues.append(tempValue)

    # Get status identifiers
    statusIdentifiers = (PSS_HTR_STAT_1_GPIO, PSS_HTR_STAT_2_GPIO,\
    PSS_HTR_STAT_3_GPIO, PSS_HTR_STAT_4_GPIO)
    statusValues = []
    for iden in statusIdentifiers:
            statusValues.append(SensorManager.gpio_input(iden,0))

    return {"control": "OBC", #"ANAL"
            "batteries": (
            {"temp": tempValues[0], "heaters": statusValues[0]},
            {"temp": tempValues[1], "heaters": statusValues[0]},
            {"temp": tempValues[2], "heaters": statusValues[0]},
            {"temp": tempValues[3], "heaters": statusValues[0]}
            )
           }

def main():
    print(BatteryHeatersReader())

if __name__ == '__main__':
    main()
