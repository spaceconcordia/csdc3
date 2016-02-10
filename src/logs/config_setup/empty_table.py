"""
Connect to each one of the DBs (3 copies) & create their tables.
Certain tables are under data_logs and others under system_logs.
"""
from create_db import createDBs
from delete_db import deleteDBs

def emptyTables():
    deleteDBs()
    createDBs()

if __name__ == "__main__":
    emptyTables()
