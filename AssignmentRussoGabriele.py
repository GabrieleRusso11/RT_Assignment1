from __future__ import print_function
import time
import math
from sr.robot import *

"""_____________Variables_____________"""

""" Threshold for the control of the orientation """
a_th = 4.0 
""" Threshold for the control of the linear distance """
d_th = 0.4
""" Instance of the class Robot """
R = Robot()

"""______________Robot Moving Functions_______________"""

"""
drive is a function for setting a linear velocity
Arg : speed (init) is the speed of the wheels

""" 
def drive(speed):
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed

"""
stop is a function for stopping the robot's motors 
setting their velocity to zero
Arg : no arguments

"""
def stop() : 
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

"""
reverse is a function for reversing the direction 
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
turn is a function for setting the robot angular 
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

"""______________Orientation Functions_______________"""

"""
Angle is a function which returns the robot angular position 
through the robot library function heading  

"""

def angle() :
    return (R.heading*(180/math.pi)) #heading gives the angle in radiants
    #so I convert it in degrees

def alignment_0() :
    print_1 = 0
    while not(-4 <= angle() <= 4) :
        if right_dist_g() > left_dist_g() :
            if print_1 == 0 :
                print_1 = 1
                print("****************************************")
                print("I turn on the right to avoid the walls")
                print("****************************************")
            turn(15,0.1)
        else :
            if print_1 == 0 :
                print_1 = 1
                print("***************************************")
                print("I turn on the left to avoid the walls.")
                print("***************************************")  
            turn(-15,0.1)
            
def alignment_90() :
    print_1 = 0
    while not(86 <= angle() <= 94) :
        if right_dist_g() > left_dist_g() :
            if print_1 == 0 :
                print_1 = 1
                print("****************************************")
                print("I turn on the right to avoid the walls")
                print("****************************************")
            turn(15,0.1)
        else :
            if print_1 == 0 :
                print_1 = 1
                print("***************************************")
                print("I turn on the left to avoid the walls.")
                print("***************************************")  
            turn(-15,0.1)
            
def alignment_minus_90() :
    print_1 = 0
    while not(-94 <= angle() <= -86) : 
        if right_dist_g() > left_dist_g() :
            if print_1 == 0 :
                print_1 = 1
                print("****************************************")
                print("I turn on the right to avoid the walls")
                print("****************************************")
            turn(15,0.1)
        else :
            if print_1 == 0 :
                print_1 = 1
                print("***************************************")
                print("I turn on the left to avoid the walls.")
                print("***************************************")  
            turn(-15,0.1)
            
def alignment_180() :
    print_1 = 0
    while (-176 <= angle() <= 176) :
        if right_dist_g() > left_dist_g() :
            if print_1 == 0 :
                print_1 = 1
                print("****************************************")
                print("I turn on the right to avoid the walls")
                print("****************************************")
            turn(15,0.1)
        else :
            if print_1 == 0 :
                print_1 = 1
                print("***************************************")
                print("I turn on the left to avoid the walls.")
                print("***************************************")  
            turn(-15,0.1)
            

def rotate_0() :
    while not(-4 <= angle() <= 4) :
        turn(15,0.1)

def rotate_90() :
    while not(86 <= angle() <= 94) :
        turn(15,0.1)

def rotate_minus_90() :
    while not(-94 <= angle() <= -86) :
        turn(15,0.1)

def rotate_180() :
    while (-176 <= angle() <= 176) :
        turn(15,0.1)

def semicircle() :
    if -40 <= angle() <= 40 :
        rotate_180()
    elif -130 <= angle() <= -50 :
        rotate_90()
    elif not(-140 <= angle() <= 140) :
        rotate_0()
    elif 50 <= angle() <= 130 :
        rotate_minus_90()

"""_____________Token Management Functions______________"""

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
   # rot_y = 360
    for token in R.see() :
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_SILVER :
            dist = token.dist
            #if abs(token.rot_y) < abs(rot_y) :
            rot_y = token.rot_y
    if dist == 100 : 
        return -1, -1
    else :
        return dist, rot_y

def find_golden_token() :
    dist = 100
    #rot_y = 360
    for  token in R.see() :
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD :
            dist = token.dist
            #if abs(token.rot_y) < abs(rot_y) :
            rot_y = token.rot_y
    if dist == 100 :
        return -1, -1
    else :
        return dist, rot_y

"""
take_silver_token is function used to first grab a 
silver token,second rotate the robot 180 degrees
then release the silver token and finally rotate the 
robot 180 degrees again.
Arg : dist (float) is the distance of the closest 
      silver token 
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
            if rot < 0 : # if the robot is not well aligned with the token, we move it on the left or on the right
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

def avoid_golden_token(dist,rot) :
    if front_dist_g() < 1 : #the robot has a golden token wall in front it,
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
            drive(80)
        elif right_dist_g() < left_dist_g():
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
            drive(80) 
    if token_nearness_detection_g() < 0.7 :
        if  right_dist_g() > left_dist_g(): # if the robot is not well aligned with the token, we move it on the left or on the right
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
             
def front_dist_s():
    dist = 100
    for token in R.see() :
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_SILVER and -40 < token.rot_y < 40 :
            dist = token.dist
    return dist

def token_nearness_detection_g() :
    dist = 100
    for token in R.see() :
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD and -70 < token.rot_y < 70 :
            dist = token.dist
    return dist

def front_dist_g():
    dist = 100
    for token in R.see() :
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD and -20 < token.rot_y < 20 :
            dist = token.dist
    return dist

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
    while(1) :
        dist_s, rot_s = find_silver_token()
        dist_g, rot_g = find_golden_token()
        drive(60)
        
        take_silver_token(dist_g,rot_s)
        avoid_golden_token(dist_g,rot_g)
        
main()
    