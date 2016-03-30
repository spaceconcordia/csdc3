import tornado.web
import sys
sys.path.append('/root/csdc3/src/logs')
sys.path.append('/root/csdc3/src/sensors')
from chomsky import *
from sensor_constants import *

class Sensors3Handler(tornado.web.RequestHandler):
    def get(self):
        sensordata = [[], [], []]

        # Retrieve triple values
        rawDataList = selectTelemetryLog(MAG_0)
        for rawData in rawDataList:
            data = str(rawData[1]).replace("(","").replace(")","").split(",")
            data = [float(i) for i in data]
            sensordata[0].append({"x": rawData[3], "y": data[0]})
            sensordata[1].append({"x": rawData[3], "y": data[1]})
            sensordata[2].append({"x": rawData[3], "y": data[2]})

        # Assign proper values
        mag0_x = sensordata[0][0]
        mag0_y = sensordata[0][1]
        mag0_z = sensordata[0][2]
        magData = [mag0_x, mag0_y, mag0_z]

        self.render(
            'sensors3.html',
            sensordata = magData
        )
