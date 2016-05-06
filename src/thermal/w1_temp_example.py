import sys
sys.path.append('/root/csdc3/lib/ablib')

from ablib_python3 import DS18B20
import time

w1_addr = ["00000188490c", "000001885520"]
w1_addr = ["000001aaf87d"]
sensors = []

def main():
    for addr in w1_addr:
        sensors.append(DS18B20(addr))

    start_time = time.time()
    end_time = 5
    with open("temperature.txt", "w") as f:
        while True:
            for sensor in sensors:
                print("Temp=%.2f C" % (sensor.getTemp())),
            f.write(str(sensor.getTemp()) + '\n')
            time.sleep(0.1)
            print

if __name__ == "__main__":
    main()
