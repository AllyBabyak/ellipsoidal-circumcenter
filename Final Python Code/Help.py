# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 09:01:52 2023

@author: a.babyak
"""

from CoordinateConversions import RadiansToXYZ, XYZToRadians
from VectorCalculations import (ThreePointCircumcenter, Distance3D, DotProduct, 
                                ThreePointPlaneNormal, IntersectionWithSpheroid, 
                                VectorThrough, Midpoint, PerpendicularVector,
                                LineIntersect, CenterPick)
from ForTesting import VincentyInverse, ErrorTest
from Center import ArcCenter

Error = 67.03192943708552

P1 = RadiansToXYZ((-7.346357301466442e-07, 4.430217897370805))
P2 = RadiansToXYZ((7.272502034539906e-07, 4.430217918292082))
P3 = RadiansToXYZ((2.8622184163462365e-07, 4.430216938215158))

print("Points \n",P1,"\n",P2,"\n",P3,"\n")

PN = ThreePointPlaneNormal(P1, P2, P3)
PN0 = PN[0],PN[1],0

print("Plane Normal \n",PN,"\n",PN0,"\n")

M12 = Midpoint(P1, P2)
M13 = Midpoint(P1, P3)
M23 = Midpoint(P2, P3)

print("Midpoints\n",M12,"\n",M13,"\n",M23,"\n")

V12 = VectorThrough(P1, P2)
V13 = VectorThrough(P1, P3)
V23 = VectorThrough(P2, P3)

print("Vectors Through Points\n",V12,"\n",V13,"\n",V23,"\n")

P12 = PerpendicularVector(V12, PN)
P13 = PerpendicularVector(V13, PN)
P23 = PerpendicularVector(V23, PN)

print("Perpendicular Bisectors\n",P12,"\n",P13,"\n",P23)

P120 = PerpendicularVector(V12, PN0)
P130 = PerpendicularVector(V13, PN0)
P230 = PerpendicularVector(V23, PN0)

print("\n",P120,"\n",P130,"\n",P230,"\n")

Potential1 = LineIntersect(M12, P12, M13, P13)
Potential2 = LineIntersect(M12, P12, M23, P23)
Potential3 = LineIntersect(M13, P13, M23, P23)

print("Potential Circumcenters\n",Potential1,"\n",Potential2,"\n",Potential3,"\n")

print("Calculated Circumcenter\n",ThreePointCircumcenter(P1, P2, P3),"\n")

IS = IntersectionWithSpheroid(Potential2, PN)
C = CenterPick(P1, P2, P3, IS)
C0 = (-1775939.7,-6125901.55,0)

print("Center\n",C,"\n",C0)

AC = ArcCenter(P1, P2, P3, "XYZ")
print("\n",AC,"\n")

D1 = VincentyInverse(XYZToRadians(P1), XYZToRadians(C))
D2 = VincentyInverse(XYZToRadians(P2), XYZToRadians(C))
D3 = VincentyInverse(XYZToRadians(P3), XYZToRadians(C))
print("Distances\n",D1,D2,D3)

E = ErrorTest(P1, P2, P3, AC, "XYZ")
print(E)

CSharpCenter = (-1775937.741343743,-6125902.404211298,-0.017845721448131985)
CSInt = IntersectionWithSpheroid(CSharpCenter, PN)
