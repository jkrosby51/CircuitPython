# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_hcsr04
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
rgbValue1 = 0
rgbValue2 = 0


while True:
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("Retrying!")
    dot.fill(colorwheel(rgbValue))
    time.sleep(0.1)
    if sonar.distance > 5 and sonar.distance < 20:
     rgbValue1 = simpleio.map_range(sonar.distance, 0, 255, 5, 20)

