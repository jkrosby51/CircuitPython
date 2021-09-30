# CircuitPython
 The follwing files are my first foray into CircuitPython.
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---


## Hello_CircuitPython

### Description & Code
Using CircuitPython to change the RGB value of the Metro Express neopixel.

[Full Code](https://github.com/jkrosby51/CircuitPython/blob/main/HelloWorld.py)

### Evidence
![Red LED](https://github.com/jkrosby51/CircuitPython/blob/main/Images/HelloCircuitPython%20Evidence.jpg)

### Wiring
N/A

### Reflection
Once the Metro was fully updated and the correct libraries were found, this assignment was easy.


## CircuitPython_Servo

### Description & Code
Using capacative touch to move a servo.

I used this part of the code in order to move the servo when the wires were touched, without letting the angle value go past 180 or 0.
```python
    if angle < 180 and touch1.value:
        angle = angle + 5
        my_servo.angle = angle
        print("angle: ", angle)
    if angle > 0 and touch2.value:
        angle = angle - 5
        my_servo.angle = angle
        print("angle: ", angle)
```
[Full Code](https://github.com/jkrosby51/CircuitPython/blob/main/ServoCapTouch.py)

### Evidence
![gif](https://github.com/jkrosby51/CircuitPython/blob/main/Images/ServoCapTouch%20Gif.gif)
### Wiring
![Wiring](https://github.com/jkrosby51/CircuitPython/blob/main/Images/ServoCapTouch%20Wiring.jpg)
### Reflection
Cap touch can be very useful for interaction (i.e. buttons) and is simple to code.


## CircuitPython_Distance_Sensor

### Description & Code
Translating Distance values from a hcsr04 to rgb values for a neopixel.

This section of the code was used to turn the Distance measurement to rgb values used to control the neopixel on the board.
```python
elif cm < 20:
 redValue = simpleio.map_range(cm, 5, 20, 255, 0)
 greenValue = 0
 blueValue = simpleio.map_range(cm, 5, 20, 0, 255)
 print("RGB: (", redValue, ", ", greenValue, ", ", blueValue, ")")
 dot.fill((int(redValue), int(greenValue), int(blueValue)))
elif cm < 35:
 redValue = 0
 greenValue = simpleio.map_range(cm, 20, 35, 0, 255)
 blueValue = simpleio.map_range(cm, 20, 35, 255, 0)
 print("RGB: (", redValue, ", ", greenValue, ", ", blueValue, ")")
 dot.fill((int(redValue), int(greenValue), int (blueValue)))
```
[Full Code](https://github.com/jkrosby51/CircuitPython/blob/main/DistanceRGB.py)

### Evidence
![Distance Sensor](https://github.com/jkrosby51/CircuitPython/blob/main/Images/DistanceRGB%20Gif.gif)

### Wiring
![DistanceRGB Wiring](https://github.com/jkrosby51/CircuitPython/blob/main/Images/DistanceRGB%20Wiring.png)
### Reflection
Simpleio Mapping can be useful for mapping values to different formats to be used as an input for another function. Keeping code organized makes it much easier to find errors and to avoid them in the first place.


## CircuitPython_Photointerrupter 

### Description & Code
This project counted how many times the photointeruppter detected interupts.

This part of the code was in charge of making sure that it only counted once per interrupt (as opposed to it counting every tick where there was something blocking the laser)
```python
photo = interrupter.value
    if photo and not state:
            counter += 1
    state = photo
```

[Full Code](https://github.com/jkrosby51/CircuitPython/blob/main/Photointerrupters.py)

### Evidence

![photointerruptergif](https://github.com/jkrosby51/CircuitPython/blob/main/Images/PhotointerrupterGif.gif)
![photointerrupterserial](https://github.com/jkrosby51/CircuitPython/blob/main/Images/PhotointerrupterSerial.png)
### Wiring

![photointerrupterwiring](https://github.com/jkrosby51/CircuitPython/blob/main/Images/PhotointerrupterWiring.jpg)

### Reflection

The photointerrupter is a useful way to take inputs. In order to code the counter I had to make sure that it only counted when the sensor noticed a change in states, which I showed above.


## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
