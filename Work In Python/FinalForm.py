# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 08:05:36 2023

@author: a.babyak
"""

from BasicallyTheFinalForm import (Center, CoordToRadians, XYZToGeodetic, 
                                   Distance3D, CoordToDegrees, GeodeticToXYZ,
                                   VincentyInverse, DegreesToXYZ)

def CenterPick(Coord1,Coord2,Coord3,Centers):
    Center1,Center2 = Centers
    distance11 = Distance3D(Center1, Coord1)
    distance12 = Distance3D(Center1, Coord2)
    distance13 = Distance3D(Center1, Coord3)
    SumDistance1 = distance11 + distance12 + distance13
    distance21 = Distance3D(Center2, Coord1)
    distance22 = Distance3D(Center2, Coord2)
    distance23 = Distance3D(Center2, Coord3)
    SumDistance2 = distance21 + distance22 + distance23
    
    if SumDistance1 < SumDistance2:
        return Center1
    else:
        return Center2

def ArcCenter(Coord1,Coord2,Coord3,AngleType):
    if AngleType == "Degrees":
        Coord1 = DegreesToXYZ(Coord1)
        Coord2 = DegreesToXYZ(Coord2)
        Coord3 = DegreesToXYZ(Coord3)
    elif AngleType == "Radians":
        Coord1 = GeodeticToXYZ(Coord1)
        Coord2 = GeodeticToXYZ(Coord2)
        Coord3 = GeodeticToXYZ(Coord3)
    
    Centers = Center(Coord1, Coord2, Coord3)
    C = CenterPick(Coord1, Coord2, Coord3, Centers)
    C = XYZToGeodetic(C)
    
    if AngleType == "Degrees":
        C = CoordToDegrees(C)
        
    return C

def ErrorTestGiven(Coord1,Coord2,Coord3,CalcCenter, AngleType):
    if AngleType == "Degrees": 
        Coord1 = CoordToRadians(Coord1)
        Coord2 = CoordToRadians(Coord2)
        Coord3 = CoordToRadians(Coord3)
        CalcCenter = CoordToRadians(CalcCenter)
    D1 = VincentyInverse(Coord1, CalcCenter)
    D2 = VincentyInverse(Coord2, CalcCenter)
    D3 = VincentyInverse(Coord3, CalcCenter)
    Error = max(D1,D2,D3) - min(D1,D2,D3)
    return Error

def ErrorTest(Coord1,Coord2,Coord3,AngleType):
    if AngleType == "Degrees": 
        Coord1 = CoordToRadians(Coord1)
        Coord2 = CoordToRadians(Coord2)
        Coord3 = CoordToRadians(Coord3)
    CalcCenter = ArcCenter(Coord1, Coord2, Coord3, "Degrees")
    CalcCenter = CoordToRadians(CalcCenter)
    D1 = VincentyInverse(Coord1, CalcCenter)
    D2 = VincentyInverse(Coord2, CalcCenter)
    D3 = VincentyInverse(Coord3, CalcCenter)
    Error = max(D1,D2,D3) - min(D1,D2,D3)
    return Error

def StringToCoord(Coord):
    NoBrac = Coord[1:-1]
    List = NoBrac.split(', ')
    lat = float(List[0])
    long = float(List[1])
    return lat,long

'''
P1 = (-4.38353132127002e-05, 46.00001102392895)
P2 = (1.4340552682185362e-05, 45.999957402833815)
P3 = (2.5538818365231167e-05, 45.99996293387819)

Cent = ArcCenter(P1, P2, P3, "Degrees")

Error = ErrorTestGiven(P1, P2, P3, Cent, "Degrees")
print(Cent)
print(Error)
'''