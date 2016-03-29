f = open('loggedData.txt', 'r')
data = f.readlines()
f.close()

amp = []
volt = []
temp_bat = []
temp_bat_time = []
temp_eps = []

for idx, point in enumerate(data):
    point = point.replace('\n', '')
    if point.startswith(' I2C0_mux0_ch4_48'):
        need = (point.split(' I2C0_mux0_ch4_48')[1]).split(" power ")[0]
        temp_bat.append(need) 
        need = (point.split(' I2C0_mux0_ch4_48')[1]).split(" power ")[1]
        temp_bat_time.append(need)
    if point.startswith(' power ('):
        need = ((point.split('(')[1]).split(')')[0]).split(',')
        amp.append(float(need[1])/1000.0)
        volt.append(float(need[0])/1000.0)
    if point.startswith(' I2C0_mux0_ch4_4c'):
        need = (point.split(' I2C0_mux0_ch4_4c')[1]).split(" power ")[0]
        temp_eps.append(need)

for idx, a in enumerate(amp):
    pass#print("{x: " + str(idx)  + ", y:" + str(a)  + "},\n")

for idx, a in enumerate(volt):
    pass#print("{x: " + str(idx)  + ", y:" + str(a)  + "},\n")

for idx, a in enumerate(temp_eps):
    pass#print("{x: " + str(idx)  + ", y:" + str(a)  + "},\n")

result = []
for idx, a in enumerate(temp_bat):
    if idx > 0:
        time_prev = temp_bat_time[idx-1].split(':')[1]
        time_ = temp_bat_time[idx].split(':')[1]
        if(time_prev != time_):
            result.append(a)

for idx, a in enumerate(result):
    print("{x: " + str(idx)  + ", y:" + str(a)  + "},\n")
