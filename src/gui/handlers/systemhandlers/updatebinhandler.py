import tornado.web
import datetime
import os, uuid

BACKUP_PATH = "/root/csdc3/src/backup/"

class UpdatebinHandler(tornado.web.RequestHandler):

    def get(self): # Get backup list to choose from on rollback
        backup_list = []
        for file in os.listdir(BACKUP_PATH):
            backup_list.append(file[:-4])
        self.write({
            "status_code": 200,
            "backup_list": backup_list
        })

    def post(self):
        # Read initial arg to decide if it is roll back or binary update.
        backup_file = self.get_argument("backup_file", "None")

        if backup_file == "None": # Update binaries with file passed
            fileinfo = self.request.files['filearg'][0]
            fname = fileinfo['filename']
            fbody = fileinfo['body']

            fh = open(BACKUP_PATH + fname, 'wb+')
            fh.write(fbody)
            fh.close()

            # find the path to that name & do the replacement of files.
            # will need to make use of os.system

        else: # backup_file name is given gotta roll back.
            # find the path to that name & do the replacement of files.
            # will need to make use of os.system

        self.render('index.html', section='commands')
