"""CircuitPython Essentials Servo standard servo example"""
# https://learn.adafruit.com/circuitpython-essentials/circuitpython-servo
import time
import board
import pwmio
import touchio
import servo

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
#
#Servo
#
######
#pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
#my_servo = servo.Servo(pwm)
#
#while True:
#    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
#        my_servo.angle = angle
#        time.sleep(0.05)
#    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
#        my_servo.angle = angle
#        time.sleep(0.05)
######

#
# Cap Touch
#

touch_A1 = touchio.TouchIn(board.A2)  # Not a touch pin on Trinket M0!
touch_A2 = touchio.TouchIn(board.A3)  # Not a touch pin on Trinket M0!

while True:
    if touch_A1.value:
        print("Touched A2!")
        dot.fill((255,0,0))
    if touch_A2.value:
        print("Touched A3!")
        dot.fill((0,0,255))
    time.sleep(0.05)
