#!/usr/bin/python3

import explorerhat
import board
import busio
import adafruit_vcnl4010
import time

# # uncomment one or both of these lines to correct if any of the motors travel backwards!
# explorerhat.motor.one.invert()
# explorerhat.motor.two.invert()

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_vcnl4010.VCNL4010(i2c)

while True:
	if sensor.proximity < 2500:
		explorerhat.motor.forwards()
	elif sensor.proximity > 2501:
		explorerhat.motor.stop()
		explorerhat.motor.backwards()
		time.sleep(1.0)
		explorerhat.motor.stop()
		explorerhat.motor.one.backwards()
		time.sleep(1.0)
		explorerhat.motor.stop()
