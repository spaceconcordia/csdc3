import tornado.web

import sys
sys.path.insert(0, '/root/csdc3/src/logs/')
from chomsky import *

class PayloadHandler(tornado.web.RequestHandler):
    def get(self):
        result = {}
        for i,item in enumerate(list(reversed(selectPayloadLog()))):
            result["p{}".format(i)] = selectPayloadData(item[0], item[1], item[2])
            if i == 4:
                break
        num_experiments = len(result)

        f = open('/root/csdc3/src/gui/templates/payload.html', 'w')

        fsec1 = open('/root/csdc3/src/gui/handlers/payload_sec1.html', 'r')
        fsec2 = open('/root/csdc3/src/gui/handlers/payload_sec2.html', 'r')
        fsec3 = open('/root/csdc3/src/gui/handlers/payload_sec3.html', 'r')

        f.write(fsec1.read())

        for i in range(num_experiments):
            f.write('var chartstrain' + str(i) + ' = new CanvasJS.Chart("chartPayloadStrain' +  str(i) + '",' +
                '{ animationEnabled: true, title:{ text: "' + str(i+1) + '. Strain VS. Time"}, axisX:{' +
                ' title: "time(sec)", intervalType: "second", interval:6 }, axisY:{ title: "Strain" }, data: [ {' +
                ' type: "spline", showInLegend: true, name: "series1", legendText: "Payload Exp ' + str(i+1) + ' - Strain",' +
                ' xValueType: "dateTime", dataPoints: (payload_data["p' + str(i) + '"])["strainConvList"] } ' +
                ' ], legend: { cursor: "pointer", itemclick: function (e) { if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) { e.dataSeries.visible = false; } else { e.dataSeries.visible = true; } ' +
                ' chartstrain' + str(i) + '.render(); }}}); chartstrain' + str(i) + '.render(); var chartload' + str(i) + ' = new CanvasJS.Chart("chartPayloadLoad' +  str(i) + '",' +
                ' { animationEnabled: true, title:{ text: " ' + str(i+1) + '. Load(N) VS. Time" }, axisX:{ title: "time(sec)", intervalType: "second", interval:6 }, ' +
                ' axisY:{ title: "Load(N)" }, data: [ { type: "spline", showInLegend: true, name: "series1", legendText: "Payload Exp ' + str(i+1) + ' - Load", xValueType: "dateTime", dataPoints: (payload_data["p' + str(i) + '"])["loadConvList"]' +
                ' } ], legend: { cursor: "pointer", itemclick: function (e) { if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) { e.dataSeries.visible = false; } else { e.dataSeries.visible = true; } chartload' + str(i) + '.render();' +
                ' }}}); chartload' + str(i) + '.render(); var charttemp' + str(i) + ' = new CanvasJS.Chart("chartPayloadTemp' +  str(i) + '",' +
                ' { animationEnabled: true, title:{ text: " ' + str(i+1) + '. Temp VS. Time" }, axisX:{ title: "time(sec)", intervalType: "second", interval:6 }, axisY:{ title: "Temperature °C" }, data: [' +
                ' { type: "spline", showInLegend: true, name: "series1", legendText: "Payload Exp ' + str(i+1) + ' - Temperature", xValueType: "dateTime", dataPoints: (payload_data["p' + str(i) + '"])["tempList"]' +
                ' } ], legend: { cursor: "pointer", itemclick: function (e) { if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) { e.dataSeries.visible = false; } else { e.dataSeries.visible = true; } charttemp' + str(i) + '.render(); }} }); charttemp' + str(i) + '.render();'
            )

        f.write(fsec2.read())

        f.write('<div class="main payload"><div class="row"><div class="col-xs-5"></div><div class="col-xs-2"><div id="batterydata" class="dropdown">' +
            '<button id="bat-data-selec-btn" class="btn btn-default dropdown-toggle" type="button" data-toggle="dropdown">Payload Experiment Data Num' +
            '<span class="caret"></span></button><ul class="dropdown-menu">'
        )

        for i in range(num_experiments):
            f.write('                        <li><a id="pay' + str(i+1) + '-data" href="#">Payload Experiment ' + str(i+1)  + '</a></li>\n')
        
        f.write('</ul></div></div><div class="col-xs-5"></div></div>')

        for i in range(num_experiments):
            f.write('            <div id="payloadrow' + str(i) + '" class="row">\n')
            f.write('                <div class="col-xs-4"><div id="chartPayloadStrain' +  str(i) + '" style="height: 400px; width: 100%;"></div></div>\n')
            f.write('                <div class="col-xs-4"><div id="chartPayloadLoad' +  str(i) + '" style="height: 400px; width: 100%;"></div></div>\n')
            f.write('                <div class="col-xs-4"><div id="chartPayloadTemp' +  str(i) + '" style="height: 400px; width: 100%;"></div></div>\n')
            f.write('            </div>\n')

        f.write(fsec3.read())

        f.close()
        fsec1.close()
        fsec2.close()
        fsec3.close()

        self.render('payload.html', payloaddata = result)
