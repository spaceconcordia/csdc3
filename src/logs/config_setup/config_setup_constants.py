"""
File containts the constants used by the logs modules.
"""

# paths to both log types
SCRIPTS_PATH =        "/root/csdc3/src/gui/scripts"
SYSTEM_LOGS_PATH =    "/root/csdc3/src/logs/system_logs"
DATA_LOGS_PATH =      "/root/csdc3/src/logs/data_logs"

NUM_REDUNDANT_COPIES = 3

# names for dbs.
SYSTEM_CALLS_DB  =    "syscall.db"
DEBUG_LOGS_DB =       "debuglogs.db"
TELEMETRY_DB =        "telemetry.db"

# constants for db and table names and value types
SUBSYSTEM =           "Subsystem"
PAYLOAD =             "Payload"
CDH =                 "C&DH"
POWER =               "Power"
ACS =                 "ACS"
COMMS =               "Communications"

LOG =                 "Log"
SENSORID =            "SensorIdentifier"
VALUE =               "Val"
TIMESTAMP =           "Timestamp"
LEVEL =               "Level"

# debug levels
NOTICE =              "NOTICE"
WARNING =             "WARNING"
DEBUG =               "DEBUG"
ERROR =               "ERROR"
URGENT =              "URGENT"
CRITICAL =            "CRITICAL"

SYSCALL =             "systemcall"
STDIN =               "stdin"
STDOUT =              "stdout"
STDERR =              "stderr"

NULL =                "NULL"
TEXT =                "TEXT"
INTEGER =             "INTEGER"
REAL =                "REAL"
BLOB =                "BLOB"

TELEMETRY_COLS = [
    (SENSORID,  TEXT)
,   (VALUE,     REAL)
,   (SUBSYSTEM, TEXT)
,   (TIMESTAMP, INTEGER)
]

SYSTEM_CALLS_COLS = [
    (LEVEL,     TEXT)
,   (SYSCALL,   TEXT)
,   (SUBSYSTEM, TEXT)
,   (TIMESTAMP, INTEGER)
,   (STDERR,    TEXT)
]

DEBUG_LOGS_COLS = [
    (LEVEL,     TEXT)
,   (LOG,       TEXT)
,   (SUBSYSTEM, TEXT)
,   (TIMESTAMP, INTEGER)
]

DB_TABLES_LIST = [
    (SYSTEM_CALLS_DB, SYSTEM_CALLS_COLS, SYSTEM_LOGS_PATH)
,   (DEBUG_LOGS_DB, DEBUG_LOGS_COLS, SYSTEM_LOGS_PATH)
,   (TELEMETRY_DB, TELEMETRY_COLS, DATA_LOGS_PATH)
]
