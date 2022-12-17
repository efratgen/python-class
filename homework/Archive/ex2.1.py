#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 14:47:54 2022

@author: efrat
"""

user=int(input("insert number, press 0 to stop"))
maxx=user
minx=user
cntmax=0
cntmin=0
locationmax=1
locationmin=1
sumx=0
while user!=0:
    cntmax+=1
    cntmin+=1
    sumx+=user
    avg=sumx/(cntmin)
    if user>maxx:
        maxx=user
        locationmax=cntmax
    if user<minx:
        minx=user
        locationmin=cntmin
    user=int(input("insert number, press 0 to stop"))
print("maximum is:",maxx, "location is:", locationmax)
print("minimum is:",minx, "location is:", locationmin)      
print("sum is",sumx)
print("avg is:", avg)