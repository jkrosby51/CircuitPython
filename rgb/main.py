import time
import board
from rgb import LED   # import the LED class from the rgb module

# 1st LED pins
blueLEDPin = board.D9
greenLEDPin = board.D10
redLEDPin = board.D11

# 2nd LED pins
blueLEDPin2 = board.D2
greenLEDPin2 = board.D3
redLEDPin2 = board.D4

# 1st LED initiation
myBlueLED = LED(blueLEDPin)
myGreenLED = LED(greenLEDPin)
myRedLED = LED(redLEDPin)

# 2nd LED initiation
myBlueLED2 = LED(blueLEDPin2)
myGreenLED2 = LED(greenLEDPin2)
myRedLED2 = LED(redLEDPin2)

while True:
    # 1st LED cycle
    myGreenLED.fade()
    time.sleep(1)
    myBlueLED.fade()
    time.sleep(1)
    myRedLED.fade()
    time.sleep(1)

    # 2nd LED cycle
    myGreenLED2.fade()
    time.sleep(1)
    myBlueLED2.fade()
    time.sleep(1)
    myRedLED2.fade()
    time.sleep(1)