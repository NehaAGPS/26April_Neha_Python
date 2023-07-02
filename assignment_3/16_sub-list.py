# Write a Python program to check whether a list contains a sub list.

l1=[]
l2=[]
n1=int(input("Enter number of element in list1:"))
n2=int(input("Enter number of element in list2:"))

for i in range(n1):
    print("Enter element in list1:")
    a=int(input())
    l1.append(a)

for j in range (n2):
    print("Enter element in list2:")
    b=int(input())
    l2.append(b)

if j in l1:
    print("list2 is same as list1")
else:
    print("list2 is not same list1")