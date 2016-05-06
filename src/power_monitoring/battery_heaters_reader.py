# import sys
# sys.path.append("/root/csdc3/src/sensors/")
# sys.path.append("/root/csdc3/src/utils/")
# from sensor_manager import SensorManager
# from sensor_constants import *
# from statistics import median

def returnRandInt(minValue, maxValue):
    return int(random.random()*(maxValue - minValue + 1)) % (maxValue + 1) + minValue

def BatteryHeatersReader():
    #Get temperature inputs
    tempIdentifiers = (TEMP_BAT_4, TEMP_BAT_2, TEMP_BAT_3, TEMP_BAT_1)
    tempValues = []
    for iden in tempIdentifiers:
        SensorManager.init_temp_sensor(iden)
        tempValue = SensorManager.read_temp_sensor(iden)
        SensorManager.stop_temp_sensor(iden)
        # Keep final value of sensor
        tempValues.append(tempValue)
   
    # Get status identifiers
    statusIdentifiers = (PSS_HTR_STAT_1_GPIO, PSS_HTR_STAT_2_GPIO,\
    PSS_HTR_STAT_3_GPIO, PSS_HTR_STAT_4_GPIO)
    statusValues = []
    for iden in statusIdentifiers:
            statusValues.append(SensorManager.gpio_input(iden,0))

#    state0 = [23, 34, -32, 1]
#    state1 = [27, 21, 34, 24]
#    state2 = [30, 11, 22, 12]
#    state3 = [35, 2, 1, 15]
#    statusValues = [True, False, True, False]
#    tempValues = []
#    try:
#        f = open('state.tmp', 'r')
#        state = int(f.read())
#    except:
#        f = open('state.tmp', 'w')
#        f.write(str(0))
#        state = 1
#    finally:
#        f.close()

#        if state == 0:
#            tempValues = state0
#        elif state == 1:
#            tempValues = state1
#        elif state == 2:
#            tempValues = state2
#        else:
#            tempValues = state3
#            state = -1
#    try:
#        f = open('state.tmp', 'w')
#        f.write(str(state + 1))
#   finally:
#        f.close()

    # Set up dict containing result
#    result = {"control": "", "batteries": []}

    # Populate battery heater list with acquired values
#    for i in range(0,len(tempValues)):
#        if i < len(tempValues) and i < len(statusValues):
#            result["batteries"].append({"temp": tempValues[i], "heaters": statusValues[i]})

    # Update control status
    if SensorManager.gpio_input(PSS_HTR_MUX_SEL_GPIO,0):
        result["control"] = "ANAL"
    else:
        result["control"] = "OBC"

    print(result)
    return result

def functionality():
    result = BatteryHeatersReader()
    print(result)

if __name__ == '__main__':
    functionality()
