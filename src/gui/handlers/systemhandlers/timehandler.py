import tornado.web
import datetime

class TimeHandler(tornado.web.RequestHandler):
    def get(self):
        self.write({
            "time": str(datetime.datetime.now()).split('.')[0]
        })
        self.finish()

    def post(self):
        time = getargument("sys_time", "DEFAULT")

        if time == "DEFAULT":
            self.write({
                "status_code": 400
            })
            self.finish()
        else:
            self.write({
                "status_code": 200,
                "time-set": time,
                "time-now": str(datetime.datetime.now()).split('.')[0]
            })
            self.finish()
