import tornado.web

import sys
sys.path.insert(0, "/root/csdc3/src/logs/config_setup")

from empty_table import emptyTables

class LogsHandler(tornado.web.RequestHandler):

    def get(self):
        # Should returned a stupid dumb of data.
        # Select what to return based on sensor or subsystem or level or ALL.
        # TODO: need to work on the insert part.
        pass

    def delete(self):
        emptyTables()
