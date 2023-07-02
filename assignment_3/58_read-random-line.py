# Write a Python program to read a random line from a file.

fl=open('file.txt','r+')
d=[]
n=int(input("Enter Number List Data:-"))
for i in range(n):
    x=input("Enter Your data:-")
    d.append(x)
fl.write(str(d))

import random
y='y'
while y!='n':
    fl=open('file.txt','r+')
    t=fl.read()
    w=list(map(str,t.split(',')))
    print(random.choice(w))
    y=input("Refresh 'y' for 'yes' or 'n' for 'no' :-")
