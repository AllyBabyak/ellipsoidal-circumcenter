# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 11:48:22 2023

@author: a.babyak
"""

import math
from math import radians

a = 6378137.0
e2 = 0.00676866
f = 1 - math.sqrt(1 - e2)
b = a*(1 - f)

def DegreesToRadians(angle):
    return angle * (math.pi / 180)

def CartesianToGeodetic(x,y,z):
    fx = (2*x)/(a**2)
    fy = (2*y)/(a**2)
    fz = (2*z)/(b**2)
    bottom = math.sqrt(fx**2 + fy**2 + fz**2)
    Latitude = math.asin(abs(fz)/bottom)
    Longitude = math.atan2(y,x)
    return Latitude, Longitude

def ReducedLatitude(angle):
    return math.atan((1-f)*math.tan(angle))

def EllipsoidalDistance(Coord1, Coord2):
    Lat1, Long1 = Coord1
    Lat2, Long2 = Coord2
    U1 = ReducedLatitude(Lat1)
    U2 = ReducedLatitude(Lat2)
    L = Long2 - Long1
    lam = L
    mal = 1000000
    o = 1000000
    cos2a = 1000000
    sino = 1000000
    cos2om = 1000000
    coso = 1000000
    while abs(lam - mal) > 10**(-12):
        sino = math.sqrt((math.cos(U2)*math.sin(lam))**2
                         + (math.cos(U1)*math.sin(U2)
                            + math.sin(U1)*math.cos(U2)*math.cos(lam))**2)
        coso = math.sin(U1)*math.sin(U2) + math.cos(U1)*math.cos(U2)*math.cos(lam)
        o = math.atan2(sino, coso)
        sina = (math.cos(U1)*math.cos(U2)*math.sin(lam))/sino
        cos2a = 1 - sina**2
        cos2om = coso - (2*math.sin(U1)*math.sin(U2))/cos2a
        C = (f/16)*cos2a*(4 + f*(4 - 3*cos2a))
        mal = lam
        lam = L + (1-C)*f*sina*(o + C*sino*(cos2om + C*coso*(-1 + 2*cos2om**2)))
    u2 = cos2a * ((a**2 - b**2)/b**2)
    A = 1 + (u2/16384)*(256 + u2*(-768 + u2*(320 - 175*u2)))
    B = (u2/1024)*(256 + u2*(-128 + u2*(74 - 47*u2)))
    do = B * sino * (cos2om + (1/4)*B*(coso*(-1 + 2*cos2om**2) - (B/6)*cos2om
                                       * (-3 + 4*sino**2)*(-3 + 4*cos2om**2)))
    s = b*A*(o-do)
    return s

NorthPole = [radians(13.472466353),radians(144.748750706)]
Point = [radians(13.339038461),radians(144.635331292)]

distance1 = EllipsoidalDistance(NorthPole, Point)
print(distance1)