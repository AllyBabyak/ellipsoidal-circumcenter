# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 13:29:00 2023

@author: a.babyak
"""

from EllipseCircumcenter import (Center, XYPlaneCircumcenter, TangentPlaneNormal,
                                 IntersectWithXYPlane, ThreePointCircumcenter,
                                 ThreePointPlaneNormal, Midpoint, VectorThrough,
                                 IntersectionWithSpheroid, QuadraticFormula,
                                 PerpendicularVector, LineIntersect, Circumcenter2,
                                 VectorLength)
from FinalForm import CenterPick, ErrorTestGiven
from BasicallyTheFinalForm import DegreesToXYZ, GeodeticToXYZ, XYZToGeodetic, CoordToDegrees

MajorAxis = 6378137.0 
MinorAxis = 6356752.314245
e2 = (MajorAxis**2 - MinorAxis**2)/(MajorAxis**2)



P1 = DegreesToXYZ((-10, 20))
P2 = DegreesToXYZ((85, 20))
P3 = DegreesToXYZ((50, 20))


x1,y1,z1 = P1
x2,y2,z2 = P2
x3,y3,z3 = P3
V12x, V12y, V12z = VectorThrough(P1, P2)
V13x, V13y, V13z = VectorThrough(P1, P3)
V23x, V23y, V23z = VectorThrough(P2, P3)

xNo23 = V12y * V13z - V12z * V13y
yNo23 = V12z * V13x - V12x * V13z
zNo23 = V12x * V13y - V12y * V13x

xNo12 = V23y * V13z - V23z * V13y
yNo12 = V23z * V13x - V23x * V13z
zNo12 = V23x * V13y - V23y * V13x

xNo13 = V23y * V12z - V23z * V12y
yNo13 = V23z * V12x - V23x * V12z
zNo13 = V23x * V12y - V23y * V12x

PNormalNo23 =  xNo23, yNo23, 0
PNormalNo12 =  xNo12, yNo12, 0
PNormalNo13 =  xNo13, yNo13, 0


PNormal = PNormalNo12



M12 = Midpoint(P1, P2)
M13 = Midpoint(P1, P3)
M23 = Midpoint(P2, P3)
V12 = VectorThrough(P1, P2)
V13 = VectorThrough(P1, P3)
V23 = VectorThrough(P2, P3)
Perp12 = PerpendicularVector(V12, PNormal) ##Through M12
Perp13 = PerpendicularVector(V13, PNormal) ##Through M13
Perp23 = PerpendicularVector(V23, PNormal)

C1 = LineIntersect(M13, Perp13, M23, Perp23)
C2 = LineIntersect(M12, Perp12, M23, Perp23)
C3 = LineIntersect(M12, Perp12, M13, Perp13)

print(C1,C2,C3)

VL11 = VectorLength(VectorThrough(P1, C1))
VL21 = VectorLength(VectorThrough(P2, C1))
VL31 = VectorLength(VectorThrough(P3, C1))

print(VL11,VL21,VL31)

VL12 = VectorLength(VectorThrough(P1, C2))
VL22 = VectorLength(VectorThrough(P2, C2))
VL32 = VectorLength(VectorThrough(P3, C2))

print(VL12,VL22,VL32)

VL13 = VectorLength(VectorThrough(P1, C3))
VL23 = VectorLength(VectorThrough(P2, C3))
VL33 = VectorLength(VectorThrough(P3, C3))

print(VL13,VL23,VL33)


'''
Perp12 = PerpendicularVector(V12, PNormal) ##Through M12
Perp13 = PerpendicularVector(V13, PNormal) ##Through M13
Perp23 = PerpendicularVector(V23, PNormal)




C = ThreePointCircumcenter(I1, I2, I3)

XYPC = XYPlaneCircumcenter(P1, P2, P3)
'''

