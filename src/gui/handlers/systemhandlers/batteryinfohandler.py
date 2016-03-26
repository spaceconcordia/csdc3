import tornado.web
import sys
sys.path.append("/root/csdc3/src/power_monitoring/")
from battery_heaters_reader import BatteryHeatersReader

class BatteryInfoHandler(tornado.web.RequestHandler):
    def get(self):
        battery_data = BatteryHeatersReader()
        f = open('/root/csdc3/src/gui/handlers/systemhandlers/battery_data.txt', 'a')
        for battery in battery_data['batteries']:
            f.write(str(battery['temp']) + ' ' + str(battery['heaters']) + '|')
        f.write('\n')
        self.write({
            "status_code": 200,
            "data": battery_data
        })
        self.finish()
