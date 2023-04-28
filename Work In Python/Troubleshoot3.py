# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 10:09:58 2023

@author: a.babyak
"""

from BasicallyTheFinalForm import (DegreesToXYZ, Center, XYZToGeodetic,
                                   ThreePointPlaneNormal, ThreePointCircumcenter,
                                   IntersectionWithSpheroid, Midpoint,
                                   PerpendicularVector,LineIntersect)
from FinalForm import CenterPick
from EllipseCircumcenter import VectorLength, VectorThrough

P1 = (15, 15)
P2 = (85, 15)
P3 = (-10, 15.00001)

Coord1 = DegreesToXYZ(P1)
Coord2 = DegreesToXYZ(P2)
Coord3 = DegreesToXYZ(P3)

## Centers = Center(Coord1, Coord2, Coord3)

PlaneNormal = ThreePointPlaneNormal(Coord1, Coord2, Coord3)
Circumcenter = ThreePointCircumcenter(Coord1, Coord2, Coord3)

PNormal = ThreePointPlaneNormal(Coord1, Coord2, Coord3)
M12 = Midpoint(Coord1, Coord2)
M13 = Midpoint(Coord1, Coord3)
M23 = Midpoint(Coord2, Coord3)
V12 = VectorThrough(Coord1, Coord2)
V13 = VectorThrough(Coord1, Coord3)
V23 = VectorThrough(Coord2, Coord3)
Perp12 = PerpendicularVector(V12, PNormal) ##Through M12
Perp13 = PerpendicularVector(V13, PNormal) ##Through M13
Perp23 = PerpendicularVector(V23, PNormal)

CNo12 = LineIntersect(M23, Perp23, M13, Perp13)
CNo13 = LineIntersect(M23, Perp23, M12, Perp12)
CNo23 = LineIntersect(M12, Perp12, M13, Perp13)

L112 = VectorLength(VectorThrough(Coord1, CNo12))
L212 = VectorLength(VectorThrough(Coord2, CNo12))
L312 = VectorLength(VectorThrough(Coord3, CNo12))

print(L112,L212,L312)

L113 = VectorLength(VectorThrough(Coord1, CNo13))
L213 = VectorLength(VectorThrough(Coord2, CNo13))
L313 = VectorLength(VectorThrough(Coord3, CNo13))

print(L113,L213,L313)

L123 = VectorLength(VectorThrough(Coord1, CNo23))
L223 = VectorLength(VectorThrough(Coord2, CNo23))
L323 = VectorLength(VectorThrough(Coord3, CNo23))

print(L123,L223,L323)

## CircumPlane = IntersectionWithSpheroid(Circumcenter, PlaneNormal)


## C = CenterPick(Coord1, Coord2, Coord3, Centers)
## C = XYZToGeodetic(C)