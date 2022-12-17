#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 12:41:08 2022

@author: efrat
"""
import random
def display_board (lst):
    for i in range (len(lst)):
        if (i+1)%3==0:
            print (f'   !   !   ')
            print (f' {lst[i-2]} ! {lst[i-1]} ! {lst[i]} ')
            print (f'   !   !   ')
            if i!=8:
                print (11*"-")

def choose_first ():
    first=random.randint(1,2)
    if first==1:
        print ("first is x")
    else:
        print ("first is y")
        
    
def main ():
    xo=[" ","X"," ","O","X"," ","O"," ","X"]
    display_board(xo)
    
    choose_first()
    
main()    

