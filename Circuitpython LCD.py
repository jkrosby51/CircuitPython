import time
import board
import touchio

touch_pad1 = board.A3
touch_pad2 = board.A5

touch1 = touchio.TouchIn(touch_pad1)
touch2 = touchio.TouchIn(touch_pad2)

bool tOneOld = False
bool tOneCurrent = False
bool tTwoOld = False
bool tTwoCurrent = False

while True:
    t1Old = t1Current