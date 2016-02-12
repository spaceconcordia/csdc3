import tornado.web
import datetime
import os, uuid

__UPLOADS__ = "/root/csdc3/src/timetagged_cmds/"

class TimetagcmdHandler(tornado.web.RequestHandler):

    def post(self):
        fileinfo = self.request.files['filearg'][0]
        fname = fileinfo['filename']
        fbody = fileinfo['body']

        fh = open(__UPLOADS__ + fname, 'wb+')
        fh.write(fbody)
        fh.close()
        
        # the file under timetagged_cmds, add it to Cron
        # have a job running every 5 mins to check if things run and delete them once done
        # TODO by JB.

        # render the index page again
        self.render('index.html', section='commands')
