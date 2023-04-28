# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 08:22:47 2023

@author: a.babyak
"""
import Math

## Constants of Ellipsoid
SemiMajorAxis = 25
SemiMinorAxis = 12
Eccentricity = (SemiMajorAxis**2 - SemiMinorAxis**2)/SemiMajorAxis**2

def eta2(CenterLatitude):
    top = Eccentricity**2 * (Math.cos(CenterLatitude))**2
    bottom = 1 - Eccentricity**2
    return top / bottom

def V2(CenterLatitude):
    return 1 + eta2(CenterLatitude)

def t(CenterLatitude):
    return Math.tan(CenterLatitude)

def N(CenterLatitude):
    bottom = 1 - Eccentricity*(Math.sin(CenterLatitude))**2
    return SemiMajorAxis / Math.sqrt(bottom)

def c(CenterLatitude):
    return Math.cos(CenterLatitude)

def xValue(CenterLongitude,CenterLatitude,PointLongitude,PointLatitude):
    eta2C = eta2(CenterLatitude)
    V2C = V2(CenterLatitude)
    tC = t(CenterLatitude)
    NC = N(CenterLatitude)
    cC = c(CenterLatitude)
    Coeff10 = NC*cC
    Coeff11 = - (NC*cC*tC)/V2C
    Coeff30 = - (NC * cC**3 * tC**2)/6
    Coeff12 = - ((NC * cC**2)/(6 * V2C**2))*(2 + 2*eta2C + 9*eta2C*tC**2)
    Coeff31 = - ((NC * cC**3)/(6 * V2C)) * tC * (1 - tC**2 + eta2C)
    Coeff13 = - (((NC * cC)/(6 * V2C**3)) * eta2C * tC 
                 * (7 - 3 * tC**2 + 7 * eta2C + 12 * eta2C * tC**2))
    Coeff50 = - ((NC * cC**5)/120) * tC**3 * (3 - tC**2 + 3 * eta2C)
    Coeff32 = - (((NC * cC**3)/(180 * V2C**4)) 
                 * (8 - 40*tC**2 + eta2C * (16 - 31*tC**2)))
