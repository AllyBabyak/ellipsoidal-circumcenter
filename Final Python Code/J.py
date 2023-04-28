# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 10:45:45 2023

@author: a.babyak
"""

from CoordinateConversions import RadiansToXYZ, XYZToRadians, CoordTypeToXYZ, XYZToCoordType
from VectorCalculations import (ThreePointCircumcenter, Distance3D, Midpoint,
                                ThreePointPlaneNormal, VectorThrough, 
                                PerpendicularVector, LineIntersect,
                                LargestCircumcenterError, CenterPick,
                                IntersectionWithSpheroid)
from Center import ArcCenter
from ForTesting import VincentyInverse

## (-3.9949421366807325e-05, -2.214946219648919) 4.083504125623449

P1 = (-1.422326190560158e-06, 4.068039408405771)
P2 = (-4.267542674038072e-06, 4.068038237282101)
P3 = (1.6452155634560493e-06, 4.068039362714805)

P1C = RadiansToXYZ(P1)
P2C = RadiansToXYZ(P2)
P3C = RadiansToXYZ(P3)

PlaneCircumcenter = ThreePointCircumcenter(P1C, P2C, P3C)

Center = ArcCenter(P1, P2, P3, "Radians")

D1 = VincentyInverse(Center, P1)
D2 = VincentyInverse(Center, P2)
D3 = VincentyInverse(Center, P3)

PD1 = Distance3D(PlaneCircumcenter, P1C)
PD2 = Distance3D(PlaneCircumcenter, P2C)
PD3 = Distance3D(PlaneCircumcenter, P3C)

def ThreePointCircumcenterV2(P1,P2,P3):
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
   
    Potential1 = LineIntersect(M23, Perp23, M13, Perp13)
    Potential2 = LineIntersect(M12, Perp12, M13, Perp13)
    Potential3 = LineIntersect(M12, Perp12, M23, Perp23)
    
    E1 = LargestCircumcenterError(P1, P2, P3, Potential1)
    E2 = LargestCircumcenterError(P1, P2, P3, Potential2)
    E3 = LargestCircumcenterError(P1, P2, P3, Potential3)
    
    if min(E1,E2,E3) == E1:
        return Potential1
    elif min(E1,E2,E3) == E2:
        return Potential2
    else:
        return Potential3

PlaneNormal = ThreePointPlaneNormal(P1C, P2C, P3C)
C = ThreePointCircumcenterV2(P1C, P2C, P3C)
CR = XYZToRadians(C)

def XYZArcCenter(P1,P2,P3):
    PlaneNormal = ThreePointPlaneNormal(P1, P2, P3)
    Circumcenter = ThreePointCircumcenterV2(P1, P2, P3)
    PotentialCenters = IntersectionWithSpheroid(Circumcenter, PlaneNormal)
    
    ArcCenter = CenterPick(P1, P2, P3, PotentialCenters)
    return ArcCenter

CC = XYZArcCenter(P1C, P2C, P3C)
CR = XYZToRadians(CC)
D1 = VincentyInverse(CR, P1)
D2 = VincentyInverse(CR, P2)
D3 = VincentyInverse(CR, P3)
print(D1,D2,D3)
    
        
    