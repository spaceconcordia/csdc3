import tornado.web
import os

class EndBatteryInfoHandler(tornado.web.RequestHandler):
    def get(self):
        with open(r"/root/csdc3/src/gui/handlers/systemhandlers/battery_data.txt", "r") as f:
            rawData = f.readlines()
            for data in rawData:
                # Split data for temperature values and heater status
                data = data.replace(" ","|").split("|")
                battery_temps = [data[i] for i in range(0,len(data)-1,2)]
                battery_heats = [1 if data[i] == 'True' else 0 for i in range(1,len(data)-1,2)]

                print(battery_temps)

                #Perform size check (should only have 4 per line)
                if len(battery_temps) > 4 or len(battery_heats) > 4:
                    raise Exception("Invalid length")

                # Create time vector
                timeList = list(range(0,10,3))

                # Populate with parsed data for given line
                bat1_temp = [timeList[0], battery_temps[0]]
                bat2_temp = [timeList[1], battery_temps[1]]
                bat3_temp = [timeList[2], battery_temps[2]]
                bat4_temp = [timeList[3], battery_temps[3]]
                bat1_heat = [timeList[0], battery_heats[0]]
                bat2_heat = [timeList[1], battery_heats[1]]
                bat3_heat = [timeList[2], battery_heats[2]]
                bat4_heat = [timeList[3], battery_heats[3]]

        #os.system('rm /root/csdc3/src/gui/handlers/systemhandlers/battery_data.txt')
        self.render('endbattery.html') # Pass Data after Parsing It!
