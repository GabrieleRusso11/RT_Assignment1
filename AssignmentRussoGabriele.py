from __future__ import print_function
import time
import math
from sr.robot import *

"""++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""

"""---------------- R.T.1 First Assignment --------------------"""

"""---------- By The Robotics Engineering Student -------------"""

"""--------------------- RUSSO GABRIELE -----------------------"""

"""++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""


"""------------------------Variables---------------------------"""

""" Threshold for the control of the orientation """
a_th = 4.0 
""" Threshold for the control of the linear distance """
d_th = 0.4
""" Instance of the class Robot """
R = Robot()

"""-------------------Robot Moving Functions--------------------"""
"""
drive is a function used to set a linear velocity
Arg : speed (init) is the speed of the wheels

""" 
def drive(speed):
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    
"""
stop is a function used to stop the robot's motors 
setting their velocity to zero
Arg : no arguments

"""
def stop() : 
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

"""
reverse is a function used to reverse the direction 
of travel
Arg : speed (int) is the speed of the wheels
      seconds (int) is the time interval before
      stopping the motors
"""
def reverse(speed,seconds) : 
    drive(-speed)
    time.sleep(seconds)
    stop()

"""
turn is a function used to setting the robot angular 
velocity
Arg : speed (int) is the speed of the wheels
      seconds (int) is the time interval before
      stopping the motors
"""
def turn(speed,seconds) :
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

"""---------------------Orientation Functions-----------------------"""
"""
Angle is a function which returns the robot angular position 
through the robot library function heading  

"""
def angle() :
    return (R.heading*(180/math.pi)) #heading gives the angle in radiants
    #so I convert it in degrees

"""
alignment_0, alignment_90, alignment_180 and alignment_minus_90
are functions used to align the robot using the heading function 
included in the robot library.
Each function align the robot to a specific angle obteined by
the heading function (0, 90, -90, and 180).
Thanks this function the robot can go around the bend deciding 
whether turn right o left seeing if there are a wall in front it or on 
its right (or left)

"""
def alignment_0() :
    print_1 = 0
    while not(-4 <= angle() <= 4) :
        if right_dist_g() > left_dist_g() :
            if print_1 == 0 :
                print_1 = 1
                print("****************************************")
                print("I turn on the right to avoid the walls")
                print("****************************************")
            turn(12,0.1)
        else :
            if print_1 == 0 :
                print_1 = 1
                print("***************************************")
                print("I turn on the left to avoid the walls.")
                print("***************************************")  
            turn(-12,0.1)
            
def alignment_90() :
    print_1 = 0
    while not(86 <= angle() <= 94) :
        if right_dist_g() > left_dist_g() :
            if print_1 == 0 :
                print_1 = 1
                print("****************************************")
                print("I turn on the right to avoid the walls")
                print("****************************************")
            turn(12,0.1)
        else :
            if print_1 == 0 :
                print_1 = 1
                print("***************************************")
                print("I turn on the left to avoid the walls.")
                print("***************************************")  
            turn(-12,0.1)
            
def alignment_minus_90() :
    print_1 = 0
    while not(-94 <= angle() <= -86) : 
        if right_dist_g() > left_dist_g() :
            if print_1 == 0 :
                print_1 = 1
                print("****************************************")
                print("I turn on the right to avoid the walls")
                print("****************************************")
            turn(12,0.1)
        else :
            if print_1 == 0 :
                print_1 = 1
                print("***************************************")
                print("I turn on the left to avoid the walls.")
                print("***************************************")  
            turn(-12,0.1)
            
def alignment_180() :
    print_1 = 0
    while (-176 <= angle() <= 176) :
        if right_dist_g() > left_dist_g() :
            if print_1 == 0 :
                print_1 = 1
                print("****************************************")
                print("I turn on the right to avoid the walls")
                print("****************************************")
            turn(12,0.1)
        else :
            if print_1 == 0 :
                print_1 = 1
                print("***************************************")
                print("I turn on the left to avoid the walls.")
                print("***************************************")  
            turn(-12,0.1)
            
"""
rotate_0, rotate_90, rotate_180, rotate_minus_90 are similar to 
the alignment functions but these functions are used to turn the
robot 180 degrees.
they compose the function semicircle that is a function used to 
rotate the robot 180 degrees after grabbing the silver token and 
rotate again 180 degrees after releasing the silver token behind

"""
def rotate_0() :
    while not(-4 <= angle() <= 4) :
        turn(12,0.1)

def rotate_90() :
    while not(86 <= angle() <= 94) :
        turn(12,0.1)

def rotate_minus_90() :
    while not(-94 <= angle() <= -86) :
        turn(12,0.1)

def rotate_180() :
    while (-176 <= angle() <= 176) :
        turn(12,0.1)

def semicircle() :
    if -50 <= angle() <= 50 :
        rotate_180()
    elif -140 <= angle() <= -50 :
        rotate_90()
    elif not(-120 <= angle() <= 120) :
        rotate_0()
    elif 50 <= angle() <= 140 :
        rotate_minus_90()

"""-----------------Token Management Functions-------------------"""

"""
find_silver_token is a function used to find the 
closest silver token
Returns : dist (float) is the distance of the closest 
          silver token (-1 if no silver token is detected ) 
          rot_y (float) is the angle between the robot 
          and the silver token (-1 if no silver token 
          is detected ) 
"""
def find_silver_token() :
    dist = 100
    for token in R.see() :
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_SILVER :
            dist = token.dist
            rot_y = token.rot_y
    if dist == 100 : 
        return -1, -1
    else :
        return dist, rot_y
