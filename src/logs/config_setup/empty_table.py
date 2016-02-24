"""
Connect to each one of the DBs (3 copies) & create their tables.
Certain tables are under data_logs and others under system_logs.
"""
import os
from create_db import createDBs, createStaticLogs
from delete_db import deleteDBs
from config_setup_constants import *

def emptyTables():
    deleteDBs()
    createDBs()
    os.system("rm " + STATIC_LOGS_PATH + "/*")
    createStaticLogs()

if __name__ == "__main__":
    emptyTables()
