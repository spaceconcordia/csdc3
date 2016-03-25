import tornado.web

class BatteryInfoHandler(tornado.web.RequestHandler):
    def get(self):
        battery_data = 0#function call
        self.write({
            "status_code": 200,
            "data": battery_data
        })
        self.finish()
