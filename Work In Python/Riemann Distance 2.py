# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 10:13:35 2023

@author: a.babyak
"""

from math import cos,tan,sqrt,sin,asin,atan2, radians,degrees

## a = 6378206.4
## e2 =  0.00676866
a = 6378137.0 
b = 6356752.314245
e2 = (a**2 - b**2)/(a**2)

def xCoord(centre, point):
    B0, L0 = centre
    B, L = point
    c0 = cos(B0)
    eta2 = (e2/(1-e2))*c0**2
    V2 = 1 + eta2
    t0 = tan(B0)
    s0 = sin(B0)
    N0 = a / (sqrt(1 - e2*s0**2))
    
    coeff10 = N0*c0
    coeff11 = - ((N0*c0) / V2) * t0
    coeff30 = - ((N0*c0**3)/6) * t0**2
    coeff12 = - ((N0*c0)/(6*V2**2)) * (2 + 2*eta2 + 9*eta2*t0**2)
    coeff31 = - ((N0*c0**3)/(6*V2)) * t0*(1 - t0**2 + eta2)
    coeff13 = - ((N0*c0)/(6*V2**3)) * eta2*t0*(7 - 3*t0**2 + 7*eta2 
                                               + 12*eta2*t0**2)
    coeff50 = - ((N0*c0**5)/120) * t0**3 * (3 - t0**2 + 3*eta2)
    coeff32 = - ((N0*c0**3)/(180*V2**2)) * (8 - 40*t0**2 
                                            + eta2*(16 - 31*t0**2 - 45*t0**4)
                                            + eta2**2*(8 + 9*t0**2))
    coeff14 = - ((N0*c0)/(360*V2**4)) * (8 + 4*eta2*(28 - 69*t0**2)
                                         + eta2**2 * (200 - 507*t0**2 + 405*t0**4)
                                         + 3*eta2**3 * (32 - 77*t0**2 - 1140*t0**4))
    
    l = L - L0
    b = B - B0
    
    x = (coeff10*l + coeff11*l*b + coeff30*l**3 + coeff12*l*b**2 
         + coeff31*l**3*b + coeff13*l*b**3 + coeff50*l**5 + coeff32*l**3*b**2
         + coeff14*l*b**4)
    
    return x

def yCoord(centre, point):
    B0, L0 = centre
    B, L = point
    c0 = cos(B0)
    eta2 = (e2/(1-e2))*c0**2
    V2 = 1 + eta2
    t0 = tan(B0)
    s0 = sin(B0)
    N0 = a / (sqrt(1 - e2*s0**2))
    
    coeff01 = N0/V2
    coeff20 = ((N0*c0**2)/2) * t0
    coeff02 = (N0/(2*V2**2)) * 3*eta2*t0
    coeff21 = ((N0*c0**2)/(6*V2)) * (1 - 3*t0**2 + eta2)
    coeff03 = (N0/(2*V2**3)) * eta2 * (1 - t0**2 + eta2 + 4*eta2*t0**2)
    coeff40 = ((N0*c0**4)/24) * t0 * (1 - t0**2 + eta2)
    coeff22 = - ((N0*c0**2)/(12*V2**2)) * t0 * (4 + 3*eta2 + 9*eta2*t0**2 - eta2**2)
    coeff04 = - (N0/(8*V2**4)) * eta2*t0*(4 + 17*eta2 - 9*eta2*t0**2 
                                          + 13*eta2**2 + 76*eta2**2*t0**2)
    coeff41 = ((N0*c0**4)/(360*V2)) * (7 - 50*t0**2 + 15*t0**4 
                                       + 2*eta2*(7 - 37*t0**2) 
                                       + eta2**2*(7 - 24*t0**2))
    coeff23 = ((N0*c0**2)/(180*V2**3)) * (-8 - eta2*(7 + 174*t0**2 - 45*t0**4)
                                          + 2*eta2**2*(5 - 83*t0**2 - 90*t0**4)
                                          + 3*eta2**3*(3 + 2*t0**2))
    coeff05 = (N0/(40*V2**5))*eta2 * (-4 + 4*t0**2 + eta2*(3 - 98*t0**2 + 15*t0**4)
                                      + 2*eta2**2*(9 - 179*t0**2 + 90*t0**4)
                                      + eta2**3 * (11 - 256*t0**2 - 1320*t0**4))
    
    l = L - L0
    b = B - B0
    
    y = (coeff01*b + coeff20*l**2 + coeff02*b**2 + coeff21*l**2*b + coeff03*b**3
         + coeff40*l**4 + coeff22*l**2*b**2 + coeff04*b**4 + coeff41*l**4*b
         + coeff23*l**2*b**3 + coeff05*b**5)
    
    return y

def distance(centre, point):
    x = xCoord(centre, point)
    y = yCoord(centre, point)
    return sqrt(x**2 + y**2)

def CartesianToGeodetic(x,y,z):
    a2 = a*sqrt(1-e2)
    fx = (2*x)/(a**2)
    fy = (2*y)/(a**2)
    fz = (2*z)/(a2**2)
    bottom = sqrt(fx**2 + fy**2 + fz**2)
    Latitude = asin(abs(fz)/bottom)
    Longitude = atan2(y,x)
    if z < 0:
        Latitude = (-1)*Latitude
    return [Latitude, Longitude]


def CoordToRadians(Coord):
    C1,C2 = Coord
    C1 = radians(C1)
    C2 = radians(C2)
    return C1,C2

def CoordToDegrees(Coord):
    C1,C2 = Coord
    C1 = degrees(C1)
    C2 = degrees(C2)
    return C1,C2


C = CoordToRadians((-50.0000136620894, -154.9998837075605))
P1 = CoordToRadians((45.62935525337285, 36.69427441440054))
D = distance(C, P1)
print(D)