from machine import I2C, Pin

MPU6050_REGISTER_ADDR = 0x68
MPU6050_POWER_MGMT_ADDR = 0x6B
i2c = I2C(0, scl = Pin(1), sda = Pin(0), freq = 400_000)
i2c.writeto_mem(MPU6050_REGISTER_ADDR, MPU6050_POWER_MGMT_ADDR, bytes([0x00]))
pin = Pin('LED', Pin.OUT)

def read_mpu():
    acceleration_data = i2c.readfrom_mem(MPU6050_REGISTER_ADDR, 0x3B, 6)
    gyroscope_data = i2c.readfrom_mem(MPU6050_REGISTER_ADDR, 0x43, 6)
    temperature_data = i2c.readfrom_mem(MPU6050_REGISTER_ADDR, 0x41, 2)

    ax = int.from_bytes(acceleration_data[0:2], signed = True)
    ay = int.from_bytes(acceleration_data[2:4], signed = True)
    az = int.from_bytes(acceleration_data[4:6], signed = True)
    gx = int.from_bytes(gyroscope_data[0:2], signed = True)
    gy = int.from_bytes(gyroscope_data[2:4], signed = True)
    gz = int.from_bytes(gyroscope_data[4:6], signed = True)
    tm = int.from_bytes(temperature_data, signed = True)

    return {
        'acceleration': (ax, ay, az),
        'gyroscope': (gx, gy, gz),
        'temperature': tm
    }

while True:
    pin.toggle()
    data = read_mpu()
    print('Acceleration : ', data['acceleration'])
    print('Gyrocope : ', data['gyroscope'])
    print('Temperature : ', data['temperature'])
    print()
    pin.toggle()
