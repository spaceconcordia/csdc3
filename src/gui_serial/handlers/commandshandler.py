import tornado.web

class CommandsHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', section='commands')
