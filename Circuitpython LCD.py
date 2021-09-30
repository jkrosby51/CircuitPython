import time
import board
import touchio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

# get and i2c object
i2c = board.I2C()

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)

touch_pad1 = board.A3
touch_pad2 = board.A5

touch1 = touchio.TouchIn(touch_pad1)
touch2 = touchio.TouchIn(touch_pad2)

counter = 0
photo1 = False
state1 = False
photo2 = False
state2 = False
direction = 1

while True:
###Cap Touch Counter###
    photo1 = touch1.value
    if photo1 and not state1:
            counter += direction
    state1 = photo1

    photo2 = touch2.value
    if photo2 and not state2:
            direction *= -1;
    state2 = photo2

    print("Counter: ",counter, end = " \t")
    print("Direction: ", direction)
    #1time.sleep(0.1)

###LCD###

    if direction == 1:
        lcd.print("Direction: Up  \n")
    elif direction == -1:
        lcd.print("Direction: Down\n")
    lcd.print("Presses:   ")
    lcd.print(str(counter))
    lcd.print("  \n")

