import tornado.web
import os

class EndBatteryInfoHandler(tornado.web.RequestHandler):
    def get(self):
        bat1_temp = []
        bat2_temp = []
        bat3_temp = []
        bat4_temp = []
        bat1_heat = []
        bat2_heat = []
        bat3_heat = []
        bat4_heat = []
   
        with open(r"/root/csdc3/src/gui/handlers/systemhandlers/battery_data.txt", "r") as f:
            rawData = f.read()
            for idxt, data in enumerate(rawData.split('\n')):
                if data != '':
                    data = data.split('|')
                    data.pop(4)
                    for idx, battery in enumerate(data):
                        battery = battery.split(' ')
                        #print(battery)
                        if idx == 0:
                            bat1_temp.append({'x': idxt*4, 'y': float(battery[0])})
                            if (battery[1] == 'True'):
                                bat1_heat.append({'x': idxt*4, 'y': 1})
                            elif (battery[1] == 'False'):
                                bat1_heat.append({'x': idxt*4, 'y': 0})
                        elif idx == 1:
                            bat2_temp.append({'x': idxt*4, 'y': float(battery[0])})
                            if (battery[1] == 'True'):
                                bat2_heat.append({'x': idxt*4, 'y': 1})
                            elif (battery[1] == 'False'):
                                bat2_heat.append({'x': idxt*4, 'y': 0})
                        elif idx == 2:
                            bat3_temp.append({'x': idxt*4, 'y': float(battery[0])})
                            if (battery[1] == 'True'):
                                bat3_heat.append({'x': idxt*4, 'y': 1})
                            elif (battery[1] == 'False'):
                                bat3_heat.append({'x': idxt*4, 'y': 0})
                        elif idx == 3:
                            bat4_temp.append({'x': idxt*4, 'y': float(battery[0])})
                            if (battery[1] == 'True'):
                                bat4_heat.append({'x': idxt*4, 'y': 1})
                            elif (battery[1] == 'False'):
                                bat4_heat.append({'x': idxt*4, 'y': 0})

        #os.system('rm /root/csdc3/src/gui/handlers/systemhandlers/battery_data.txt')
        self.render(
            'endbattery.html',
            batterydata = {
                'b1_t': bat1_temp,
                'b2_t': bat2_temp,
                'b3_t': bat3_temp,
                'b4_t': bat4_temp,
                'b1_h': bat1_heat,
                'b2_h': bat2_heat,
                'b3_h': bat3_heat,
                'b4_h': bat4_heat,
            }
        )
