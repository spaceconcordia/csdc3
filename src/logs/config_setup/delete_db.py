"""
Connect to each one of the DBs (3 copies) & create their tables.
Certain tables are under data_logs and others under system_logs.
"""
import os
from config_setup_constants import *

def deleteDBs():
    os.system("bash " + SCRIPTS_PATH + "/deleteDB.sh")

if __name__ == "__main__":
    deleteDBs()
