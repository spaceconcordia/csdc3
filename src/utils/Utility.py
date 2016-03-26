""" File containing various miscellaneous functions """

def twos_to_int(val, len):
    """ Convert two's complement to int """
    if val & (1 << len - 1):
      val = val - (1 << len)
    return val

def conv_bin_to_float(decimalBin, fractionalBin):
    """ convert base2 of decimal value to float """
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
