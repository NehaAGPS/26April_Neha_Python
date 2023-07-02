# How can you pick a random item from a list or tuple? 

import random
d=[]

n=int(input("Enter Number Of List Data:-"))
for i in range(n):
    t=input("Enter List Data:-")
    d.append(t)
print("This Is List Of Data")
print(d)
x=random.choice(d)
print(x)
print("~~~~~~~~~~~~~~~~~~~~~~")
print("This Is Tuple Of Data")
print(tuple(d))
f=random.choice(d)
print(f)