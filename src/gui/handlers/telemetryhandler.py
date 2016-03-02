import tornado.web

class TelemetryHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', section='telemetry')
