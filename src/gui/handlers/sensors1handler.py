import tornado.web
import sys
sys.path.append('/root/csdc3/src/logs')
sys.path.append('/root/csdc3/src/sensors')
from chomsky import *
from sensor_constants import *

class Sensors1Handler(tornado.web.RequestHandler):
    def get(self):
        sensorData = []
        rawDataList = selectTelemetryLog(TEMP_EPS_BRD)
        for data in rawDataList:
            sensorData.append({"x": data[3], "y": data[1]})
        print(rawDataList)
        self.render(
            'sensors1.html',
            sensordata = sensorData
        )
