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
![Red LED](https://github.com/jkrosby51/CircuitPython/blob/main/Images/20210914_103706.jpg)

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
![gif](https://github.com/jkrosby51/CircuitPython/blob/main/Images/ezgif-4-b1361fa9f47f.gif)
### Wiring
![Wiring](https://github.com/jkrosby51/CircuitPython/blob/main/Images/ServoCapTouch%20Wiring.jpg)
### Reflection
Cap touch can be very useful for interaction (i.e. buttons) and is simple to code.


## CircuitPython_Distance_Sensor

### Description & Code
Translating Distance values from a hcsr04 to rgb values for a neopixel.
```python
Code goes here

```

### Evidence

### Wiring

### Reflection


## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
