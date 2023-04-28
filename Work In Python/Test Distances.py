# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 15:38:16 2023

@author: a.babyak
"""

from vincenty import vincenty_inverse
import math

a = 600
b = 500
f = (a-b)/a

def CartesianToGeodetic(x,y,z):
    fx = (2*x)/(a**2)
    fy = (2*y)/(a**2)
    fz = (2*z)/(b**2)
    bottom = math.sqrt(fx**2 + fy**2 + fz**2)
    Latitude = math.asin(abs(fz)/bottom)
    Longitude = math.atan2(y,x)
    if z < 0:
        Latitude = (-1)*Latitude
    return [math.degrees(Latitude), math.degrees(Longitude)]


CCoord = CartesianToGeodetic(578.0351219868269, -41.28067439090813, 129.55935917430634)

P1Coord = CartesianToGeodetic(291.05, -392.21, 290.42738311170166)
P2Coord = CartesianToGeodetic(247.04, 102.64, 447.55219186642853)
P3Coord = CartesianToGeodetic(409.1, 409.1, 132.48265085579217)

distance1 = vincenty_inverse(CCoord,P1Coord).m
distance2 = vincenty_inverse(CCoord,P2Coord).m
distance3 = vincenty_inverse(CCoord,P3Coord).m

print(distance1)
print(distance2)
print(distance3)