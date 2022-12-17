#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 12:48:41 2022

@author: efrat
"""
import random
print ("1. throw one dice")
print ("2. throw two dice")
print ("3. quit")
n=int(input("choose 1 option from the menu:"))
x=random.randint(1,6)
y=random.randint(1,6)
z=random.randint(1,6)
a=random.randint(1,6)
if n==1:
    print(x)
    n=x
elif n==2:
    print(x)
    print(y)
    n=(x+y)
elif n==3:
    print("bye")    
if n!=3:
 n2=int(input("choose 1 more option from the menu:"))
 if n2==1:
    print(z)
    n2=z
 elif n2==2:
    print(z)
    print(a)
    n2=(z+a)
 elif n2==3:
     print ("bye")
if n2!=3:    
   v=(n+n2)
   print("total=",v)
   if v==12 or v<4:
      print ("you win")
   else:
      print("you loose")
    
    
    