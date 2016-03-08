import tornado.web

class SystemHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', section='system')

    def post(self):
        self.write({ "status" : "Ario boy" })
        self.finish()
