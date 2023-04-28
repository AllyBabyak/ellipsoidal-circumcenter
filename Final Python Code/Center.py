# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 15:01:33 2023

@author: a.babyak
"""

from VectorCalculations import XYZArcCenter
from CoordinateConversions import CoordTypeToXYZ, XYZToCoordType
from Center2D import SameLongCenter

MajorAxis = 6378137.0 
MinorAxis = 6356752.314245
e2 = (MajorAxis**2 - MinorAxis**2)/(MajorAxis**2)

def ArcCenter(Coord1,Coord2,Coord3,CoordType):
    if (len(Coord1) == 2) and (Coord1[1] == Coord2[1] == Coord2[1]):
        return SameLongCenter (Coord1,Coord2,Coord3,CoordType)
    
    P1 = CoordTypeToXYZ(Coord1, CoordType)
    P2 = CoordTypeToXYZ(Coord2, CoordType)
    P3 = CoordTypeToXYZ(Coord3, CoordType)
        
    XYZCenter = XYZArcCenter(P1, P2, P3)
    
    Center = XYZToCoordType(XYZCenter, CoordType)
        
    return Center
    