#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 13:04:06 2022

@author: efrat
"""

a=int(input("choose number a"))
b=int(input("choose number b"))
c=int(input("choose number c"))
if b**2-(4*a*c)>0:
    print ("2 solutions")
    x1=(-b+(b**2-4*a*c)**0.5)/(2*a)
    x2=(-b-(b**2-4*a*c)**0.5)/(2*a)
    print (x1,x2)
elif b**2-4*a*c==0:
    print ("1 solution")
    x=(-b)/2*a
    print (x)
else:
    print ("no solution for this quadradic equation")
    