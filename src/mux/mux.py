import smbus

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
        print("Check i2c devices...")
        raw_input()

def main():
    print("Scanning i2c multiplexer")
    scan_mux()

if __name__ == "__main__":
    main()
