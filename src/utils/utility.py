import os

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

def conv_bin_to_int(decimalBin, fractionalBin):
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

if __name__ == "__main__":
    get_disk_usage('/')
