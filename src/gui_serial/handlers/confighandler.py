import tornado.web

class ConfigHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', section='config')
