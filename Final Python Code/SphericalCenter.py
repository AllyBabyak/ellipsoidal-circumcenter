# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 10:11:48 2023

@author: a.babyak
"""

from math import sqrt, pi
from VectorCalculations import CenterPick, ThreePointPlaneNormal
from CoordinateConversions import SphereCoordTypeToXYZ, SphereXYZToCoordType, sign

RadiusNearEquator = 6335439
RadiusNearPoles = 6399594
AverageRadius = 6371009

def IntersectionWithSphere(Vector,Radius):
    a,b,c = Vector
    bottom = sqrt(a**2 + b**2 + c**2)
    t = Radius/bottom
    x = t*a
    y = t*b
    z = t*c
    return (x,y,z),(-x,-y,-z)

def SphericalCenter(Coord1,Coord2,Coord3,CoordType,Radius):
    if (len(Coord1) == 2) and (Coord1[1] == Coord2[1] == Coord3[1]):
        if CoordType == "Degrees":
            Center = (0,Coord1[1] + 90)
        elif CoordType == "Radians":
            Center = (0,Coord1[1] + pi/2)
            
    elif (len(Coord1) == 2) and (Coord1[0] == Coord2[0] == Coord3[0]):
        if CoordType == "Degrees":
            Center = (sign(Coord1[0])*90,0)
        elif CoordType == "Radians":
            Center = (sign(Coord1[0])*(pi/2),0)
            
    else:
        P1 = SphereCoordTypeToXYZ(Coord1, Radius, CoordType)
        P2 = SphereCoordTypeToXYZ(Coord2, Radius, CoordType)
        P3 = SphereCoordTypeToXYZ(Coord3, Radius, CoordType)
    
        Normal = ThreePointPlaneNormal(P1, P2, P3)
        Centers = IntersectionWithSphere(Normal, Radius)
    
        XYZCenter = CenterPick(P1, P2, P3, Centers)
    
        Center0 = SphereXYZToCoordType(Centers[0], Radius, CoordType)
        Center1 = SphereXYZToCoordType(Centers[1], Radius, CoordType)
        print(Center0)
    return Center1


