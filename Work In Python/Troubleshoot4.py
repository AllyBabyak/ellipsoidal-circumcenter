# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 10:35:03 2023

@author: a.babyak
"""

from EllipseCircumcenter import VectorLength, VectorThrough
from BasicallyTheFinalForm import (DegreesToXYZ, XYZToGeodetic, VincentyInverse,
                                   CoordToDegrees)
from math import sqrt
from FinalForm import ErrorTestGiven

MajorAxis = 6378137.0 
MinorAxis = 6356752.314245
e2 = (MajorAxis**2 - MinorAxis**2)/(MajorAxis**2)

P1 = (1, 20)
P2 = (2, 20)
P3 = (3, 20)

P1C = DegreesToXYZ(P1)
P2C = DegreesToXYZ(P2)
P3C = DegreesToXYZ(P3)

Q1 = (1, 0)
Q2 = (2, 0)
Q3 = (3, 0)

Q1C = DegreesToXYZ(Q1)
Q2C = DegreesToXYZ(Q2)
Q3C = DegreesToXYZ(Q3)

LP1 = VectorLength(P1C)
LQ2 = VectorLength(Q1C)

def Circumcenter2D(P1,P2,P3):
    x1,y1,z1 = P1
    x2,y2,z2 = P2
    x3,y3,z3 = P3
    
    t = x1**2 + z1**2 - x2**2 - z2**2
    u = x1**2 + z1**2 - x3**2 - z3**2
    J = (x1 - x2)*(z1 - z3) - (x1 - x3)*(z1 - z2)
    
    x = ((z1 - z3)*t - (z1 - z2)*u)/(2*J)
    z = ((x1 - x2)*u - (x1 - x3)*t)/(2*J)
    
    return x,0,z

def HorizontalSpheroidIntersect(Pointxz):
    x,y,z = Pointxz
    a = MajorAxis
    b = MinorAxis
    InRoot = a**2 * (1 - (z**2)/(b**2)) - x**2
    RootPlus = sqrt(InRoot)
    RootMinus = -RootPlus
    Center1 = x, RootPlus, z
    Center2 = x, RootMinus, z
    return Center1, Center2

C = Circumcenter2D(Q1C, Q2C, Q3C)

I = HorizontalSpheroidIntersect(C)
ID = CoordToDegrees(XYZToGeodetic(I[0]))

Error1 = ErrorTestGiven(Q1, Q2, Q3, ID, "Degrees")
Error2 = ErrorTestGiven(Q1, Q2, Q3, (0,90), "Degrees")

print(Error1, Error2)