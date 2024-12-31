from machine import I2C, Pin
pin = Pin('LED', Pin.OUT)


i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)
devices = i2c.scan()
pin.toggle()

if devices:
    print("I2C devices found:", [hex(device) for device in devices])
else:
    print("No I2C devices found!")