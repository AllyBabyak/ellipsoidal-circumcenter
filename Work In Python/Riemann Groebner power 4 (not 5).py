# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 07:59:55 2023

@author: a.babyak
"""

from sympy import Poly, Symbol, groebner, symbols

L = Symbol('L')
B = Symbol('B')
r = Symbol('r')

xCoeffs = symbols('x:9')
yCoeffs = symbols('y:11')

givenL = symbols('L:3')
givenB = symbols('B:3')

b0 = Poly(B-givenB[0],B)
l0 = Poly(L-givenL[0],L)
b1 = Poly(B-givenB[1],B)
l1 = Poly(L-givenL[1],L)
b2 = Poly(B-givenB[2],B)
l2 = Poly(L-givenL[2],L)

X0 = Poly(xCoeffs[0]*l0 + xCoeffs[1]*l0*b0 + xCoeffs[2]*l0**3 
          + xCoeffs[3]*l0*b0**2 + xCoeffs[4]*l0**3*b0 + xCoeffs[5]*l0*b0**3)

X1 = Poly(xCoeffs[0]*l1 + xCoeffs[1]*l1*b1 + xCoeffs[2]*l1**3 
          + xCoeffs[3]*l1*b1**2 + xCoeffs[4]*l1**3*b1 + xCoeffs[5]*l1*b1**3)

X2 = Poly(xCoeffs[0]*l2 + xCoeffs[1]*l2*b2 + xCoeffs[2]*l2**3 
          + xCoeffs[3]*l2*b2**2 + xCoeffs[4]*l2**3*b2 + xCoeffs[5]*l2*b2**3)

Y0 = Poly(yCoeffs[0]*b0 + yCoeffs[1]*l0**2 + yCoeffs[2]*b0**2 
          + yCoeffs[3]*l0**2*b0 + yCoeffs[4]*b0**3 + yCoeffs[5]*l0**4 
          + yCoeffs[6]*l0**2*b0**2 + yCoeffs[7]*b0**4)

Y1 = Poly(yCoeffs[0]*b1 + yCoeffs[1]*l1**2 + yCoeffs[2]*b1**2 
          + yCoeffs[3]*l1**2*b1 + yCoeffs[4]*b1**3 + yCoeffs[5]*l1**4 
          + yCoeffs[6]*l1**2*b1**2 + yCoeffs[7]*b1**4)

Y2 = Poly(yCoeffs[0]*b2 + yCoeffs[1]*l2**2 + yCoeffs[2]*b2**2 
          + yCoeffs[3]*l2**2*b2 + yCoeffs[4]*b2**3 + yCoeffs[5]*l2**4 
          + yCoeffs[6]*l2**2*b2**2 + yCoeffs[7]*b2**4)

f0 = Poly(X0**2 + Y0**2 + r**2, L,B,r)
f1 = Poly(X1**2 + Y1**2 + r**2, L,B,r)
f2 = Poly(X2**2 + Y2**2 + r**2, L,B,r)

g = groebner([f0,f1,f2],L,B,r,order='lex')
print(g)