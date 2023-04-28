# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 15:55:55 2023

@author: a.babyak
"""

from sympy import Poly, Symbol, groebner,symbols

y = Symbol('y')
x = Symbol('x')
z = Symbol('z')
a = Symbol('a')
b = Symbol('b')
p1 = Poly(y*x + x**2 + y)
p2 = Poly(a*y*x + b*x -5)
g = groebner([p1,p2],x,y,z,order='lex')
aCoeffs = symbols('a:65')
print(g)