"""
find_golden_token is a function used to find the 
closest golden token
Returns : dist (float) is the distance of the closest 
          golden token (-1 if no golden token is detected ) 
          rot_y (float) is the angle between the robot 
          and the golden token (-1 if no golden token 
          is detected ) 
"""
def find_golden_token() :
    dist = 100
    for  token in R.see() :
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD :
            dist = token.dist
            rot_y = token.rot_y
    if dist == 100 :
        return -1, -1
    else :
        return dist, rot_y

"""
take_silver_token is function used to find ad reach a 
silver token
Once the robot finds a silver token it first grabs the
silver token,second the robot rotates 180 degrees 
(using the semicircle functions) then it releases the silver
token and finally the robot rotates 180 degrees again.

Arg : d_g (float) is the distance of the closest 
      golden token used to determine if the robot is closer
      to a silver token than to a golden token 
      rot_y (float) is the angle between the robot 
      and the silver token 
"""
def take_silver_token(d_g,rot) :
    if front_dist_s() < d_th and -a_th <= rot <= a_th :
        stop()
        if R.grab() :
            print("-----------------------------------")
            print("I have grabbed the silver token.")
            print("-----------------------------------")
            time.sleep(1)
            semicircle()
            R.release()
            reverse(25,1)
            semicircle()
            drive(60)
    if front_dist_s() < d_g and abs(rot) <= 90 :   
        if abs(rot) <= a_th :
            print("----------------------------------------------")
            print("I am near to a silver token, so I go ahead")
            print("----------------------------------------------")
            drive(60)
        else :    
            if rot < 0 : # if the robot is not well aligned with the token, 
                         #we move it on the left or on the right
                print("-------------------------------------------")
                print("I have detected a silver token on my left")
                print("I turn on left a bit...")
                print("-------------------------------------------")
                turn(-4,0.5)
            elif rot > 0 : 
                print("-------------------------------------------")
                print("I have detected a silver token on my right")
                print("I turn on right a bit..")
                print("-------------------------------------------")
                turn(4,0.5)

"""
avoid_golden_token is a function used to avoid the golden token.
This function allows the robot to avoid and go arround the bend 
in the same time thanks to the alignment functions.
So it check if there is a wall in front it and on its left or right
and then thanks to the alignment functions it turn in the correct direction
and go on.
Instead the second IF statement, allows the robot to avoid the golden token 
even when the robot isn't in a bend, using the function 
token_nearness_detection_g() to detect if the robot is closed to the goldens
token in a specific angular range.
"""
def avoid_golden_token(dist,rot) :
    if front_dist_g() < 1.15 : #the robot has a golden token wall in front it,
                               #so now it checks if it has to turn left or right
        if right_dist_g() > left_dist_g() : #turn right
            print("****************************************************")
            print("I have found a wall in front to me and on my left")
            print("****************************************************")
            if -100 <= angle() <= -80 :
                alignment_0()
            elif -10 <= angle() <= 10 :
                alignment_90()
            elif 80 <= angle() <= 100 :
                alignment_0()
            drive(60)
        elif right_dist_g() < left_dist_g(): #turn left 
            print("*****************************************************")
            print("I have found a wall in front to me and on my right")
            print("*****************************************************")
            if 80 <= angle() <= 100 :
                alignment_0()
            elif -10 <= angle() <= 10:
                alignment_minus_90()
            elif -100 <= angle() <= -80 :
                alignment_180()
            else :
                alignment_90()
            drive(60) 
    if token_nearness_detection_g() < 0.7 :
        if  right_dist_g() > left_dist_g(): # if the robot is not well aligned with the token, 
                                            #we move it on the left or on the right
            print("++++++++++++++++++++++++++++++++++++++++++++++")
            print("There are golden tokens on my left")
            print("I have to turn right a bit to avoid them")
            print("++++++++++++++++++++++++++++++++++++++++++++++")
            turn(4, 0.5)
        else :
            print("++++++++++++++++++++++++++++++++++++++++++++++")
            print("There are golden tokens on my right")
            print("I have to turn left a bit to avoid them")
            print("++++++++++++++++++++++++++++++++++++++++++++++")
            turn(-4, 0.5)
        drive(60)

"""----------------------Distance Functions------------------------"""
"""
front_dist_s returns the frontal distance from a silver token

"""           
def front_dist_s():
    dist = 100
    for token in R.see() :
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_SILVER and -40 < token.rot_y < 40 :
            dist = token.dist
    return dist
"""
token_nearness_detection_g is really similar to the front_dist_g 
function but with a bigger angular range, in ordder to detect better 
the golden tokens to avoid
"""
def token_nearness_detection_g() :
    dist = 100
    for token in R.see() :
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD and -70 < token.rot_y < 70 :
            dist = token.dist
    return dist
"""
front_dist_g returns the frontal distance from a golden token
in order to detect if there is a wall in front the robot

"""      
def front_dist_g():
    dist = 100
    for token in R.see() :
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD and -20 < token.rot_y < 20 :
            dist = token.dist
    return dist
"""
right_dist_g and left_dist_g returns the lateral distance from a golden token
in order to detect if there are walls on the robot right side or on the left side

"""      
def right_dist_g() :
    dist = 100
    for token in R.see() :
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD and 70 < token.rot_y < 110 :
            dist = token.dist
    return dist
    
def left_dist_g() :
    dist = 100
    for token in R.see() :
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD and -110 < token.rot_y < -70 :
            dist = token.dist
    return dist

def main() :

    time.sleep(3)
    drive(60)

    while(1) :
        dist_s, rot_s = find_silver_token()
        dist_g, rot_g = find_golden_token()
        
        take_silver_token(dist_g,rot_s)
        avoid_golden_token(dist_g,rot_g)
        time.sleep(0.2)
        
main()
    