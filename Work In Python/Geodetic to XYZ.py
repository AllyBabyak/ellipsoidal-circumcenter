# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:14:50 2023

@author: a.babyak
"""

from math import sqrt, sin,cos

SemiMajorAxis = 6378137.0 
SemiMinorAxis = 6356752.314245
e2 = (SemiMajorAxis**2 - SemiMinorAxis**2)/(SemiMajorAxis**2)


def GeodeticToXYZ(lat,long):
    N = SemiMajorAxis/(sqrt(1 - e2 * sin(lat)**2))
    x = N * cos(lat) * cos(long)
    y = N * cos(lat) * sin(long)
    z = (1 - e2) * N * sin(lat)
    return x,y,z

test = GeodeticToXYZ(0.3451159890927403, 0.7053433296787647)
print(test)