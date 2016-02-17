"""
Connect to each one of the DBs (3 copies) & create their tables.
It does it for both data_logs and system_logs.
"""
import sqlite3
from config_setup_constants import *

def createDBs():
    copies = ["/copy1/", "/copy2/", "/copy3/"]
    for copy in copies:
        for table in DB_TABLES_LIST:
            db_name = table[0]
            table_params = table[1]
            path = table[2]

            conn = sqlite3.connect(path + copy + db_name)
            command = "CREATE TABLE tabolo("
            for i, param in enumerate(table_params):
                if i < len(table_params)-1:
                    command += param[0] + " " + param[1] + ","
                else:
                    command += param[0] + " " + param[1] + ")"
            print(command)
            c = conn.cursor()
            c.execute(command)
            conn.commit()

            conn.close()

if __name__ == "__main__":
    createDBs()
