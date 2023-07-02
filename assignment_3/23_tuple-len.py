# Write a Python program to find the length of a tuple.

data=[]
n=int(input("Enter number of data:"))
for i in range(n):
    x=int(input("Enter numbers:"))
    data.append(x)

print(tuple(data))
print(len(data))