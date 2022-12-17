# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 12:06:28 2021

@author: דוניטה כהן
"""
import math

def lcm(x,z):
    t=(x*z)//math.gcd(x,z)
    return t
   
x= int(input("insert first number")) 
z= int(input("insert second number"))
while x!=0 and z!=0:
    print (lcm(x,z))
    x= int(input("insert first number")) 
    z= int(input("insert second number"))
    
    
     
        
        
        
        
    