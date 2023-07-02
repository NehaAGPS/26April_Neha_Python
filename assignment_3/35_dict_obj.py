# How Do You Traverse Through A Dictionary Object In Python?

d1={}
n=int(input("Enter Number Of Pairs:-"))
for i in range(n):
    key=input("Enter Number Of Key's:-")
    value=input("Enter Number Of Value:- ")
    d1[key]=value
print(d1)
for i in d1:
    print(i,"~~~>",d1[i])
    