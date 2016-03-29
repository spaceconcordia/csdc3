import tornado.web
import sys
sys.path.append('/root/csdc3/src/logs')
sys.path.append('/root/csdc3/src/sensors')
from chomsky import *
from sensor_constants import *

class SensorsHandler(tornado.web.RequestHandler):
    def get(self):
        # Include results lists for sensors from sensor sweep
        # temp_eps_brd = []
        # temp_payload_brd = []
        # mag0_x = []
        # mag0_y = []
        # mag0_z = []
        # pwr_volts  = []
        # pwr_current = []
        # pwr_power = []
        # singleValueResults = [temp_eps_brd, temp_payload_brd]
        # tripleValueResults = [[mag0_x, mag0_y, mag0_z], [pwr_volts, pwr_current, pwr_power]]
        singleValueResults = [[], []]
        tripleValueResults = [[[], [], []], [[], [], []]]

        # Include sensor ids
        singleValueList = [TEMP_EPS_BRD, TEMP_PAYLOAD_BRD]
        tripleValueList = [MAG_0, POWER]

        # Retrieve single values
        for i, sensorId in enumerate(singleValueList):
            rawDataList = selectTelemetryLog(sensorId)
            for data in rawDataList:
                singleValueResults[i].append({"x": data[3], "y": data[1]})

        # Retrieve triple values
        for i, sensorId in enumerate(tripleValueList):
            rawDataList = selectTelemetryLog(sensorId)
            for rawData in rawDataList:
                data = str(rawData[1]).replace("(","").replace(")","").split(",")
                data = [float(i) for i in data]
                tripleValueResults[i][0].append({"x": rawData[3], "y": data[0]})
                tripleValueResults[i][1].append({"x": rawData[3], "y": data[1]})
                tripleValueResults[i][2].append({"x": rawData[3], "y": data[2]})

        # Assign proper values
        temp_eps_brd = singleValueResults[0]
        temp_payload_brd = singleValueResults[1]
        mag0_x = tripleValueResults[0][0]
        mag0_y = tripleValueResults[0][1]
        mag0_z = tripleValueResults[0][2]
        pwr_volts  = [{"x":i["x"], "y":i["y"]/1000} for i in tripleValueResults[1][0]]
        pwr_current = [{"x":i["x"], "y":i["y"]/1000} for i in tripleValueResults[1][1]]
        pwr_power = [{"x":i["x"], "y":i["y"]/1000000} for i in tripleValueResults[1][2]]

        self.render(
            'sensors1.html',
            sensordata = []
        )
