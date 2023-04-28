# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 15:03:38 2023

@author: a.babyak
"""

from math import cos,sqrt,sin,asin,atan2,atan,radians,degrees,acos,pi

MajorAxis = 6378137.0 
MinorAxis = 6356752.314245
e2 = (MajorAxis**2 - MinorAxis**2)/(MajorAxis**2)

def sign(number):
    if number >= 0:
        return 1
    else:
        return -1

def RadiansToXYZ(Coord):
    lat,long = Coord
    N = MajorAxis/(sqrt(1 - e2 * sin(lat)**2))
    x = N * cos(lat) * cos(long)
    y = N * cos(lat) * sin(long)
    z = (1 - e2) * N * sin(lat)
    return x,y,z

def XYZToRadians(Coord):
    x,y,z = Coord
    a2 = MinorAxis
    a = MajorAxis
    fx = (2*x)/(a**2)
    fy = (2*y)/(a**2)
    fz = (2*z)/(a2**2)
    bottom = sqrt(fx**2 + fy**2 + fz**2)
    Latitude = asin(abs(fz)/bottom)
    Longitude = atan2(y,x)
    if z < 0:
        Latitude = (-1)*Latitude
    return Latitude, Longitude

def DegreesToRadians(Coord):
    C1,C2 = Coord
    C1 = radians(C1)
    C2 = radians(C2)
    return C1,C2

def RadiansToDegrees(Coord):
    C1,C2 = Coord
    C1 = degrees(C1)
    C2 = degrees(C2)
    return C1,C2

def DegreesToXYZ(Coord):
    if Coord[0] == 90:
        x = 0
        y = 0
        z = MinorAxis
    elif Coord[0] == -90:
        x = 0
        y = 0
        z = -MinorAxis
    else:
        Radians = DegreesToRadians(Coord)
        x,y,z = RadiansToXYZ(Radians)
    return x,y,z

def XYZToDegrees(Coord):
    Radians = XYZToRadians(Coord)
    Degrees = RadiansToDegrees(Radians)
    return Degrees

def DMSToDegrees(Coord):
    DegreePosition = Coord.index(' ')
    MinutePosition = Coord.index("'")
    SecondPosition = Coord.index('"')
    Degrees = float(Coord[0,DegreePosition])
    Minutes = float(Coord[DegreePosition + 1, MinutePosition])
    Seconds = float(Coord[MinutePosition + 1, SecondPosition])
    return Degrees + (Minutes/60) + (Seconds/3600)

def DMSToXYZ(Coord):
    Degrees = DMSToDegrees(Coord)
    XYZ = DegreesToXYZ(Degrees)
    return XYZ

def DegreesToDMS(Coord):
    Degrees = Coord // 1
    Remains = (Coord - Degrees)*60
    Minutes = Remains // 1
    Seconds = (Remains - Minutes)*60
    return str(Degrees) + " " + str(Minutes) + "'" + str(Seconds) + '"'

def XYZToDMS(Coord):
    Degrees = XYZToDegrees(Coord)
    DMS = DegreesToDMS(Degrees)
    return DMS
    

def CoordTypeToXYZ(Coord,CoordType):
    if CoordType == "Degrees":
        XYZCoord = DegreesToXYZ(Coord)
    elif CoordType == "Radians":
        XYZCoord = RadiansToXYZ(Coord)
    elif CoordType == "DMS":
        XYZCoord = DMSToXYZ(Coord)
    elif CoordType == "XYZ":
        XYZCoord = Coord
    return XYZCoord

def XYZToCoordType(Coord,CoordType):
    if CoordType == "Degrees":
        TypeCoord = XYZToDegrees(Coord)
    elif CoordType == "Radians":
        TypeCoord = XYZToRadians(Coord)
    elif CoordType == "DMS":
        TypeCoord = XYZToDMS(Coord)
    elif CoordType == "XYZ":
        TypeCoord = Coord
    return TypeCoord

def SphereRadiansToXYZ(Coord,Radius):
    lat, long = Coord
    nlat = pi/2 - lat
    x = Radius * sin(nlat) * cos(long)
    y = Radius * sin(nlat) * sin(long)
    z = Radius * cos(nlat)
    return x,y,z

def SphereDegreesToXYZ(Coord,Radius):
    Radians = DegreesToRadians(Coord)
    XYZ = SphereRadiansToXYZ(Radians, Radius)
    return XYZ

def SphereXYZToRadians(Coord,Radius):
    x,y,z = Coord
    long = atan(y/x)
    nlat = atan(sqrt(x**2 + y**2)/z)
    lat = pi/2 - nlat
    return lat,long

def SphereXYZToDegrees(Coord,Radius):
    Radians = SphereXYZToRadians(Coord, Radius)
    Degrees = RadiansToDegrees(Radians)
    return Degrees

def SphereXYZToCoordType(Coord,Radius,CoordType):
    if CoordType == "Degrees":
        TypeCoord = SphereXYZToDegrees(Coord, Radius)
    elif CoordType == "Radians":
        TypeCoord = SphereXYZToRadians(Coord, Radius)
    elif CoordType == "XYZ":
        TypeCoord = Coord
    return TypeCoord

def SphereCoordTypeToXYZ(Coord,Radius,CoordType):
    if CoordType == "Degrees":
        TypeCoord = SphereDegreesToXYZ(Coord, Radius)
    elif CoordType == "Radians":
        TypeCoord = SphereRadiansToXYZ(Coord, Radius)
    elif CoordType == "XYZ":
        TypeCoord = Coord
    return TypeCoord