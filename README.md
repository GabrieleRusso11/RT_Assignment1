# Gabriele Russo's first assignment for the Research Track 1 course (Mat. 5180813)

## Installing and running
The simulator requires a Python 2.7 installation, the [pygame](http://pygame.org/) library, [PyPyBox2D](https://pypi.python.org/pypi/pypybox2d/2.1-r331), and [PyYAML](https://pypi.python.org/pypi/PyYAML/).

Once everything is installed, run the progamm by typing on the shell :

```
 python2 run.py AssignmentRussoGabriele.py 
 ```
 

## Introduction
The aim of this project is that the robot has to move in an arena (image below) in which there are two types of token :

* Silver Token ( the robot must reach it )
* Golden Token ( the robot must avoid it )

The robot must avoid the golden tokens, which compose the walls of the path, and instead it must take the silver tokens, randomly located in the arena between the golden token walls.
Once it grabs a silver token it must turn 180 degrees and so release the silver token behind itself, then it goes on searching another silver token in the path so on and so forth.

![Arena](https://github.com/GabrieleRusso11/RT_Assignment1/blob/main/images/Arena.png)

## How it works 

My program achieve the aim using four principal categories of functions :

* Robot Movement Functions
* Orientation Functions
* Distance Functions 
* Token Management Functions

### Robot Movement Functions

In this category there are the functions that let the robot to move in the arena :

```python
def drive(speed):
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
```
This function active the motors and let the robot to go ahead.

```python
def stop() : 
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0
```
This function sets to zero the speed motors and so it stops the robot movement

```python
def reverse(speed,seconds) : 
    drive(-speed)
    time.sleep(seconds)
    stop()
```
This function uses a combination of the `drive()` function and the `stop()` function to let the robot to go in the reverse direction.

```python
def turn(speed,seconds) :
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0
```
This function let the robot to turn towards a generic direction.

### Orientation Functions

In this category there are functions that use the library function `heading` to align the robot to a specific orientation.

Heading returns the angular robot position, it angle range goes from 0 to -180 and from 180 to 0, so I have the following angular situation : 

![Robot](https://github.com/GabrieleRusso11/RT_Assignment1/blob/main/images/Heading.jpg)

I take the heading values through the `angle()` function : 

```python
def angle() :
    return (R.heading*(180/math.pi))
```

In this category there is the `semicircle()` function that thanks to the `rotate_0()`, `rotate_90()`, `rotate_minus_90()` and `rotate_180()` functions let the robot to turn 180 degrees in the correct direction seeing in which position the robot is in that precise instant and turning in the opposite angular position :

![semicircle_rotate_functions](https://github.com/GabrieleRusso11/RT_Assignment1/blob/main/images/semicircle_rotate_functions.png)

Then there are the `alignment_0()`, `alignment_90()`, `alignment_minus_90()` and `alignment_180()` that conceptually are very similar to the rotate functions but in this case they are used to detecd whether there are a wall on the left or on the right and turn 90 degrees in the correct direction ( i.e. the direction where there are not walls ). So in a nutshell the alignment functions are used to let the robot to go around the bends. (the function flowcharts are shown below).

`alignment_0()` :

![alignment0](https://github.com/GabrieleRusso11/RT_Assignment1/blob/main/images/alignment0.png)

`alignment_90()` :

![alignment90](https://github.com/GabrieleRusso11/RT_Assignment1/blob/main/images/alignment90.png)

`alignment_minus_90()` :

![alignmentminus90](https://github.com/GabrieleRusso11/RT_Assignment1/blob/main/images/alignmentminus90.png)

`alignment_180()` :

![alignment180](https://github.com/GabrieleRusso11/RT_Assignment1/blob/main/images/alignment180.png)

### Distance functions



## Flowchart

![Gabriele_Russo_flowchart](https://github.com/GabrieleRusso11/RT_Assignment1/blob/main/Gabriele_Russo_flowchart.png)

## Possible Improvements