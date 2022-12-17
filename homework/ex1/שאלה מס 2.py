#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 12:28:38 2022

@author: efrat
"""

n=int(input("הכנס מספר בן 3 ספרות"))
if 100<=n<=999:
    print(n%10)
    n=int((n-n%10)/10)
    print(n%10)
    n=int((n-n%10)/10)
    print(n)
else:
    print ("error")
    
    

    