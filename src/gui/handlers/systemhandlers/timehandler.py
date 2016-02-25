import tornado.web
import datetime

import os

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
