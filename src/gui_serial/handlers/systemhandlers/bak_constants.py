"""
File contains the constants used by the gui modules.
"""

SRC_PATH =                 "/root/csdc3/src"
LOGS_PATH =                SRC_PATH + "/logs/"
LOGS_CONFIG_SETUP_PATH =   LOGS_PATH + "/config_setup/"
PAYLOAD_PATH =             SRC_PATH + "/payload/"
POWER_MONITORING_PATH =    SRC_PATH + "/power_monitoring/"
SENSOR_PATH =              SRC_PATH + "/sensors/"

LOGS_SRC_LIST = ["chomsky"]
SENSOR_SRC_LIST = ["sensor_constants.py", "sensor_entropy.py", "sensor_manager.py"]

SRC_LISTS = SENSOR_SRC_LIST + LOGS_SRC_LIST
SRC_TUPLES = [
    (LOGS_SRC_LIST, LOGS_PATH)
,   (SENSOR_SRC_LIST, SENSOR_PATH)
]