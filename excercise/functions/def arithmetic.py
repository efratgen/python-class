#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 13:40:46 2022

@author: efrat
"""

def arithmetic (first, step, location):
    i=first+(location-1)*step
    return i

def arithmetic_geometric (a,b,c):
    if a-b == b-c:
        return f"{a},{b},{c} is arithmetic"
    elif a/b == b/c:
        return f"{a},{b},{c} is geometric"
    else:
        return f"none"
        

def main ():
    y= arithmetic (2,3,6)
    print (y)
    print (arithmetic_geometric (2,6,10))

main ()

    
    

