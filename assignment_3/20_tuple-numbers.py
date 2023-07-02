# Write a Python program to create a tuple with numbers.

#number=(1,2,3,4,5,6,7,8,9)
#print(number)


data=[]
n=int(input("Enter number of data:"))
for i in range(n):
    x=int(input("Enter numbers:"))
    data.append(x)

print(tuple(data))