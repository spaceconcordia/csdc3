import tornado.web

import sys
sys.path.insert(0, "/root/csdc3/src/logs/config_setup")

from empty_table import emptyTables

class LogsHandler(tornado.web.RequestHandler):

    def delete(self):
        emptyTables()
