# Write a Python script to concatenate following dictionaries to create a new one.

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

d3={}
n=int(input("Third Dictionary Number Of Pairs:-"))
for i in range(n):
    key=input("Enter Number Of Key's:-")
    value=input("Enter Number Of Value:- ")
    d3[key]=value

print("~~ Dictionary 1:-",d1)   
print("~~ Dictionary 2:-",d2) 
print("~~ dictionary 3:-",d3)

final={}
for d in (d1,d2,d3):
    final.update(d)
print(final)
