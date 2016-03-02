import tornado.web

import os
import datetime

from subprocess    import check_output
from gui_constants import *

RAM_INTENSIVE_PROCESSES =      "ramIntensProc"
CPU_INTENSIVE_PROCESSES =      "cpuIntensProc"
DISK_PARTITION =               "diskPart"
RAM_USAGE_CHART =              "ramUsageCharts"
CPU_AVG_LOAD_CHART =           "cpuAvgLoadCharts"
CPU_UTIL_CHART =               "cpuUtilizationCharts"

class SysdataHandler(tornado.web.RequestHandler):
    def get(self):
        data_name = self.get_argument("data_name", "None")

        if data_name == "None" or \
            (data_name != RAM_INTENSIVE_PROCESSES
                and  data_name != CPU_INTENSIVE_PROCESSES
                    and  data_name != DISK_PARTITION
                        and  data_name != RAM_USAGE_CHART
                            and  data_name != CPU_AVG_LOAD_CHART
                                and  data_name != CPU_UTIL_CHART):
            self.write({
                "status_code": 400,
                "message": "Illegal input arguments",
                "description": "data_name was not passed",
            })
            self.finish()

        elif data_name == RAM_INTENSIVE_PROCESSES:
            os.system('ps aux | sort -rk 4,4 | head -n 7 > ' + GUI_PATH + '/out1.txt')
            jstable = '<table class="table"><thead><tr><th>PID</th><th>User</th>' + \
                '<th>Mem%</th><th>Rss</th><th>Vsz</th><th>Cmd</th></tr></thead><tbody>'
            with open(GUI_PATH + '/out1.txt', 'r') as f:
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
            os.system('rm ' + GUI_PATH + '/out1.txt')
            self.write({
                "status_code": 200,
                "jstable": jstable,
                "request_time": str(datetime.datetime.now()).split('.')[0]
            })
            self.finish()

        elif data_name == CPU_INTENSIVE_PROCESSES:
            os.system('ps aux | sort -rk 3,3 | head -n 7 > ' + GUI_PATH + '/out2.txt')
            jstable = '<table class="table"><thead><tr><th>PID</th><th>User</th>' + \
                '<th>Cpu%</th><th>Rss</th><th>Vsz</th><th>Cmd</th></tr></thead><tbody>'
            with open(GUI_PATH + '/out2.txt', 'r') as f:
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
            os.system('rm ' + GUI_PATH + '/out2.txt')
            self.write({
                "status_code": 200,
                "jstable": jstable,
                "request_time": str(datetime.datetime.now()).split('.')[0]
            })
            self.finish()

        elif data_name == DISK_PARTITION:
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

        elif data_name == RAM_USAGE_CHART:
            os.system('free -m > ' + GUI_PATH + '/out3.txt')
            with open(GUI_PATH + '/out3.txt', 'r') as f:
                content = f.read().split('\n')
                content.pop()
                ramUsageVals = content.pop(1).split()
                ramUsageRatioVal = float(ramUsageVals[2])/float(ramUsageVals[1])
            os.system('rm ' + GUI_PATH + '/out3.txt')
            self.write({
                "status_code": 200,
                "timeseries_data": ramUsageRatioVal*100,
                "free_ram": ramUsageVals[3],
                "used_ram": ramUsageVals[2],
                "total_ram": ramUsageVals[1],
                "request_time": str(datetime.datetime.now()).split('.')[0]
            })
            self.finish()

        elif data_name == CPU_AVG_LOAD_CHART:
            os.system('uptime > ' + GUI_PATH + '/out4.txt')
            with open(GUI_PATH + '/out4.txt', 'r') as f:
                loadAvgsInfo = f.read().split(':')
                loadAvgs = loadAvgsInfo[len(loadAvgsInfo)-1].replace('\n','').split(',')
            os.system('rm ' + GUI_PATH + '/out4.txt')
            self.write({
                "status_code": 200,
                "timeseries_data1": float(loadAvgs[0]),
                "timeseries_data5": float(loadAvgs[1]),
                "timeseries_data15": float(loadAvgs[2]),
                "request_time": str(datetime.datetime.now()).split('.')[0]
            })
            self.finish()

        elif data_name == CPU_UTIL_CHART:
            os.system('mpstat > ' + GUI_PATH + '/out5.txt')
            with open(GUI_PATH + '/out5.txt', 'r') as f:
                content = f.read().split('\n')
                content.pop()
                mpstatVals = content.pop(3).split()
                idleVal = mpstatVals[len(mpstatVals)-1]
                cpuUtilVal = 100 - float(idleVal)
            os.system('rm ' + GUI_PATH + '/out5.txt')
            self.write({
                "status_code": 200,
                "timeseries_data": cpuUtilVal,
                "request_time": str(datetime.datetime.now()).split('.')[0]
            })
            self.finish()
