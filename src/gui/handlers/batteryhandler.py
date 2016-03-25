import tornado.web

class BatteryHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', section='battery')
