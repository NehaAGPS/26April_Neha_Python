# How will you randomizes the items of a list in place? 

import random
d=[]

n=int(input("Enter Number Of List Data:-"))
for i in range(n):
    t=input("Enter List Data:-")
    d.append(t)
print("This Is List Of Data")
print(d)

random.shuffle(d)
print(d)
