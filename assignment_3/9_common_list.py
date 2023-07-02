# Write a Python function that takes two lists and returns true if they have 
# at least one common member. 

a=[]
b=[]
x=int(input("Enter number of element in a:"))
y=int(input("Enter number of element in b:"))
for i in range (x):
    for j in range(y) :
        m=int(input("Enter el1:"))
        a.append(m)
        print(a)
    n=int(input("Enter el2:"))
    b.append(n)
    print(b)
    if n in a:
        print("true")
    else:
        print("false")
