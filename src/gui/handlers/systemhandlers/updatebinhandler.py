import tornado.web
import datetime
import os

from bak_constants import *

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

            if not(fname in SRC_LISTS):
                self.write({
                    "status_code": 400,
                    "message": "Illegal input arguments",
                    "description": "data_name was not passed"
                })
                self.finish()
            else:
                for tuple in SRC_TUPLES:
                    if fname in tuple[0]:
                        file_to_update = tuple[1] + fname
                        os.system("mv " + file_to_update + " " + BACKUP_PATH + fname + ".bak")
                        fh = open(file_to_update, 'wb+')
                        fh.write(fileinfo['body'])
                        fh.close()
        else: # backup_file name is given gotta roll back.
            pass
        self.render('index.html', section='commands')
