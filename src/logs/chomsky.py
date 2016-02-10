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
    print(telemetry_rows)
    conn.close()

    return telemetry_rows

def insertSystemCallLog():
    pass

def insertDebugLog():
    pass

def selectSystemCallLog():
    pass

def selectDebugLog():
    pass

if __name__ == "__main__":
    # TelemetryLog SELECT & INSERT test
    for i in range(500):
        insertTelemetryLog("sensor_id", 5, "payload", i)
    selectTelemetryLog("sensor_id")
    emptyTables()

    # SystemCallLog SELECT & INSERT test

    # DebugLog SELECT & INSERT test
