# Write a Python program to replace last value of tuples in a list. 

data=[]
n=int(input("Enter number of data:"))
for i in range(n):
    x=input("Enter your value:")
    data.append(x)

print(tuple(data))
x=input("Enter your value:-")
data[-1]=x
print(data)
