import tornado.ioloop
import tornado.web

import os.path
import sys

sys.path.insert(0, "/var/www/Aleksandr/src/handlers")
from payloadhandler   import PayloadHandler
from commandshandler  import CommandsHandler
from systemhandler    import SystemHandler
from telemetryhandler import TelemetryHandler
from confighandler    import ConfigHandler
from inputhandler     import InputHandler
from paramhandler     import ParamHandler

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    debug=True
)

application = tornado.web.Application([
    (r"/", SystemHandler),
    (r"/system", SystemHandler),
    (r"/commands", CommandsHandler),
	(r"/payload", PayloadHandler),
	(r"/telemetry", TelemetryHandler),
    (r"/config", ConfigHandler),
    (r"/test/([0-9]+)", InputHandler),
    (r"/param", ParamHandler)
], **settings)

if __name__ == "__main__":
    print('Server Running...')
    print('Press ctrl + c to close')
    application.listen(8889)
    tornado.ioloop.IOLoop.instance().start()
