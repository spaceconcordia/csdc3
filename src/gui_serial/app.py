import tornado.ioloop
import tornado.web

import tornado.httpserver
import tornado.websocket
import tornado.gen
from tornado.options import define, options

import serialworker

import os.path
import sys
import multiprocessing

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
from sysdatahandler       import SysdataHandler

define("port", default=8080, help="run on the given port", type=int)

clients = [] 

input_queue = multiprocessing.Queue()
output_queue = multiprocessing.Queue()

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    debug=True
)

application = tornado.web.Application([
#    (r"/", SystemHandler),
#    (r"/system", SystemHandler),
    (r"/commands", CommandsHandler),
	(r"/payload", PayloadHandler),
	(r"/telemetry", TelemetryHandler),
    (r"/config", ConfigHandler),

# system command handler
#    (r"/time", TimeHandler),
#    (r"/deploy-antenna", DeployAntennaHandler),
#    (r"/start-payload", StartPayloadHandler),
#    (r"/logs", LogsHandler),
#    (r"/timetagcmd", TimetagcmdHandler),
#    (r"/updatebin", UpdatebinHandler),
#    (r"/sysdata", SysdataHandler),

# static logs handlers
     (r"/(.*)", tornado.web.StaticFileHandler, {'path': '/root/csdc3/src/logs/logs/'}),
], **settings)

if __name__ == "__main__":
	## start the serial worker in background (as a deamon)
    sp = serialworker.SerialProcess(input_queue, output_queue)
    sp.daemon = True
    sp.start()
    tornado.options.parse_command_line()

    httpServer = tornado.httpserver.HTTPServer(application)
    httpServer.listen(options.port)
    print("Listening on port:", options.port)
    print('Server Running...')
    print('Press ctrl + c to close')

    mainLoop = tornado.ioloop.IOLoop.instance()
	## adjust the scheduler_interval according to the frames sent by the serial port
    scheduler_interval = 100
    scheduler = tornado.ioloop.PeriodicCallback(checkQueue, scheduler_interval, io_loop = mainLoop)
    scheduler.start()
    mainLoop.start()
