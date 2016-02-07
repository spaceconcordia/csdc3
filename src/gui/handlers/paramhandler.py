import tornado.web

class ParamHandler(tornado.web.RequestHandler):
    def get(self):
        self.write({
            "argument passs equals ": self.get_argument("param", "paramNotPassed")
        })
        self.finish()