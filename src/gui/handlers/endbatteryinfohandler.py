import tornado.web
import os

class EndBatteryInfoHandler(tornado.web.RequestHandler):
    def get(self):
        # parse data here: /root/csdc3/src/gui/handlers/systemhandlers/battery_data.txt'
        bat1_temp = []
        bat2_temp = []
        bat3_temp = []
        bat4_temp = []
        bat1_heat = []
        bat2_heat = []
        bat3_heat = []
        bat4_heat = []
        #os.system('rm /root/csdc3/src/gui/handlers/systemhandlers/battery_data.txt')
        self.render('endbattery.html') # Pass Data after Parsing It!
