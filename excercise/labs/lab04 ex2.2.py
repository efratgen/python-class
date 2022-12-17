#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 14:17:00 2022

@author: efrat
"""
base=int(input("enter base"))
spaces=0
for i in range(0,base):
    stars=1+(i*2)
    spaces=int((base-stars)/2)
    print(spaces*" "+stars*"*"+spaces*" ")
    
