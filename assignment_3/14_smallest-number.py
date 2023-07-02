# Write a Python program to find the second smallest number in a list. 

s=list()
a=int(input("Enter Number Of List:-"))
for i in range(a):
    x=int(input("Enter Number:-"))
    s.append(x)
print(s)
s.sort()
d=s[1]
print(d)
