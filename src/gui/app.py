import tornado.ioloop
import tornado.web

import os.path
import sys

from gui_constants import *

sys.path.insert(0, HANDLERS_PATH)
from payloadhandler         import PayloadHandler
from commandshandler        import CommandsHandler
from systemhandler          import SystemHandler
from interfacinghandler     import InterfacingHandler
from sensors1handler        import Sensors1Handler
from sensors2handler        import Sensors2Handler
from sensors3handler        import Sensors3Handler
from sensors4handler        import Sensors4Handler
from sensors5handler        import Sensors5Handler
from sensors6handler        import Sensors6Handler
from batteryhandler         import BatteryHandler
from endbatteryinfohandler  import EndBatteryInfoHandler

sys.path.insert(0, SYSTEM_HANDLERS_PATH)
from timehandler            import TimeHandler
from deployantennahandler   import DeployAntennaHandler
from startpayloadhandler    import StartPayloadHandler
from logshandler            import LogsHandler
from timetagcmdhandler      import TimetagcmdHandler
from updatebinhandler       import UpdatebinHandler
from sysdatahandler         import SysdataHandler
from batteryinfohandler     import BatteryInfoHandler

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
	(r"/interfacing", InterfacingHandler),
    (r"/battery", BatteryHandler),
    (r"/endbattery", EndBatteryInfoHandler),
    (r"/sensors1", Sensors1Handler),
    (r"/sensors2", Sensors2Handler),
    (r"/sensors3", Sensors3Handler),
    (r"/sensors4", Sensors4Handler),
    (r"/sensors5", Sensors5Handler),
    (r"/sensors6", Sensors6Handler),

# system command handler
    (r"/time", TimeHandler),
    (r"/deploy-antenna", DeployAntennaHandler),
    (r"/start-payload", StartPayloadHandler),
    (r"/logs", LogsHandler),
    (r"/timetagcmd", TimetagcmdHandler),
    (r"/updatebin", UpdatebinHandler),
    (r"/sysdata", SysdataHandler),
    (r"/batteryinfo", BatteryInfoHandler),

# static logs handlers
    (r"/(.*)", tornado.web.StaticFileHandler, {'path': '/root/csdc3/src/logs/logs/'}),
], **settings)

if __name__ == "__main__":
    print('Server Running...')
    print('Press ctrl + c to close')
    application.listen(8889)
    tornado.ioloop.IOLoop.instance().start()
