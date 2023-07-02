#Write a Python program to get unique values from a list 

list=[]
n=int(input("Enter number of element in list:"))
for i in range(n):
    el=input("Enter element:")
    list.append(el)
print(list)
data=[]
for el in list:
    if el not in data:
     data.append(el)
print(data)