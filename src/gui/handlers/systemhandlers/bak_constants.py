"""
File contains the constants used by the gui modules.
"""

SRC_PATH =                 "/root/csdc3/src"
LOGS_PATH =                SRC_PATH + "/logs/"
LOGS_CONFIG_SETUP_PATH =   LOGS_PATH + "/config_setup/"
PAYLOAD_PATH =             SRC_PATH + "/payload/"
POWER_MONITORING_PATH =    SRC_PATH + "/power_monitoring/"
SENSOR_PATH =              SRC_PATH + "/sensors/"
WATCHDOG_PATH =            SRC_PATH + "/watchdog/"
UTILITY_PATH =             SRC_PATH + "/utils/"

LOGS_SRC_LIST = ["chomsky.py"]
SENSOR_SRC_LIST = ["sensor_constants.py", "sensor_entropy.py", "sensor_manager.py", "sensor_sweep.py"]
PAYLOAD_SRC_LIST = ["payload.py"]
POWERMONITOR_SRC_LIST = ["powermonitor.py", "current_monitor.py", "battery_heaters_reader.py", "ShutAllBatteryHeaters"]
WATCHDOG_SRC_LIST = ["watchdog.py"]
UTILS_SRC_LIST = ["utility.py"]

SRC_LISTS = SENSOR_SRC_LIST + LOGS_SRC_LIST + PAYLOAD_SRC_LIST + POWERMONITOR_SRC_LIST + WATCHDOG_SRC_LIST + UTILS_SRC_LIST
SRC_TUPLES = [
    (LOGS_SRC_LIST, LOGS_PATH)
,   (SENSOR_SRC_LIST, SENSOR_PATH)
,   (PAYLOAD_SRC_LIST, PAYLOAD_PATH)
,   (POWERMONITOR_SRC_LIST, POWER_MONITORING_PATH)
,   (UTILS_SRC_LIST, UTILITY_PATH)
,   (WATCHDOG_SRC_LIST, WATCHDOG_PATH)
]
