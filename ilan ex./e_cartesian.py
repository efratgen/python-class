# Exercise 2.3. Write a function cartesian(A, B) that takes two lists and returns a list of all the pairs 
# (a,b) where a is an element of A and b is an element of B. For example, cartesian([0,1], [0,1,2]) 
# should return [(0,0), (1,0), (0,1), (1,1), (0,2), (1,2)]. Note: you may return the pairs in any order.

def e_cartesian (lst1,lst2):
    newlist=[]
    for i in lst2:
        for j in lst1:
            value= f"({j},{i})"
            newlist.append (value)

    return newlist        


print (e_cartesian([0,1],[0,1,2]))    


# change