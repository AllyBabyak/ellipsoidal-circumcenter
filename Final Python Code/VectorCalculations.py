# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 14:53:32 2023

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

def ThreePointCircumcenterOld(P1,P2,P3):
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
    else:
        Circumcenter = LineIntersect(M12, Perp12, M13, Perp13)
    return Circumcenter

def ThreePointCircumcenter(P1,P2,P3):
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

def QuadraticFormula(A,B,C):
    determinant = (B**2 - 4*A*C)
    if determinant < 0:
        x1 = (-B)/(2*A)
        x2 = (-B)/(2*A)
    else:
        bottom = 2*A
        x1 = (-B + sqrt(determinant))/bottom
        x2 = (-B - sqrt(determinant))/bottom
    return x1,x2

def IntersectionWithSpheroid(Point,Vector):
    x0,y0,z0 = Point
    a,b,c = Vector
    A = (a**2 + b**2)/(MajorAxis**2) + (c**2)/(MinorAxis**2)
    B = 2 * ((a*x0 + b*y0)/(MajorAxis**2) + (c*z0)/(MinorAxis**2))
    C = (x0**2 + y0**2)/(MajorAxis**2) + (z0**2)/(MinorAxis**2) - 1
    if A !=0:
        Solutions = QuadraticFormula(A, B, C)
    else:
        Solutions = ((-C)/B),((-C)/B)
    x1 = x0 + Solutions[0]*a
    x2 = x0 + Solutions[1]*a
    y1 = y0 + Solutions[0]*b
    y2 = y0 + Solutions[1]*b
    z1 = z0 + Solutions[0]*c
    z2 = z0 + Solutions[1]*c
    return (x1,y1,z1),(x2,y2,z2)
    

def Distance3D(Coord1, Coord2):
    x1,y1,z1 = Coord1
    x2,y2,z2 = Coord2
    distance = sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
    return distance

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
    
def XYZArcCenter(P1,P2,P3):
    PlaneNormal = ThreePointPlaneNormal(P1, P2, P3)
    Circumcenter = ThreePointCircumcenter(P1, P2, P3)
    PotentialCenters = IntersectionWithSpheroid(Circumcenter, PlaneNormal)
    
    ArcCenter = CenterPick(P1, P2, P3, PotentialCenters)
    return ArcCenter

def CompareThreeValuesThreshold(V1,V2,V3,Threshold):
    C12 = abs(V1 - V2)
    C13 = abs(V1 - V3)
    C23 = abs(V2 - V3)
    if (C12 > Threshold) or (C13 > Threshold) or (C23 > Threshold):
        return False
    else:
        return True
    
def CompareToCircumcenterThreshold(P1,P2,P3,C,Threshold):
    D1 = Distance3D(P1, C)
    D2 = Distance3D(P2, C)
    D3 = Distance3D(P3, C)
    return CompareThreeValuesThreshold(D1, D2, D3, Threshold)

def LargestError(V1,V2,V3):
    C12 = abs(V1 - V2)
    C13 = abs(V1 - V3)
    C23 = abs(V2 - V3)
    return max(C12, C13, C23)

def LargestCircumcenterError(P1,P2,P3,C):
    D1 = Distance3D(P1, C)
    D2 = Distance3D(P2, C)
    D3 = Distance3D(P3, C)
    return LargestError(D1, D2, D3)

def DotProduct(V1,V2):
    V1x, V1y, V1z = V1
    V2x, V2y, V2z = V2
    return V1x*V2x + V1y*V2y + V1z*V2z