import os
from datetime import timedelta

def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        uptime_string = str(timedelta(seconds = uptime_seconds))
    return uptime_string

def get_disk_usage(path):
    st = os.statvfs(path)
    free = (st.f_bavail * st.f_frsize)
    total = (st.f_blocks * st.f_frsize)
    used = (st.f_blocks - st.f_bfree) * st.f_frsize
    return free

def twos_to_int(val, len):
    if val & (1 << len - 1):
      val = val - (1 << len)
    return val

def conv_bin_to_float(decimalBin, fractionalBin):
    result = 0
    isNegative = (decimalBin >> 7) & 0x1
    if isNegative:
        result = (decimalBin ^ 0xff) + 1
        result *= -1
    else:
        result = decimalBin
    tempFract = fractionalBin
    count = 1
    fract = 0
    while count <= 8:
        fract += ((tempFract >> 7) & 0x1) * pow(2, -count)
        tempFract = tempFract << 1
        count += 1
    result += fract
    return result

def str2list(strArg):
    return strArg.replace("(","").replace(")","").split(",")

def convertLoad(inputVoltage):
    inputVoltage = (float(inputVoltage)*1.61)/(2**12)
    maxLoad = 600
    maxVoltage = 1.61
    return (inputVoltage/maxVoltage)*maxLoad

def convertStrain(Vo):
    Vo = (float(Vo)*1.61)/(2**12)
    R = 350
    Vs = 3.3
    GF = 2.12
    return ((4*R*Vo)/(Vs-2*Vo))/GF

def median(lst):
    lst = sorted(lst)
    if len(lst) < 1:
            return None
    if len(lst) %2 == 1:
            return lst[((len(lst)+1)/2)-1]
    else:
            return float(sum(lst[(len(lst)/2)-1:(len(lst)/2)+1]))/2.0

if __name__ == "__main__":
    get_disk_usage('/')
