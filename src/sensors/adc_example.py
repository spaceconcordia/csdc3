import time
from sensor_entropy import *
from sensor_manager import SensorManager

def main():
    SensorManager.init_adc()
    input()
    start = time.time()
    while time.time() - start <= 30:
        print(SensorManager.read_adc(0))
    addr = SensorEntropy.addr(ADC)
    adc_reg = SensorEntropy.reg(ADC)
    bus = SensorManager.bus
    bus.write_byte_data(addr, adc_reg['CONFIG_REG'], 0x00)


if __name__ == "__main__":
    main()
