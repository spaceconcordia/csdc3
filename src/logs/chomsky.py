"""
Connect to each one of the DBs (3 copies) & create their tables.
It does it for both data_logs and system_logs.
"""
import sqlite3
import sys
sys.path.insert(0, './config_setup')
from config_setup_constants import *
from empty_table            import emptyTables 
import time

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

def selectTelemetryLog(sensor_id):
    telemetry_rows = []
    conn = sqlite3.connect(DATA_LOGS_PATH + "/copy1/" + TELEMETRY_DB)
    c = conn.cursor()
    for row in c.execute("SELECT * FROM tabolo WHERE "
        + SENSORID + "='" + sensor_id + "'"
        + " ORDER BY " + TIMESTAMP + " DESC"):
        telemetry_rows.append(row)
    conn.close()
    return telemetry_rows

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

if __name__ == "__main__":
    # TelemetryLog SELECT & INSERT tests
    for i in range(500):
        insertTelemetryLog("sensor_id", 5, PAYLOAD, i)
    print(selectTelemetryLog("sensor_id"))
    emptyTables()

    # SystemCallLog SELECT & INSERT tests
    for i in range(500):
        insertSystemCallLog(NOTICE, "date -s", CDH , i, "stderr")
    print(selectSystemCallLog(CDH))
    emptyTables()

    # DebugLog SELECT & INSERT tests
    for i in range(500):
        insertDebugLog(NOTICE, "FUCK IT DUDE", CDH , i)
    print(selectDebugLog(CDH))
    emptyTables()
