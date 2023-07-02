# Write a Python function to calculate the factorial of a number
# (a nonnegative integer)

a=int(input("Enter Number:"))
f=1
b=1
while b<=a:
    f=f*a
    b=b+1
print("the factorial of",a,"is",f)