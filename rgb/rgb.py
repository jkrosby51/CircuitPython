import time
import board
import pwmio

class LED:
    '''LED is a class designed for a single color LED to fade in and out'''

    def __init__(self, ledpin):
       # Initiating LED class object
       self.led = pwmio.PWMOut(ledpin, frequency=5000, duty_cycle=0)


    def fade(self):
        for i in range(255):
            if i < (128):       # First half of cycle, starts at zero brightness and moves up to 65535 (max).
                self.led.duty_cycle = int(i * 65535 / (255/2)) # fade off
            elif i == 128:      # Holds at max brightness for 1s
               time.sleep(1)
            else:               # Second half of cycle, starts at 65535 brightness (max) and moves down to zero.
                self.led.duty_cycle = 65535 - int((i-128) * 65535 / (255/2))

            time.sleep(0.01)    # Holds at min brightness for 1s