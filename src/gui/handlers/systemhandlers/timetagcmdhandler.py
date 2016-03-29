import tornado.web
import datetime
import os, uuid

CRON_PATH =   "/root/csdc3/src/cron/"
import sys
sys.path.insert(0, CRON_PATH)
from cron_manager import CronManager

TIMETAGGED_CMD_PATH = "/root/csdc3/src/timetagged_cmds/"

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
            os.chmod(TIMETAGGED_CMD_PATH + fname, 1)
            # render the index page again
            self.render('index.html', section='commands')
