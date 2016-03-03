import smbus

I2C_ADDRESS = 0x68

bus = smbus.SMBus(0)

# Set all ports in input mode
bus.write_byte(I2C_ADDRESS, 0xFF)

# Read all the input lines
high = bus.read_byte(0x1b)
low = bus.read_byte(0x1c)

value = (high << 8) + low

print value 

