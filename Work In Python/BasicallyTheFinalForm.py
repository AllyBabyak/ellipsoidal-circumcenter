# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 09:31:29 2023

@author: a.babyak
"""

from math import atan, tan, sin, sqrt, cos, atan2, radians, degrees, asin

MajorAxis = 6378137.0 
MinorAxis = 6356752.314245
e2 = (MajorAxis**2 - MinorAxis**2)/(MajorAxis**2)
f = 1/298.257223563

def VincentyInverse(Coord1, Coord2):
    phi1, L1 = Coord1
    phi2, L2 = Coord2
    
    if phi1 == phi2 == 0:
        s = MajorAxis*abs(L1 - L2)
        return s
    
    U1 = atan((1 - f)*tan(phi1))
    U2 = atan((1 - f)*tan(phi2))
    L = L2 - L1
    
    maxIter = 500
    tol=10**(-12)
    lam = L
    
    for i in range(0,maxIter):
        sinsigma = sqrt((cos(U2)*sin(lam))**2 
                        + (cos(U1)*sin(U2) - sin(U1)*cos(U2)*cos(lam))**2)
        cossigma = sin(U1)*sin(U2) + cos(U1)*cos(U2)*cos(lam)
        sigma = atan2(sinsigma, cossigma)
        sinalpha = (cos(U1)*cos(U2)*sin(lam))/sinsigma
        cos2sigmam = cossigma - (2*sin(U1)*sin(U2))/(1 - sinalpha**2)
        C = (f/16) * (1-sinalpha**2) * (4 + f*(4 - 3*(1 - sinalpha**2)))
        mal = lam
        lam = L + (1-C)*f*sinalpha*(sigma + C*sinsigma*(cos2sigmam+C*cossigma*(-1 + 2*cos2sigmam**2)))
        
        diff = abs(lam - mal)
        if diff < tol:
            break
        
    u2 = (1-sinalpha**2)*((MajorAxis**2 - MinorAxis**2)/MinorAxis**2)
    A = 1 + (u2/16384)*(4096 + u2*(-768 + u2*(320 - 175*u2)))
    B = (u2/1024)*(256 + u2*(-128 + u2*(74 - 47*u2)))
    deltasigma = B*sinsigma*(cos2sigmam + 1/4 * B * (cossigma*(-1 + 2*cos2sigmam**2)
                                                     - B/6 * cos2sigmam * (-3 + 4*sinsigma**2)*(-3 + 4*cos2sigmam**2)))
    s = MinorAxis*A*(sigma-deltasigma)
    return s

def VincentyForward(Coord1, azimuth, distance):
    phi1,L1 = Coord1
    
    U1 = atan((1 - f)*tan(phi1))
    sigma1 = atan2(tan(U1), cos(azimuth))
    sinalpha = cos(U1)*sin(azimuth)
    u2 = (1-sinalpha**2) * ((MajorAxis**2 - MinorAxis**2)/(MinorAxis**2))
    A = 1 + (u2/16384)*(4096 + u2*(-768 + u2*(320 - 175*u2)))
    B = (u2/1024)*(256 + u2*(-128 + u2*(74 - 47*u2)))
    
    maxIter = 500
    tol=10**(-12)
    sigma = distance / (MinorAxis*A)
    
    for i in range(0,maxIter):
        twosigmam = 2*sigma1 + sigma
        deltasigma = B*sin(sigma) * (cos(twosigmam) + 1/4 * B * (cos(sigma)*(1 - 2 * cos(twosigmam))
                                                               - B/6 * cos(twosigmam) * (-3 + 4*sin(sigma)**2) * (-3 + 4 * cos(twosigmam)**2)))
        amgis = sigma
        sigma = distance/(MinorAxis * A) + deltasigma
        
        diff = abs(sigma - amgis)
        if diff < tol:
            break
        
    phiy = sin(U1)*cos(sigma) + cos(U1)*sin(sigma)*cos(azimuth)
    phix = (1-f)*sqrt(sinalpha**2 + (sin(U1)*sin(sigma) - cos(U1)*cos(sigma)*cos(azimuth))**2)
    phi2 = atan2(phiy, phix)
    lamy = sin(sigma)*sin(azimuth)
    lamx = cos(U1)*cos(sigma) - sin(U1)*sin(sigma)*cos(azimuth)
    lam = atan2(lamy, lamx)
    C = f/16 * (1 - sinalpha**2) * (4 + f*(f - (1 - sinalpha**2)))
    L = lam - (1 - C)*f*sinalpha*(sigma + C*sin(sigma * (cos(twosigmam) + C*cos(sigma) * (-1 + 2 * cos(twosigmam)**2))))
    L2 = L + L1
    return phi2, L2

def GeodeticToXYZ(Coord):
    lat,long = Coord
    N = MajorAxis/(sqrt(1 - e2 * sin(lat)**2))
    x = N * cos(lat) * cos(long)
    y = N * cos(lat) * sin(long)
    z = (1 - e2) * N * sin(lat)
    return x,y,z

def XYZToGeodetic(Coord):
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
    
    if M12 == (0,0,0):
        Circumcenter = LineIntersect(M23, Perp23, M13, Perp13)
    elif M13 == (0,0,0):
        Circumcenter = LineIntersect(M23, Perp23, M12, Perp12)
    else:
        Circumcenter = LineIntersect(M12, Perp12, M13, Perp13)
    return Circumcenter

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

def Center(P1,P2,P3):
    PlaneNormal = ThreePointPlaneNormal(P1, P2, P3)
    Circumcenter = ThreePointCircumcenter(P1, P2, P3)
    
    CircumPlane = IntersectionWithSpheroid(Circumcenter, PlaneNormal)
    
    return CircumPlane

def CoordToRadians(Coord):
    C1,C2 = Coord
    C1 = radians(C1)
    C2 = radians(C2)
    return C1,C2

def CoordToDegrees(Coord):
    C1,C2 = Coord
    C1 = degrees(C1)
    C2 = degrees(C2)
    return C1,C2

def Distance3D(Coord1, Coord2):
    x1,y1,z1 = Coord1
    x2,y2,z2 = Coord2
    distance = sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
    return distance

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
        Coord = CoordToRadians(Coord)
        x,y,z = GeodeticToXYZ(Coord)
    return x,y,z
