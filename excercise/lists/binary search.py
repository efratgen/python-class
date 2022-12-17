#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 10:46:57 2022

@author: efrat
"""

def binary_search (lst,item):
    start=0
    end=len(lst)-1
    while start<=end//2:
        mid_index=(start+end)//2
        if lst[mid_index]==item:
            return mid_index
        elif lst[mid_index]>item:
            end=mid_index-1
        else:
            start=mid_index+1
    return -1            
        
        
    