# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 11:42:52 2023

@author: a.babyak
"""

from EllipseCircumcenter import Center, SameLongCenter
from FinalForm import CenterPick, ErrorTestGiven
from BasicallyTheFinalForm import DegreesToXYZ, GeodeticToXYZ, XYZToGeodetic, CoordToDegrees

def ArcCenters(P1,P2,P3,AngleType):
    if AngleType == "Degrees":
        Coord1 = DegreesToXYZ(P1)
        Coord2 = DegreesToXYZ(P2)
        Coord3 = DegreesToXYZ(P3)
        if P1[1] == P2[1] == P3[1]:
            return CenterPick(SameLongCenter(Coord1,Coord2,Coord3))
    elif AngleType == "Radians":
        Coord1 = GeodeticToXYZ(P1)
        Coord2 = GeodeticToXYZ(P3)
        Coord3 = GeodeticToXYZ(P2)
        if P1[1] == P2[1] == P3[1]:
            return CenterPick(SameLongCenter(Coord1,Coord2,Coord3))
    else:
        Coord1,Coord2,Coord3 = P1,P2,P3
    
    Centers = Center(Coord1,Coord2,Coord3)
    CircumPlane = CoordToDegrees(XYZToGeodetic(CenterPick(Coord1,Coord2,Coord3,Centers[0])))
    XYCircumPlane = CoordToDegrees(XYZToGeodetic(CenterPick(Coord1,Coord2,Coord3,Centers[1])))
    XYCC = CoordToDegrees(XYZToGeodetic(CenterPick(Coord1,Coord2,Coord3,Centers[2])))
    
    return CircumPlane,XYCircumPlane,XYCC
  

P1 = DegreesToXYZ((-10, 20))
P2 = DegreesToXYZ((85, 20))
P3 = DegreesToXYZ((50, 20))

Test = ArcCenters(P1, P2, P3, "XYZ")
print(Test)
