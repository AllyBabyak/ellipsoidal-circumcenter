# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 12:39:43 2023

@author: a.babyak
"""

from sympy import Poly, Symbol, groebner, symbols

L = Symbol('L')
B = Symbol('B')
r = Symbol('r')
x = symbols('x(:c)')
y = symbols('y(:c)')

givenL = symbols('L(:c)')
givenB = symbols('B(:c)')
a = symbols('a0:51')
b = symbols('b0:51')
c = symbols('c0:51')

fLa = Poly(givenL[0] + a[10]*x[0] + a[11]*x[0]*y[0] + a[30]*x[0]**3 
           + a[12]*x[0]*y[0]**2 + a[31]*x[0]**3*y[0] + a[13]*x[0]*y[0]**3
           + a[50]*x[0]**5 + a[32]*x[0]**3*y[0]**2 + a[14]*x[0]*y[0]**4 - L)
fLb = Poly(givenL[1] + b[10]*x[1] + b[11]*x[1]*y[1] + b[30]*x[1]**3 
           + b[12]*x[1]*y[1]**2 + b[31]*x[1]**3*y[1] + b[13]*x[1]*y[1]**3
           + b[50]*x[1]**5 + b[32]*x[1]**3*y[1]**2 + b[14]*x[1]*y[1]**4 - L)
fLc = Poly(givenL[2] + c[10]*x[2] + c[11]*x[2]*y[2] + c[30]*x[2]**3 
           + c[12]*x[2]*y[2]**2 + c[31]*x[2]**3*y[2] + c[13]*x[2]*y[2]**3
           + c[50]*x[2]**5 + c[32]*x[2]**3*y[2]**2 + c[14]*x[2]*y[2]**4 - L)

fBa = Poly(givenB[0] + a[1]*y[0] + a[20]*x[0]**2 + a[2]*y[0]**2 
           + a[21]*x[0]**2*y[0] + a[3]*y[0]**3 + a[40]*x[0]**4 
           + a[22]*x[0]**2*y[0]**2 + a[4]*y[0]**4 + a[41]*x[0]**4*y[0]
           + a[23]*x[0]**2*y[0]**3 + a[5]*y[0]**5 - B)
fBb = Poly(givenB[1] + b[1]*y[1] + b[20]*x[1]**2 + b[2]*y[1]**2 
           + b[21]*x[1]**2*y[1] + b[3]*y[1]**3 + b[40]*x[1]**4 
           + b[22]*x[1]**2*y[1]**2 + b[4]*y[1]**4 + b[41]*x[1]**4*y[1]
           + b[23]*x[1]**2*y[1]**3 + b[5]*y[1]**5 - B)
fBc = Poly(givenB[2] + c[1]*y[2] + c[20]*x[2]**2 + c[2]*y[2]**2 
           + c[21]*x[2]**2*y[2] + c[3]*y[2]**3 + c[40]*x[2]**4 
           + c[22]*x[2]**2*y[2]**2 + c[4]*y[2]**4 + c[41]*x[2]**4*y[2]
           + c[23]*x[2]**2*y[2]**3 + c[5]*y[2]**5 - B)

ra = Poly(x[0]**2 + y[0]**2 - r**2)
rb = Poly(x[1]**2 + y[1]**2 - r**2)
rc = Poly(x[2]**2 + y[2]**2 - r**2)

g = groebner([fLa,fLb,fLc, fBa, fBb, fBc, ra, rb, rc],L,B,r,x[0],x[1],x[2],y[0],y[1],y[2],order='lex')
print(g)