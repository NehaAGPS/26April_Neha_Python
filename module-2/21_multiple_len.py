# Write a Python function to reverses a string if its length is a multiple of 4.

a=input("Enter String : ")

if (len(a)%4==0):
    print(a[::-1])
else:
    print(a)
