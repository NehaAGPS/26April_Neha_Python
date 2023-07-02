#Write a Python program to check a list is empty or not.

list=[]
n=int(input("Enter number of element in list:"))

for i in range(n):
    el=int(input("Enter element:"))
    list.append(el)
if len(list)==0:
    print("Empty list")
else:
    print(list)