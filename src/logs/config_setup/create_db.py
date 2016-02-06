"""
Connect to each one of the DBs (3 copies) & create their tables.
It does it for both data_logs and system_logs.
"""
import sqlite3
from config_setup_constants import *

if __name__ == "__main__":
    copies = ["/copy1/", "/copy2/", "/copy3/"]
    for copy in copies:
        for table in DB_TABLES_LIST:
            db_name = table[0]
            table_params = table[1]

            print(SYSTEM_LOGS_PATH + copy + db_name)
            conn = sqlite3.connect(SYSTEM_LOGS_PATH + copy + db_name)
            c = conn.cursor()

            c.execute("CREATE TABLE tabolo(" +
                "?,"*(len(table_params) - 1) + "?)", table_params)

            c.commit()
            conn.close()
