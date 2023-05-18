# Write a Python program to get the Fibonacci series of given range .

#a=10 
a=int(input("enter a number:"))
x,y=0,1
print("Fibonacci Series:",x,y,end=" ")
for i in range(2,a):
    z=x+y
    x=y
    y=z
    print(z,end=" ")
print()
