"""
Connect to each one of the DBs (3 copies) & create their tables.
It does it for both data_logs and system_logs.
"""
import time
import sqlite3

import sys
sys.path.insert(0, '/root/csdc3/src/sensors')
from sensor_constants       import *
sys.path.insert(0, '/root/csdc3/src/logs/config_setup')
from config_setup_constants import *
from empty_table            import emptyTables
from operator import itemgetter
sys.path.insert(0, '/root/csdc3/src/utils')
from utility import *

def insertTelemetryLog(sensor_id, value, subsystem, timestamp):
    copies = ["/copy1/", "/copy2/", "/copy3/"]
    for copy in copies:
        conn = sqlite3.connect(DATA_LOGS_PATH + copy + TELEMETRY_DB)
        c = conn.cursor()
        c.execute("INSERT INTO tabolo VALUES ('"
            + sensor_id + "','"
            + str(value) + "','"
            + subsystem + "','"
            + str(timestamp)
            + "')")
        conn.commit()
        conn.close()
    writeTelemetryLogs(sensor_id, value, subsystem, timestamp)

def selectTelemetryLog(sensor_id, num_entries=1):
    telemetry_rows = []
    conn = sqlite3.connect(DATA_LOGS_PATH + "/copy1/" + TELEMETRY_DB)
    c = conn.cursor()
    for row in c.execute("SELECT * FROM tabolo WHERE "
        + SENSORID + "='" + sensor_id + "'"
        + " ORDER BY " + TIMESTAMP + " DESC LIMIT %d;" % num_entries):
        telemetry_rows.append(row)
    conn.close()
    return telemetry_rows

def selectSubsystemLog(subsystem, num_entries=1):
    telemetry_rows = []
    conn = sqlite3.connect(DATA_LOGS_PATH + "/copy1/" + TELEMETRY_DB)
    c = conn.cursor()
    for row in c.execute("SELECT * FROM tabolo WHERE "
        + SUBSYSTEM + "='" + subsystem + "'"
        + " ORDER BY " + TIMESTAMP + " DESC LIMIT %d;" % num_entries):
        telemetry_rows.append(row)
    conn.close()
    return telemetry_rows

def selectLastTelemetryLog(sensor_id):
    telemetry_rows = []
    conn = sqlite3.connect(DATA_LOGS_PATH + "/copy1/" + TELEMETRY_DB)
    c = conn.cursor()
    for row in c.execute("SELECT LAST("
        + sensor_id + ") FROM tabolo"):
        telemetry_rows.append(row)
    conn.close()
    return telemetry_rows

def insertPayloadLog(start_time, end_time, a_or_b):
    copies = ["/copy1/", "/copy2/", "/copy3/"]
    for copy in copies:
        conn = sqlite3.connect(DATA_LOGS_PATH + copy + PAYLOAD_DB)
        c = conn.cursor()
        c.execute("INSERT INTO tabolo VALUES ('"
            + str(start_time) + "','"
            + str(end_time) + "','"
            + a_or_b
            + "')")
        conn.commit()
        conn.close()
    writePayloadLogs(start_time, end_time)

def selectPayloadLog():
    payload_rows = []
    conn = sqlite3.connect(DATA_LOGS_PATH + "/copy1/" + PAYLOAD_DB)
    c = conn.cursor()
    for row in c.execute("SELECT * FROM tabolo"):
        payload_rows.append(row)
    conn.close()
    return list(reversed(payload_rows))

def selectPayloadData(start_time, end_time, temp_payload_exp):
    payload_rows = []
    temp_rows = []
    conn = sqlite3.connect(DATA_LOGS_PATH + "/copy1/" + TELEMETRY_DB)
    c = conn.cursor()
    # Get strain and load values
    for row in c.execute("SELECT * FROM tabolo WHERE " +
        SENSORID  + " = '" + ADC_0 + "' AND " +
        TIMESTAMP + " >= " + str(start_time) + " AND " +
        TIMESTAMP + " <= " + str(end_time)):
        payload_rows.append(row)

    # Get temperature values
    for row in c.execute("SELECT * FROM tabolo WHERE " +
        SENSORID  + " = '" + temp_payload_exp + "' AND " +
        TIMESTAMP + " >= " + str(start_time) + " AND " +
        TIMESTAMP + " <= " + str(end_time)):
        temp_rows.append(row)

    payload_rows = sorted(payload_rows, key=itemgetter(-1))
    strainList = [{"x":i[-1]*1000,"y":str2list(i[1])[0]} for i in payload_rows]
    loadList = [{"x":i[-1]*1000,"y":str2list(i[1])[1]} for i in payload_rows]
    strainConvList = [{"x":i[-1]*1000,"y":convertStrain(str2list(i[1])[0])} for i in payload_rows]
    loadConvList = [{"x":i[-1]*1000,"y":convertLoad(str2list(i[1])[1])} for i in payload_rows]
    tempList = [{"x":i[-1]*1000,"y":i[1]} for i in temp_rows]
    result = {"strainList":strainList, "loadList":loadList,
    "strainConvList":strainConvList, "loadConvList":loadConvList,
    "tempList":tempList, "startTime":start_time,
    "endTime":end_time}

    conn.close()
    return result

