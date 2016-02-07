import tornado.web

class InputHandler(tornado.web.RequestHandler):
    def get(self, input):
        self.write({
            "input pass equals": input
        })
        self.finish()