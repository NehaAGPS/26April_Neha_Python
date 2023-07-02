# Write a Python program to find the highest 3 values in a dictionary.

mydict={}
n=int(input("Enter number of pairs:"))
for i in range(n):
    key=input("Enter your key's:")
    value=input("Enter your value's:")
    mydict[key]=value
print(mydict)
d=list(mydict.values())
d.sort()
d1=d[-3:]

for i in d1:
    for j in mydict.keys():
        if mydict[j]==i:
            print(f'{j}  :  {mydict[j]}')