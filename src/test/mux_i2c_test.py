import smbus
import os

MUX_ADDRESS = 0x71

bus = smbus.SMBus(0)

def muxselect(channel):
    if channel < 0 or channel > 7:
        return False
    bus.write_byte(MUX_ADDRESS, 1 << channel)

def scan_mux():
    for i in range(8):
        muxselect(i)
        print("TCA Port:", i)
        os.system("i2cdetect -y 0")
        raw_input("\nPress any key to check the next channel...\n")

def main():
    print("Scanning i2c multiplexer")
    scan_mux()

if __name__ == "__main__":
    main()
