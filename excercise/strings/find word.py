#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 11:03:21 2022

@author: efrat
"""

def find_words(s,c):
    l=[]
    wl=s.split()
    for word in wl:
        if word.lower().startswith(c):
            l.append(word)
    return l        

def main ():
    
    s="why how who"
    wsplit=find_words(s,'w')
    print (wsplit)
    
main ()    