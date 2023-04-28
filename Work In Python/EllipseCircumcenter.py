# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 08:35:06 2023

@author: a.babyak
"""

from math import sqrt

MajorAxis = 6378137.0 
MinorAxis = 6356752.314245
e2 = (MajorAxis**2 - MinorAxis**2)/(MajorAxis**2)

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

def VectorLength(Vector):
    x,y,z = Vector
    Length = sqrt(x**2 + y**2 + z**2)
    return Length

def VectorScale(Vector,Scalar):
    x,y,z = Vector
    X = x * Scalar
    Y = y * Scalar
    Z = z * Scalar
    return X,Y,Z

def DotProduct3D(V1,V2):
    x1,y1,z1 = V1
    x2,y2,z2 = V2
    return x1*x2 + y1*y2 + z1*z2
    

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
    
    top = a1*(y1 - y2) + b1*(x2-x1)
    bottom = a1*b2 - (b1*a2)
    
    if bottom == 0:
        top = c1*(y1 - y2) + b1*(z2-z1)
        bottom = c1*b2 - (b1*c2)
        if bottom == 0:
            top = a1*(z1 - z2) + c1*(x2-x1)
            bottom = a1*c2 - (a1*c2)
            if bottom == 0:
                print("error")
        
    s = top/bottom
    
    x = x2+a2*s  
    y = y2+b2*s
    z = z2+c2*s
    return x,y,z

def ThreePointCircumcenter(P1,P2,P3):
    
    if P1 == P2 == P3:
        return P1
    
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
    
    if M12 == (0,0,0):
        Circumcenter = LineIntersect(M23, Perp23, M13, Perp13)
    elif M13 == (0,0,0):
        Circumcenter = LineIntersect(M23, Perp23, M12, Perp12)
    elif M23 == (0,0,0):
        print("Error")
    else:
        Circumcenter = LineIntersect(M12, Perp12, M13, Perp13)
    return Circumcenter

def Circumcenter2(P1,P2,P3):
    if P1 == P2 == P3:
        return P1
    
    u1 = VectorThrough(P2, P1)
    w1 = PerpendicularVector(VectorThrough(P3, P1), u1)
    Lu = VectorLength(u1)
    Lw = VectorLength(w1)
    u = VectorScale(u1, 1/Lu)
    w = VectorScale(w1, 1/Lw)
    v = PerpendicularVector(w, u)
    
    bx = DotProduct3D(VectorThrough(P2,P1), u)
    
    cx = DotProduct3D(VectorThrough(P3,P1), u)
    cy = DotProduct3D(VectorThrough(P3,P1), v)
    
    top = (cx - bx/2)**2 + cy**2 - (bx/2)**2
    h = top / (2*cy)
    
    FromU = VectorScale(u, (bx/2))
    FromV = VectorScale(v, h)
    
    x1,x2,x3 = P1
    u1,u2,u3 = FromU
    v1,v2,v3 = FromV
    
    X = x1 + u1 + v1
    Y = x2 + u2 + u2
    Z = x3 + u3 + v3
    return X,Y,Z

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

def TangentPlaneNormal(Point):
    x0,y0,z0 = Point
    x = (2*x0)/MajorAxis**2
    y = (2*y0)/MajorAxis**2
    z = (2*z0)/MinorAxis**2
    
    if (x + y + z) < (10**(-5)):
        x = x * 10**10
        y = y * 10**10
        z = z * 10**10
    
    return x,y,z

def IntersectWithXYPlane(Point,Vector):
    x0,y0,z0 = Point
    a,b,c = Vector
    t = z0/c
    x = x0 - t*a
    y = y0 - t*b
    z = z0 - t*c
    return x,y,z
    
def XYPlaneCircumcenter(P1,P2,P3):
    T1 = TangentPlaneNormal(P1)
    T2 = TangentPlaneNormal(P2)
    T3 = TangentPlaneNormal(P3)
    
    if T1[2] == 0:
        I1 = (0,0,0)
    else:
        I1 = IntersectWithXYPlane(P1, T1)
    if T2[2] == 0:
        I2 = (0,0,0)
    else:
        I2 = IntersectWithXYPlane(P2, T2)
    if T3[2] == 0:
        I3 = (0,0,0)
    else:
        I3 = IntersectWithXYPlane(P3, T3)
        
    C = ThreePointCircumcenter(I1, I2, I3)
    return C

def Center(P1,P2,P3):
    PlaneNormal = ThreePointPlaneNormal(P1, P2, P3)
    Circumcenter = ThreePointCircumcenter(P1, P2, P3)
    XYCircumcenter = XYPlaneCircumcenter(P1, P2, P3)
    Vector = VectorThrough(Circumcenter, XYCircumcenter)
    
    CircumPlane = IntersectionWithSpheroid(Circumcenter, PlaneNormal)
    XYCircumPlane = IntersectionWithSpheroid(XYCircumcenter, PlaneNormal)
    
    if Vector == (0,0,0):
        XYCC = XYCircumPlane
    else:
        XYCC = IntersectionWithSpheroid(Circumcenter, Vector)
    
    return CircumPlane, XYCircumPlane, XYCC 

def ZCoord(x,y):
    return sqrt(MinorAxis**2 * (1 - (x**2 + y**2)/MajorAxis**2))

def SameLongCenter(P1, P2, P3):
    x1,y1,z1 = P1
    x2,y2,z2 = P2
    x3,y3,z3 = P3
    V12x, V12y, V12z = VectorThrough(P1, P2)
    V13x, V13y, V13z = VectorThrough(P1, P3)
    x = V12y * V13z - V12z * V13y
    y = V12z * V13x - V12x * V13z
    PNormal =  x,y,0
    M12 = Midpoint(P1, P2)
    M13 = Midpoint(P1, P3)
    M23 = Midpoint(P2, P3)
    V12 = VectorThrough(P1, P2)
    V13 = VectorThrough(P1, P3)
    V23 = VectorThrough(P2, P3)
    Perp12 = PerpendicularVector(V12, PNormal) ##Through M12
    Perp13 = PerpendicularVector(V13, PNormal) ##Through M13
    Perp23 = PerpendicularVector(V23, PNormal)
    
    if M12 == (0,0,0):
        Circumcenter = LineIntersect(M23, Perp23, M13, Perp13)
    elif M13 == (0,0,0):
        Circumcenter = LineIntersect(M23, Perp23, M12, Perp12)
    elif M23 == (0,0,0):
        print("Error")
    else:
        Circumcenter = LineIntersect(M12, Perp12, M13, Perp13)
    Centers = IntersectionWithSpheroid(Circumcenter, PNormal)
    return Centers

'''
P1 = (4573439.516781955, 3851141.7382213185, 2213586.813393494)
P2 = (4601815.230201581, 3822101.18206384, 2205152.736344949)
P3 = (4571652.673357664, 3892597.2916538604, 2144137.608872433)
PlaneNormal = ThreePointPlaneNormal(P1, P2, P3)
Circumcenter = ThreePointCircumcenter(P1, P2, P3)
XYC = XYPlaneCircumcenter(P1,P2,P3)
print(Circumcenter,XYC)
'''