def insertSystemCallLog(level, syscall, subsystem, timestamp, stderr):
    copies = ["/copy1/", "/copy2/", "/copy3/"]
    for copy in copies:
        conn = sqlite3.connect(SYSTEM_LOGS_PATH + copy + SYSTEM_CALLS_DB)
        c = conn.cursor()
        c.execute("INSERT INTO tabolo VALUES ('"
            + level + "','"
            + syscall + "','"
            + subsystem + "','"
            + str(timestamp) + "','"
            + stderr
            + "')")
        conn.commit()
        conn.close()
    writeSyscallLogs(level, syscall, subsystem, timestamp, stderr)

def selectSystemCallLog(subsystem):
    syscall_rows = []
    conn = sqlite3.connect(SYSTEM_LOGS_PATH + "/copy1/" + SYSTEM_CALLS_DB)
    c = conn.cursor()
    for row in c.execute("SELECT * FROM tabolo WHERE "
        + SUBSYSTEM + "='" + subsystem + "'"
        + " ORDER BY " + TIMESTAMP + " DESC"):
        syscall_rows.append(row)
    conn.close()
    return syscall_rows

def insertDebugLog(level, log, subsystem, timestamp):
    copies = ["/copy1/", "/copy2/", "/copy3/"]
    for copy in copies:
        conn = sqlite3.connect(SYSTEM_LOGS_PATH + copy + DEBUG_LOGS_DB)
        c = conn.cursor()
        c.execute("INSERT INTO tabolo VALUES ('"
            + level + "','"
            + log + "','"
            + subsystem + "','"
            + str(timestamp)
            + "')")
        conn.commit()
        conn.close()
    writeDebugLogs(level, log, subsystem, timestamp)

def selectDebugLog(subsystem):
    debug_rows = []
    conn = sqlite3.connect(SYSTEM_LOGS_PATH + "/copy1/" + DEBUG_LOGS_DB)
    c = conn.cursor()
    for row in c.execute("SELECT * FROM tabolo WHERE "
        + SUBSYSTEM + "='" + subsystem + "'"
        + " ORDER BY " + TIMESTAMP + " DESC"):
        debug_rows.append(row)
    conn.close()
    return debug_rows

def writeTelemetryLogs(sensor_id, value, subsystem, timestamp):
    with open(STATIC_LOGS_PATH + '/telemetry.log', 'a') as f:
        f.write(' '.join([sensor_id, str(value), subsystem, time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime(timestamp-4*60*60))]) + '\n')

def writeSyscallLogs(level, syscall, subsystem, timestamp, stderr):
    with open(STATIC_LOGS_PATH + '/syscall.log', 'a') as f:
        f.write(' '.join([level, syscall, subsystem, time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime(timestamp-4*60*60)), stderr]) + '\n')

def writeDebugLogs(level, log, subsystem, timestamp):
    with open(STATIC_LOGS_PATH + '/debuglogs.log', 'a') as f:
        f.write(' '.join([level, log, subsystem, time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime(timestamp-4*60*60))]) + '\n')

def writePayloadLogs(start_time, end_time):
    timestamp = int(time.time())
    with open(STATIC_LOGS_PATH + '/payload.log', 'a') as f:
        f.write(' '.join([str(start_time), str(end_time), time.strftime('%m/%d/%Y %H:%M:%S',  time.gmtime(timestamp-4*60*60))]) + '\n')

if __name__ == "__main__":
    # TelemetryLog SELECT & INSERT tests
    power_tuple = selectSubsystemLog(PAYLOAD, 10)
    print(power_tuple)
    """
    for i in range(50):
        insertTelemetryLog("sensor_id", 5, PAYLOAD, i)
    print(selectTelemetryLog("sensor_id"))
#   emptyTables()

    # SystemCallLog SELECT & INSERT tests
    for i in range(50):
        insertSystemCallLog(NOTICE, "date -s", CDH , i, "stderr")
    print(selectSystemCallLog(CDH))
#    emptyTables()

    # DebugLog SELECT & INSERT tests
    for i in range(50):
        insertDebugLog(NOTICE, "FUCK IT DUDE", CDH , i)
    print(selectDebugLog(CDH))
#    emptyTables()
    """

#    print(selectTelemetryLog(POWER))

# for experiment in list(reversed(selectPayloadLog())):
#       print(selectPayloadData(experiment[0], experiment[1]))
