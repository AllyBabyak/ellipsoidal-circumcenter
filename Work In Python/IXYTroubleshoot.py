# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 09:24:50 2023

@author: a.babyak
"""

from math import sqrt

MajorAxis = 600
MinorAxis = 500
e2 = (MajorAxis**2 - MinorAxis**2)/(MajorAxis**2)
tol = 0.000001

def VectorThrough(P1,P2):
    '''
    Given two points, determines the direction vector between them.
    '''
    x1,y1,z1 = P1
    x2,y2,z2 = P2
    x = x1 - x2
    y = y1 - y2
    z = z1 - z2
    return x,y,z

def ThreePointPlaneNormal(P1,P2,P3):
    '''
    Returns the normal of the plane defined by the three points.
    '''
    x1,y1,z1 = P1
    x2,y2,z2 = P2
    x3,y3,z3 = P3
    V12x, V12y, V12z = VectorThrough(P1, P2)
    V13x, V13y, V13z = VectorThrough(P1, P3)
    x = V12y * V13z - V12z * V13y
    y = V12z * V13x - V12x * V13z
    z = V12x * V13y - V12y * V13x
    return x,y,z

def TangentPlaneNormal(Point):
    x0,y0,z0 = Point
    x = (2*x0)/MajorAxis**2
    y = (2*y0)/MajorAxis**2
    z = (2*z0)/MinorAxis**2
    return x,y,z

def IntersectWithXYPlane(Point,Vector):
    x0,y0,z0 = Point
    a,b,c = Vector
    t = z0/c
    x = x0 - t*a
    y = y0 - t*b
    z = z0 - t*c
    return x,y,z

def Midpoint(P1,P2):
    '''
    Returns the midpoint of the line segment connecting the tow given points.
    '''
    x1,y1,z1 = P1
    x2,y2,z2 = P2
    x = (x1 + x2)/2
    y = (y1 + y2)/2
    z = (z1 + z2)/2
    return x,y,z

def PerpendicularVector(V1,V2):
    '''
    Returns a vector which is perpendicular to the two given vectors.
    (which in this case, are also perpendicular to each other.)
    '''
    V1x,V1y,V1z = V1
    V2x,V2y,V2z = V2
    
    x = (V1y*V2z - V1z*V2y)
    y = (V1z*V2x - V1x*V2z)
    z = (V1x*V2y - V1y*V2x)
    return x,y,z

def LineIntersect(P1,V1,P2,V2):
    '''
    Note that the Vs are the direction of the line, and the Ps are points
       which they pass through.
    Returns the point in which the two lines intersect in 3D Cartesian coords
    '''
    a1,b1,c1 = V1
    x1,y1,z1 = P1
    a2,b2,c2 = V2
    x2,y2,z2 = P2
    
    top = y1 - y2 + (b1/a1)*(x2-x1)
    bottom = b2 - (b1*a2)/a1
    s = top/bottom
    
    x = x2+a2*s  
    y = y2+b2*s
    z = z2+c2*s
    return x,y,z

def ThreePointCircumcenter(P1,P2,P3):
    M12 = Midpoint(P1, P2)
    M13 = Midpoint(P1, P3)
    PNormal = ThreePointPlaneNormal(P1, P2, P3)
    V12 = VectorThrough(P1, P2)
    V13 = VectorThrough(P1, P3)
    Perp12 = PerpendicularVector(V12, PNormal) ##Through M12
    Perp13 = PerpendicularVector(V13, PNormal) ##Through M13
    Circumcenter = LineIntersect(M12, Perp12, M13, Perp13)
    return Circumcenter

def XYPlaneCircumcenter(P1,P2,P3):
    T1 = TangentPlaneNormal(P1)
    T2 = TangentPlaneNormal(P2)
    T3 = TangentPlaneNormal(P3)
    I1 = IntersectWithXYPlane(P1, T1)
    I2 = IntersectWithXYPlane(P2, T2)
    I3 = IntersectWithXYPlane(P3, T3)
    C = ThreePointCircumcenter(I1, I2, I3)
    return C

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

def XYCircumplane (P1,P2,P3):
    PlaneNormal = ThreePointPlaneNormal(P1, P2, P3)
    XYCircumcenter = XYPlaneCircumcenter(P1, P2, P3)
    
    XYCircumPlane = IntersectionWithSpheroid(XYCircumcenter, PlaneNormal)
    
    return XYCircumPlane

def ZCoord(x,y):
    return sqrt(MinorAxis**2 * (1 - (x**2 + y**2)/MajorAxis**2))

P1 = (291.05, -392.21, ZCoord(291.05, -392.21))
P2 = (247.04, 102.64, ZCoord(247.04, 102.64))
P3 = (409.1, 409.1, ZCoord(409.1, 409.1))

TPN1 = TangentPlaneNormal(P1)
IXY1 = IntersectWithXYPlane(P1, TPN1)
print(IXY1)

