# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 14:27:51 2023

@author: a.babyak
"""

from math import atan,tan,sqrt,cos,sin,atan2
from CoordinateConversions import DegreesToRadians, XYZToRadians

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

def ErrorTest(Coord1,Coord2,Coord3,CalcCenter, AngleType):
    if AngleType == "Degrees": 
        P1 = DegreesToRadians(Coord1)
        P2 = DegreesToRadians(Coord2)
        P3 = DegreesToRadians(Coord3)
        C = DegreesToRadians(CalcCenter)
    elif AngleType == "Radians":
        P1 = Coord1
        P2 = Coord2
        P3 = Coord3
        C = CalcCenter
    elif AngleType == "XYZ":
        P1 = XYZToRadians(Coord1)
        P2 = XYZToRadians(Coord2)
        P3 = XYZToRadians(Coord3)
        C = XYZToRadians(CalcCenter)
    
    D1 = VincentyInverse(P1, C)
    D2 = VincentyInverse(P2, C)
    D3 = VincentyInverse(P3, C)
    Error = max(D1,D2,D3) - min(D1,D2,D3)
    return Error

def StringToCoord(Coord):
    NoBrac = Coord[1:-1]
    List = NoBrac.split(', ')
    lat = float(List[0])
    long = float(List[1])
    return lat,long
