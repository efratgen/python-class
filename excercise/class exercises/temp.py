# -*- coding: utf-8 -*-

n=int(input("הכנס מספר בין 3-20 לא כולל"))
if n<=3 and n>=20:
    print("error")
else: 
    print(n*("*"))
    print("*"+(n-2)*" "+"*")
    print("*"+(n-2)*" "+"*")
    print(n*("*"))
    
    