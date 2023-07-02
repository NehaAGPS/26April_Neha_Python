# Write a Python program to find the repeated items of a tuple.

data=[]
n=int(input("Enter number of data:"))
for i in range(n):
    x=input("Enter your value:")
    data.append(x)
c=data.count("neha")
print(c)
print(tuple(data))
