#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 13:32:34 2022

@author: efrat
"""

import random
import math
n = int(input("number of play"))
k = int(input("number of equal"))
cntwin = 0
cnt = 0
for i in range(0, n):
    cube1 = random.randint(1, 6)
    cube2 = random.randint(1, 6)
    cube3 = random.randint(1, 6)
    print(cube1, cube2, cube3)
    if cube1 == cube2 and cube2 == cube3:
        cntwin += 1
    if k == cntwin:
        cnt = i
if cntwin >= k:
    print("you win, times to win:", cnt)
else:
    print("you loose, times of equal:", cntwin)