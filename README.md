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




## Flowchart

![Gabriele_Russo_flowchart](https://github.com/GabrieleRusso11/RT_Assignment1/blob/main/Gabriele_Russo_flowchart.png)

## Possible Improvements