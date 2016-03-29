import tornado.web
import sys
sys.path.append('/root/csdc3/src/logs')
sys.path.append('/root/csdc3/src/sensors')
from chomsky import *
from sensor_constants import *

class Sensors6Handler(tornado.web.RequestHandler):
    def get(self):
        sensordata = [[], [], []]

        # Retrieve triple values
        rawDataList = selectTelemetryLog(POWER)
        for rawData in rawDataList:
            data = str(rawData[1]).replace("(","").replace(")","").split(",")
            data = [float(i) for i in data]
            sensordata[0].append({"x": rawData[3], "y": data[0]})
            sensordata[1].append({"x": rawData[3], "y": data[1]})
            sensordata[2].append({"x": rawData[3], "y": data[2]})

        # Assign proper values
        pwr_volts  = [{"x":i["x"], "y":i["y"]/1000} for i in sensordata[1][0]]

        self.render(
            'sensors6.html',
            sensordata = pwr_volts
        )
