# Write a Python program to check whether an element exists within a tuple.

data=[]
n=int(input("Enter number of data:"))
for i in range(n):
    x=int(input("Enter numbers:"))
    data.append(x)
    print(tuple(data))
    if 5 in data:
        print("true")
    else:
        print("false")