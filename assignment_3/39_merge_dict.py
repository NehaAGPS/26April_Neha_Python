# Write a Python script to merge two Python dictionaries.

d1={}
n=int(input("Frist Dictionary Number Of Pairs:-"))
for i in range(n):
    key=input("Enter Number Of Key's:-")
    value=input("Enter Number Of Value:- ")
    d1[key]=value

d2={}
n=int(input("Second Dictionary Number Of Pairs:-"))
for i in range(n):
    key=input("Enter Number Of Key's:-")
    value=input("Enter Number Of Value:- ")
    d2[key]=value

x=d1.update(d2)
print(d1)