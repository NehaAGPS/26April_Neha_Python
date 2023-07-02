# Write a Python script to check if a given key already exists in a dictionary. 

d1={}
n=int(input("Enter Number Of Pairs:-"))
for i in range(n):
    key=input("Enter Number Of Key's:-")
    value=input("Enter Number Of Value:- ")
    d1[key]=value
print(d1)
x=input("Enter Key:-")
if x in d1:
    print("Key Alredy Exist")
else:
    print("Key Is not Present")