import tornado.web

import os
import datetime

from subprocess    import check_output
from gui_constants import *

RAM_INTENSIVE_PROCESSES =      "ramIntensProc"
CPU_INTENSIVE_PROCESSES =      "cpuIntensProc"
DISK_PARTITION =               "diskPart"

class TableHandler(tornado.web.RequestHandler):
    def get(self):
        # for the tables: ramIntensProc, cpuIntensProc, DiskPart
        table_name = self.get_argument("table_name", "None")
        jstable = ""
        if table_name == "None" or \
            (table_name != RAM_INTENSIVE_PROCESSES
                and  table_name != CPU_INTENSIVE_PROCESSES
                    and  table_name != DISK_PARTITION):
            self.write({
                "status_code": 400,
                "message": "Illegal input arguments",
                "description": "table_name was not passed",
            })
            self.finish()
        elif table_name == RAM_INTENSIVE_PROCESSES:
            os.system('ps aux | sort -rk 4,4 | head -n 6 > ' + GUI_PATH + '/out.txt')
            jstable = '<table class="table"><thead><tr><th>PID</th><th>User</th>' + \
                '<th>Mem%</th><th>Rss</th><th>Vsz</th><th>Cmd</th></tr></thead><tbody>'
            with open(GUI_PATH + '/out.txt', 'r') as f:
                content = f.read()
                rows = content.split('\n')
                rows.pop(0)
                rows.pop()
                for row in rows:
                    row = row.split()
                    cmd = ""
                    for index, item in enumerate(row):   # default is zero
                        if index >= 10 and index <= 11:
                            cmd = cmd + item + " "
                    jstable = jstable + '<tr><td>' + row[1] + '</td>'        \
                                          + '<td>' + row[0] + '</td>'        \
                                          + '<td>' + row[3] + '</td>'        \
                                          + '<td>' + row[5] + '</td>'        \
                                          + '<td>' + row[4] + '</td>'        \
                                          + '<td>' + cmd + '</td>'           \
                                      + '</tr>'
            jstable = jstable + '</tbody></table>'
            os.system('rm ' + GUI_PATH + '/out.txt')
            self.write({
                "status_code": 200,
                "jstable": jstable,
                "request_time": str(datetime.datetime.now()).split('.')[0]
            })
            self.finish()
        elif table_name == CPU_INTENSIVE_PROCESSES:
            os.system('ps aux | sort -rk 3,3 | head -n 6 > ' + GUI_PATH + '/out.txt')
            jstable = '<table class="table"><thead><tr><th>PID</th><th>User</th>' + \
                '<th>Cpu%</th><th>Rss</th><th>Vsz</th><th>Cmd</th></tr></thead><tbody>'
            with open(GUI_PATH + '/out.txt', 'r') as f:
                content = f.read()
                rows = content.split('\n')
                rows.pop(0)
                rows.pop()
                for row in rows:
                    row = row.split()
                    cmd = ""
                    for index, item in enumerate(row):   # default is zero
                        if index == 10:
                            cmd = cmd + item + " "
                            if "python3" in item:
                                cmd = cmd + row[11]
                    jstable = jstable + '<tr><td>' + row[1] + '</td>'        \
                                          + '<td>' + row[0] + '</td>'        \
                                          + '<td>' + row[2] + '</td>'        \
                                          + '<td>' + row[5] + '</td>'        \
                                          + '<td>' + row[4] + '</td>'        \
                                          + '<td>' + cmd + '</td>'           \
                                      + '</tr>'
            jstable = jstable + '</tbody></table>'
            os.system('rm ' + GUI_PATH + '/out.txt')
            self.write({
                "status_code": 200,
                "jstable": jstable,
                "request_time": str(datetime.datetime.now()).split('.')[0]
            })
            self.finish()
        elif table_name == DISK_PARTITION:
            rows = check_output(['df', '-h']).decode('ascii').split('\n')
            rows.pop(0)
            rows.pop()
            jstable = '<table class="table"><thead><tr><th>Name</th><th>Stats</th>' + \
                '<th>Use%</th><th>Mount Path</th></tr></thead><tbody>'
            for row in rows:
                row = row.split()
                jstable = jstable + '<tr><td>' + row[0] + '</td>'                \
                                      + '<td>' + row[2] + '/' + row[1] + '</td>' \
                                      + '<td>' + row[4] + '</td>'                \
                                      + '<td>' + row[5] + '</td>'                \
                                  + '</tr>'
            jstable = jstable + '</tbody></table>'
            self.write({
                "status_code": 200,
                "jstable": jstable,
                "request_time": str(datetime.datetime.now()).split('.')[0]
            })
            self.finish()

        # for the charts: appended here?
