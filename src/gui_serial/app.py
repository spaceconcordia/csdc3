import tornado.ioloop
import tornado.web

import tornado.httpserver
import tornado.websocket
import tornado.gen
from tornado.options  import define, options

import os
import uuid
import os.path
import datetime
import serialworker
import multiprocessing

import sys
sys.path.insert(0, "/root/csdc3/src/logs/config_setup")
from empty_table import emptyTables
sys.path.insert(0, "/root/csdc3/src/payload")
#from payload import Payload
sys.path.insert(0, "/root/csdc3/src/cron/")
from cron_manager import CronManager

from gui_constants import *
from bak_constants import *
from subprocess    import check_output

TIMETAGGED_CMD_PATH =          "/root/csdc3/src/timetagged_cmds/"
BACKUP_PATH =                  "/root/csdc3/src/backup/"
RAM_INTENSIVE_PROCESSES =      "ramIntensProc"
CPU_INTENSIVE_PROCESSES =      "cpuIntensProc"
DISK_PARTITION =               "diskPart"
RAM_USAGE_CHART =              "ramUsageCharts"
CPU_AVG_LOAD_CHART =           "cpuAvgLoadCharts"
CPU_UTIL_CHART =               "cpuUtilizationCharts"

define("port", default=8080, help="run on the given port", type=int)

clients = []

input_queue = multiprocessing.Queue()
output_queue = multiprocessing.Queue()

class TelemetryHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', section='telemetry')

class SystemHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', section='system')

class PayloadHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', section='payload')

class ConfigHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', section='config')

class CommandsHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', section='commands')

class DeployAntennaHandler(tornado.web.RequestHandler):
    def put(self):
        pass

class LogsHandler(tornado.web.RequestHandler):
    def delete(self):
        emptyTables()

class StartPayloadHandler(tornado.web.RequestHandler):
    def put(self):
        # start Payload! call payload job 
        #payload = Payload(2)
        #payload.start()
        pass

class TimeHandler(tornado.web.RequestHandler):
    def get(self):
        self.write({
            "time": str(datetime.datetime.now()).split('.')[0]
        })
        self.finish()

    def post(self):
        time_to_set = self.get_argument("sys_time", "DEFAULT")
        os.system("date -s '" + time_to_set + "'")

        if time_to_set == "DEFAULT":
            self.write({
                "status_code": 400
            })
            self.finish()
        else:
            self.write({
                "status_code": 200,
                "time-set": time_to_set
            })
            self.finish()

class TimetagcmdHandler(tornado.web.RequestHandler):
    def post(self):
        fileinfo = self.request.files['filearg'][0]
        fname = fileinfo['filename']
        fbody = fileinfo['body']

        fh = open(TIMETAGGED_CMD_PATH + fname, 'wb+')
        fh.write(fbody)
        fh.close()

        rundatetime = self.get_argument("timetag", "oops")

        runtime = rundatetime.split(" ")[1]
        runhr = runtime.split(":")[0]
        runmin =  runtime.split(":")[1]

        rundate = rundatetime.split(" ")[0]
        runmonth = rundate.split("/")[0]
        runday = rundate.split("/")[1]
        runyear = rundate.split("/")[2]

        if (runtime == "oops"):
            self.write({
                "status_code": 400,
                "message": "Illegal input arguments",
                "description": "data_name was not passed"
            })
            self.finish()
        else:
            cron_mana = CronManager()
            cron_mana.add_or_update_job(int(runmin),              \
                                        int(runhr),               \
                                        int(runday),              \
                                        int(runmonth),            \
                                        '*',                      \
                                        TIMETAGGED_CMD_PATH + fname)
            cron_mana.update_cron_file()
            # render the index page again
            self.render('index.html', section='commands')

class UpdatebinHandler(tornado.web.RequestHandler):
    def get(self): # Get backup list to choose from on rollback
        backup_list = []
        for file in os.listdir(BACKUP_PATH):
            backup_list.append(file[:-4])
        self.write({
            "status_code": 200,
            "backup_list": backup_list
        })

    def post(self):
        # Read initial arg to decide if it is roll back or binary update.
        backup_file = self.get_argument("backup_file", "None")

        if backup_file == "None": # Update binaries with file passed
            fileinfo = self.request.files['filearg'][0]
            fname = fileinfo['filename']

            if not(fname in SRC_LISTS):
                self.write({
                    "status_code": 400,
                    "message": "Illegal input arguments",
                    "description": "the file you are trying to update doesn't "
                })
                self.finish()
            else:
                for tuple in SRC_TUPLES:
                    if fname in tuple[0]:
                        file_to_update = tuple[1] + fname
                        os.system("mv " + file_to_update + " " + BACKUP_PATH + fname + ".bak")
                        fh = open(file_to_update, 'wb+')
                        fh.write(fileinfo['body'])
                        fh.close()
        else: # backup_file name is given gotta roll back.
            for tuple in SRC_TUPLES:
                if backup_file in tuple[0]:
                    os.system("mv " + BACKUP_PATH + backup_file + ".bak" + " " + tuple[1] + backup_file)

        self.render('index.html', section='commands')

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

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    debug=True
)

application = tornado.web.Application([
    (r"/", SystemHandler),
    (r"/system", SystemHandler),
    (r"/commands", CommandsHandler),
	(r"/payload", PayloadHandler),
	(r"/telemetry", TelemetryHandler),
    (r"/config", ConfigHandler),

# system command handler
#    (r"/time", TimeHandler),
#    (r"/deploy-antenna", DeployAntennaHandler),
#    (r"/start-payload", StartPayloadHandler),
#    (r"/logs", LogsHandler),
#    (r"/timetagcmd", TimetagcmdHandler),
#    (r"/updatebin", UpdatebinHandler),
#    (r"/sysdata", SysdataHandler),

# static logs handlers
     (r"/(.*)", tornado.web.StaticFileHandler, {'path': '/root/csdc3/src/logs/logs/'}),
], **settings)

## check the queue for pending messages, and rely that to all connected clients
def checkQueue():
	if not output_queue.empty():
		message = output_queue.get()
		for c in clients:
			c.write_message(message)

if __name__ == "__main__":
	## start the serial worker in background (as a deamon)
    sp = serialworker.SerialProcess(input_queue, output_queue)
    sp.daemon = True
    sp.start()
    tornado.options.parse_command_line()

    httpServer = tornado.httpserver.HTTPServer(application)
    httpServer.listen(options.port)
    print("Listening on port:", options.port)
    print('Server Running...')
    print('Press ctrl + c to close')

    mainLoop = tornado.ioloop.IOLoop.instance()
	## adjust the scheduler_interval according to the frames sent by the serial port
    scheduler_interval = 100
    scheduler = tornado.ioloop.PeriodicCallback(checkQueue, scheduler_interval, io_loop = mainLoop)
    scheduler.start()
    mainLoop.start()
