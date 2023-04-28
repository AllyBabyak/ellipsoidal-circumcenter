# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 07:51:00 2023

@author: a.babyak
"""

from math import sqrt

a = 600
b = 500

def TangentPlane(XCoeff,YCoeff,ZCoeff):
    bottom = a**2 * (XCoeff**2 + YCoeff**2) + b**2 * ZCoeff**2
    d = sqrt(4/bottom)
    x0 = (a**2 * d * XCoeff)/2
    y0 = (a**2 * d * YCoeff)/2
    z0 = (b**2 * d * ZCoeff)/2
    return x0,y0,z0

print(TangentPlane(87415.29,30338.61,55658.5))