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
Make the neopixel red

[Full Code](https://github.com/jkrosby51/CircuitPython/blob/main/HelloWorld.py)

### Evidence
Pictures / Gifs of your work should go here

### Wiring
Make an account with your google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://www.markdownguide.org/basic-syntax/)

### Reflection
Challenges with updates made it difficult to complete the assignment at first but when that was fixed it was easy.


## CircuitPython_Servo

### Description & Code
Using capacative touch to move a servo.

This code is for controlling the angle of the servo with the cap touch
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
[Video](https://github.com/jkrosby51/CircuitPython/blob/main/Videos/ServoCapTouch%20-%20Video.mp4)
### Wiring
![Wiring](https://github.com/jkrosby51/CircuitPython/blob/main/Images/ServoCapTouch%20Wiring.jpg)
### Reflection
I learned more about the basics of Circuit Python, as well as how to use capacative touch and how it can be useful in the future.


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
