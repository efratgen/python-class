#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 16:35:18 2022

@author: efrat
"""

def firstletter (lst):
    newlist=[]
    for i in lst:
        newlist.append(i[0])
    return newlist

def reverse (lst):
    newlist=[]
    for i in range (1,len(lst)+1):
        newlist.append(lst[-i])
    return newlist  

def swipe (lst):
    newlist=[]
    for i in lst:
        newlist.append(i[::-1])
    return newlist    
            
def mix (lst1,lst2):
    newlist=[]
    lengh=len(lst1)
    if len(lst1)!=len(lst2):
        print ('error', newlist)
    else:
        for i in range (lengh):
            newlist.append(lst1[i]+lst2[i])
        return newlist
    
            
            

def main ():
    list1=["hey","how","are","you"] 
    pluslist1=["we","are","the","champions"]
    pluslist2=["we","keep","on","fighting"]
    print (firstletter(list1))
    print (reverse(list1))
    print (swipe(list1))
    print (mix(pluslist1,pluslist2))
main()    