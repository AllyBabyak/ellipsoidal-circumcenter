# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 08:39:10 2023

@author: a.babyak
"""

import math
from math import sin, cos, atan, tan, atan2

a = 25
b = 12
f = (a-b)/a

def EllipsoidalDistance(Coord1, Coord2):
    phi1,L1 = Coord1
    phi2,L2 = Coord2
    
    L = L2 - L1
    
    U1 = atan((1-f)*tan(phi1))
    U2 = atan((1-f)*tan(phi2))
    
    lam = L
    mal = 0
    
    sinalpha = None
    sinsigma = None
    cos2sigmam = None
    cossigma = None
    sigma = None
    cos2alpha = None
    
    while abs(lam - mal) > 10**(-12):
        sinsigma = math.sqrt((cos(U2)*sin(lam))**2 
                             + (cos(U1)*sin(U2) - sin(U1)*cos(U2)*cos(lam))**2)
        cossigma = sin(U1)*sin(U2) + cos(U1)*cos(U2)*cos(lam)
        sigma = atan2(sinsigma, cossigma)
        sinalpha = (cos(U1)*cos(U2)*sin(lam))/sinsigma
        cos2alpha = (1 - sinalpha**2)
        cos2sigmam = cossigma - (2*sin(U1)*sin(U2))/cos2alpha
        C = (f/16)*cos2alpha*(4 + f*(4 - 3*cos2alpha))
        mal = lam
        lam = L + (1-C)*f*sinalpha*(sigma + C*sinsigma
                                    *(cos2sigmam + C*cossigma
                                      *(-1 + 2*cos2sigmam**2)))
        
    u2 = cos2alpha**2 * ((a**2-b**2))/(b**2)
    A = 1 + (u2/16384)*(4096 + u2*(-768 + u2*(320 - 175*u2)))
    B = (u2/1024)*(256 + u2*(-128 + u2*(74 - 47*u2)))
    deltasigma = B*sinsigma*(cos2sigmam 
                             + (1/4)*B*(cossigma*(-1 + 2*cos2sigmam**2) 
                                        - (B/6)*cos2sigmam*(-3 + 4*sinsigma**2)
                                        *(-3 + 4*cos2sigmam**2)))
    s = b*A*(sigma - deltasigma)
    
    return s