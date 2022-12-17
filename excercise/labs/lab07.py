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
        return "x"
    else:
        return "o"
        
def place_icon (lst,player,index) :
    if lst[index] == " ":
        lst[index]=player
    else: 
        print ("can not, try again")
        
def space_check (lst,index):
    if lst[index-1]==" " :
        return "true"
    else:
        return "false"
    
def full_board_check (lst):
    for i in lst:
        if i==" ":
            return "false"
    return "true"

def win_check (lst,player):
     if player==lst[0] and lst[0]==lst[3] and lst[3]==lst[6]:
         return "true"
     if player==lst[1] and lst[1]==lst[4] and lst[4]==lst[7]:
         return "true"
     if player==lst[2] and lst[2]==lst[5] and lst[5]==lst[8]:
         return "true"
     if player==lst[0] and lst[0]==lst[1] and lst[1]==lst[2]:
         return "true"
     if player==lst[3] and lst[3]==lst[4] and lst[4]==lst[5]:
         return "true"
     if player==lst[6] and lst[6]==lst[7] and lst[7]==lst[8]:
         return "true"
     if player==lst[0] and lst[0]==lst[4] and lst[4]==lst[8]:
         return "true"
     if player==lst[2] and lst[2]==lst[4] and lst[4]==lst[6]:
         return "true"
     else:
         return "false"
     
def player_choise (lst) :
    index=int(input("insert index between 1-9"))
    while index>9 or index<1 or space_check(lst,index)=="false":
        index=int(input("insert index between 1-9"))
    return index

def replay ():
    replay=input("wanna play again? (press y or n)")
    if replay== "y":
        return "true"
    else: 
        return "false"
    
        
    
def main ():
    xo=[" "," "," "," "," "," "," "," "," "]
    
    
    
    while replay()=="true":
        print(display_board(xo))
        if choose_first()=="x":
            player1="x"
            player2="o"
        else:
            player1= "o"
            player2=="x"
        print(f'{player1} beggins')
    
main()    

