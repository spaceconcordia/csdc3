import time

current = "/sys/class/i2c-dev/i2c-0/device/0-0040/hwmon/hwmon0/curr1_input"
bus = "/sys/class/i2c-dev/i2c-0/device/0-0040/hwmon/hwmon0/in1_input"

while True:
    with open(current, "r") as c, open(bus, "r") as b:
        value = c.read()
        voltage = b.read()
        print value, voltage
        time.sleep(2)
