import board
import busio
import adafruit_vcnl4010
import time

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_vcnl4010.VCNL4010(i2c)

while True:
	print(f'Proximity: {sensor.proximity}')
	time.sleep(0.2)
