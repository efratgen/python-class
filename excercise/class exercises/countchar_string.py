#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 15:12:38 2022

@author: efrat
"""

def countchar(s,c):
    cnt=0
    for t in s:
        if t==c:
            cnt+=1
    return cnt        