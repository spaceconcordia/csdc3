import tornado.web
import os

class BatteryHandler(tornado.web.RequestHandler):
    def get(self):
        os.system('rm /root/csdc3/src/gui/handlers/systemhandlers/battery_data.txt')
        self.render('index.html', section='battery')
