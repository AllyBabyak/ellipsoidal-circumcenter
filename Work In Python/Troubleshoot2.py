# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 15:36:42 2023

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
import math

MajorAxis = 6378137.0 
MinorAxis = 6356752.314245
e2 = (MajorAxis**2 - MinorAxis**2)/(MajorAxis**2)



P1 = ((-331.86, 333.86, 310.02))
P2 = ((-134.14, 136.14, 473.95))
P3 = ((-421.05, 423.05, -50.95))


PNormal = ThreePointPlaneNormal(P1, P2, P3)
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