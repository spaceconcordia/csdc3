import tornado.ioloop
import tornado.web

import os.path
import sys

from gui_constants import *

sys.path.insert(0, HANDLERS_PATH)
from payloadhandler       import PayloadHandler
from commandshandler      import CommandsHandler
from systemhandler        import SystemHandler
from telemetryhandler     import TelemetryHandler
from confighandler        import ConfigHandler

sys.path.insert(0, SYSTEM_HANDLERS_PATH)
from timehandler          import TimeHandler
from deployantennahandler import DeployAntennaHandler
from startpayloadhandler  import StartPayloadHandler
from logshandler          import LogsHandler
from timetagcmdhandler    import TimetagcmdHandler
from updatebinhandler     import UpdatebinHandler
from tablehandler         import TableHandler

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

# system command handler
    (r"/time", TimeHandler),
    (r"/deploy-antenna", DeployAntennaHandler),
    (r"/start-payload", StartPayloadHandler),
    (r"/logs", LogsHandler),
    (r"/timetagcmd", TimetagcmdHandler),
    (r"/updatebin", UpdatebinHandler),
    (r"/sysdata", TableHandler),
], **settings)

if __name__ == "__main__":
    print('Server Running...')
    print('Press ctrl + c to close')
    application.listen(8889)
    tornado.ioloop.IOLoop.instance().start()
