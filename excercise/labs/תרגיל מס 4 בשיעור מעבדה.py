#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 13:33:37 2022

@author: efrat
"""

calculate=str(input ("choose +,-,*,/"))
num1=float(input( "choose number"))
num2=float(input("choose another number"))
if calculate=="+":
    print (num1+num2)
    print ("simple calculator ended")
elif calculate=="-":
    print (num1-num2)
    print ("simple calculator ended")
elif calculate=="*":
    print (num1*num2)
    print ("simple calculator ended")
elif calculate=="/":
    print (num1/num2)
    print("simple calculator ended")
else:
    print ("error")
