import tornado.web
import sys
sys.path.append('/root/csdc3/src/logs')
sys.path.append('/root/csdc3/src/sensors')
from chomsky import *
from sensor_constants import *

class Sensors2Handler(tornado.web.RequestHandler):
    def get(self):
        finalData = []
        rawDataList = selectTelemetryLog(TEMP_PAYLOAD_BRD)
        for data in rawDataList:
            finalData.append({"x": data[3], "y": data[1]})

        self.render(
            'sensors2.html',
            sensordata = finalData
        )
