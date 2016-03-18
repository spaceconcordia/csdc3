import tornado.web

class InterfacingHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', section='interfacing')
