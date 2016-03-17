import tornado.web

class SensorsHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', section='sensors')
