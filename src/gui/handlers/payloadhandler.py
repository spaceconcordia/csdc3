import tornado.web

class PayloadHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('payload.html')
