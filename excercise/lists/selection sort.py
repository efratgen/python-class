#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 11:14:26 2022

@author: efrat
"""

def selection_sort(lst):
    for index in range (len(lst)-1):
        min_index=index
        for k in range(index+1,len(lst)):
            if lst[min_index]>lst[k]:
                min_index=k
        lst[index],lst[min_index]=lst[min_index],lst[index]        