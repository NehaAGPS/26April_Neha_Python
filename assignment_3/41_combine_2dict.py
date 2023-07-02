# Write a Python program to combine two dictionary adding values 
# for common keys. 
# d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400} 
# Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}). 

"""from typing import Counter

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200,'d':400} 

d3=Counter(d1)+Counter(d2)
print(d3)
"""

d1={}
key=['a','b','c']
for i in range(len(key)):
    value=int(input(f"Enter Number(100,200,300) for {key[i]}:-"))
    d1[key[i]] = value
print("~~~~~~~~~~~~~~~~~~~~~")
d2={}
key=['a','b','d']
for i in range(len(key)):
    value=int(input(f"Enter Number(300,200,400) for {key[i]}:-"))
    d2[key[i]]=value

print(d1)
print(d2)
print("~~~~~~~~~~~~~~~~~~~~~")
for i in d1.keys():
    if i in d2.keys():
        d1[i]=d1[i]+d2[i]
    d2[i]=d1[i]
print(d2)
