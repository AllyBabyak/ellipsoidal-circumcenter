# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 10:01:14 2023

@author: a.babyak
"""

import sympy

SemiMajorAxis = 25
SemiMinorAxis = 12

def ZCoord(XCoord, YCoord):
    Inner = SemiMinorAxis**2 * (1 - (XCoord**2 + YCoord**2)/SemiMajorAxis**2)
    Z = sympy.sqrt(Inner)
    return Inner, Z

## Points
A = ()