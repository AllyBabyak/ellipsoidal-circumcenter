# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 14:14:10 2023

@author: a.babyak
"""

from math import sqrt, asin, atan2,sin,cos

MajorAxis = 6378137.0 
MinorAxis = 6356752.314245
e2 = (MajorAxis**2 - MinorAxis**2)/(MajorAxis**2)

def CartesianToGeodetic(x,y,z):
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

def AngleToVector(Angle):
    z = sin(Angle)
    r = cos(Angle)
    return r,z

def ParallelNormal(Vector):
    ## tz = 2z0/b^2
    ## tr = 2r0/a^2
    ## r0^2/a^2 + z0^2/b^2 = 1
    r,z = Vector
    t = sqrt(4/(MajorAxis**2 * r**2 + MinorAxis**2 * z**2))
    z0 = (MinorAxis**2 * t * z)/2
    r0 = (MajorAxis**2 * t * r)/2
    return r0,z0
    

def QuadraticFormula(A,B,C):
    x1 = (-B + sqrt(B**2 - 4*A*C))/(2*A)
    x2 = (-B - sqrt(B**2 - 4*A*C))/(2*A)
    return x1,x2

def IntersectionWithSpheroid(Point,Vector):
    x0,y0,z0 = Point
    a,b,c = Vector
    A = (a**2 + b**2)/(MajorAxis**2) + (c**2)/(MinorAxis**2)
    B = 2 * ((a*x0 + b*y0)/(MajorAxis**2) + (c*z0)/(MinorAxis**2))
    C = (x0**2 + y0**2)/(MajorAxis**2) + (z0**2)/(MinorAxis**2) - 1
    Solutions = QuadraticFormula(A, B, C)
    x1 = x0 + Solutions[0]*a
    x2 = x0 + Solutions[1]*a
    y1 = y0 + Solutions[0]*b
    y2 = y0 + Solutions[1]*b
    z1 = z0 + Solutions[0]*c
    z2 = z0 + Solutions[1]*c
    return (x1,y1,z1),(x2,y2,z2)

def GeodeticToCartesian(Latitude,Longitude):
    Lat = AngleToVector(Latitude)
    r,vz = ParallelNormal(Lat)
    vx = cos(Longitude)
    vy = sin(Longitude)
    z = IntersectionWithSpheroid((vx,vy,0), (0,0,vz))
    x = IntersectionWithSpheroid((0,vy,vz), (vx,0,0))
    y = IntersectionWithSpheroid((vx,0,vz), (0,vy,0))
    return x,y,z

Test = CartesianToGeodetic(4593077.161782029, 3854049.3295016633, 2167696.76357438)
print(Test)