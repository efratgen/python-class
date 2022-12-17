#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 10:46:09 2022

@author: efrat
"""
num=int(input("insert number"))
sumnum=1
if num<=1:
    print ("error")
else:
    for i in range (num,1000):
        sumnum=1
        for j in range(2,i):
            if i%j==0:
                sumnum+=j
        if sumnum==i:
            print(i)
            
          
    