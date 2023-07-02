# Write a Python script to sort (ascending and descending) a dictionary by value. 

import operator
dic={}
n=int(input("Enter Number Of Pairs:-"))
for i in range(n):
    key=int(input("Enter Number Of Key's:-"))
    value=input("Enter Number Of Value:- ")
    dic[key]=value
print(dic)
d=sorted(dic.items(),key=operator.itemgetter(1))
print("Ascending:-",d)
d=dict(sorted(dic.items(),key=operator.itemgetter(1),reverse=True))
print("Descending:-",d)