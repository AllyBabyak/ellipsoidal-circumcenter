# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 15:37:28 2023

@author: a.babyak
"""

from math import cos, tan, sin, sqrt, radians, degrees

a = 6378137.0 
b = 6356752.314245
e2 = (a**2 - b**2)/(a**2)

def Latitude(center, xy):
    B0, L0 = center
    x, y = xy
    
    c0 = cos(B0)
    eta2 = (e2/(1-e2))*c0**2
    V2 = 1 + eta2
    t0 = tan(B0)
    s0 = sin(B0)
    N0 = a / (sqrt(1 - e2*s0**2))
    
    coeff01 = V2/N0
    coeff20 = - (V2*t0)/(2*N0**2)
    coeff02 = - (3*V2*eta2*t0)/(2*N0**2)
    coeff21 = - (V2*(1 + 3*t0 + eta2 - 9*eta2*t0**2))/(6*N0**3)
    coeff03 = - (V2*eta2*(1 - t0**2 + eta2 - 5*eta2*t0**2))/(2*N0**3)
    coeff40 = (V2*t0*(1 + 3*t0**2 + eta2 - 9*eta2*t0**2))/(24*N0**4)
    coeff22 = - (V2*t0*(4 + 6*t0**2 - 13*eta2 - 9*eta2*t0**2 - 17*eta2**2
                        + 45*eta2**2*t0**2))/(12*N0**4)
    coeff04 = (V2*eta2**2*t0*(12 + 69*eta2 - 45*eta2*t0**2 + 57*eta2**2
                              - 105*eta2**2*t0**2))/(24 * N0**4)
    coeff41 = (V2*(1 + 30*t0**2 + 45*t0**4 + eta2*(2 - 72*t0**2 - 90*t0**4)
                   + eta2**2*(1 - 102*t0**2 + 225*t0**4)))/(120*N0**5)
    coeff23 = (V2*(-4 - 30*t0**2*(1 + t0**2) + 9*eta2*(1 + 2*t0**2 + 5*t0**4)
                   + 2*eta2**2*(15 - 177*t0**2) 
                   + eta2**3*(17 - 420*t0**3 + 525*t0**4)))/(60*N0**5)
    coeff05 = (V2*eta2*(4 - 4*t0**2 + eta2*(27 - 142*t0**2 + 15*t0**4)
                        + 2*eta2**2*(21 - 226*t0**2 + 155*t0**4)
                        + eta2**3*(19 - 314*t0**2 + 315*t0**4)))/(40*N0**5)
    
    B = (B0 + coeff01*y + coeff20*x**2 + coeff02*y**2 + coeff21*x**2*y
         + coeff03*y**3 + coeff40*x**4 + coeff22*x**2*y**2 + coeff04*y**4
         + coeff41*x**4*y + coeff23*x**2*y**3 + coeff05*y**5)
    
    return B

def Longitude(center, xy):
    B0, L0 = center
    x, y = xy
    
    c0 = cos(B0)
    eta2 = (e2/(1-e2))*c0**2
    t0 = tan(B0)
    s0 = sin(B0)
    N0 = a / (sqrt(1 - e2*s0**2))
    
    coeff10 = 1/(N0*c0)
    coeff11 = t0/(N0**2*c0)
    coeff30 = - (t0**2)/(3*N0**3*c0)
    coeff12 = (1 + 3*t0**2 + eta2)/(3*N0**3*c0)
    coeff31 = - (t0*(1 + 3*t0**2) + eta2)/(3*N0**4*c0)
    coeff13 = (t0*(2 + 3*t0**2 + eta2 - eta2**2))/(3*N0**4*c0)
    coeff50 = (t0**2*(1 + 3*t0**2 + eta2))/(15*N0**5*c0)
    coeff32 = (1 + 20*t0**2 + 30*t0**4 + eta2*(2 + 13*t0**2) 
               + eta2**3*(1 - 7*t0**2))/(15*N0**5*c0)
    coeff14 = (2 + 15*t0**2 + 15*t0**4 + 3*eta2*(1 + 2*t0**2) - 3*eta2**2*t0**2
               - eta2**3*(1 - 6*t0**2))/(15*N0**5*c0)
    
    L = (L0 + coeff10*x + coeff11*x*y + coeff30*x**3 + coeff12*x*y**2
         + coeff31*x**3*y + coeff13*x*y**3 + coeff50*x**5 + coeff32*x**3*y**2
         + coeff14*x*y**4)
    
    return L

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

def LongLatFromDistance(CenterCoord, CoordType, Distance, XValue):
    if CoordType == "Degrees":
        CenterCoord = CoordToRadians(CenterCoord)
    YValue = sqrt(Distance**2 - XValue**2)
    XYCoords = XValue,YValue
    Lat = Latitude(CenterCoord, XYCoords)
    Long = Longitude(CenterCoord, XYCoords)
    return Lat,Long


center = (30,40)

Point = LongLatFromDistance(center, "Degrees", 10000000, 4)
print(Point)