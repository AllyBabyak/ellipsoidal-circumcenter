# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 15:13:57 2023

@author: a.babyak
"""

from math import sqrt, radians
from CoordinateConversions import (DegreesToXYZ, RadiansToXYZ, XYZToDegrees, 
                                   XYZToRadians)

MajorAxis = 6378137.0 
MinorAxis = 6356752.314245
e2 = (MajorAxis**2 - MinorAxis**2)/(MajorAxis**2)

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
    Center = x, RootPlus, z
    return Center

def SameLongCenter(Coord1,Coord2,Coord3,CoordType):
    if CoordType == "Degrees":
        XYZ1 = DegreesToXYZ(Coord1)
        XYZ2 = DegreesToXYZ(Coord2)
        XYZ3 = DegreesToXYZ(Coord3)
        Adjustment = Coord1[1]
    elif CoordType == "Radians":
        XYZ1 = RadiansToXYZ(Coord1)
        XYZ2 = RadiansToXYZ(Coord2)
        XYZ3 = RadiansToXYZ(Coord3)
        Adjustment = Coord1[1]
        
    Adjustment = Coord1[1]
        
    Circumcenter = Circumcenter2D(XYZ1, XYZ2, XYZ3)
    ArcCenter0 = HorizontalSpheroidIntersect(Circumcenter)
    
    if CoordType == "Degrees":
        ArcCenter0Deg = XYZToDegrees(ArcCenter0)
        ArcCenter = ArcCenter0Deg[0],(ArcCenter0Deg[1] + Adjustment)
    elif CoordType == "Radians":
        ArcCenter0Rad = XYZToRadians(ArcCenter0)
        ArcCenter = ArcCenter0Rad[0],(ArcCenter0Rad[1] + Adjustment)
        
    return ArcCenter