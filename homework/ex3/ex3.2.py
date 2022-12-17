#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 13:18:22 2022

@author: efrat
"""

def upseries (lst):
    check=0
    for value in lst:
        if value>=check:
            check=value
        else:
            return "false"
    return "true"    
        
        
         
def uplist (lst):
    newlist=sorted(lst)
    
        
    return newlist   

    
def multinums (list1,list2):
    newlist=[]
    lengh= len(list1)
    for i in range (lengh):
        newlist.append(list1[i]*list2[i])
    return newlist    


def main():
    llist=[1,2,3,4,5,6]
    lllist=[9,6,8,3,8,0]
    listx=[1,2,3]
    listy=[2,3,4]
    print (upseries(llist))
    print (uplist(lllist))
    print (multinums(listx,listy))
main ()    

