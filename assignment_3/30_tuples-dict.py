# Write a Python program to convert a list of tuples into a dictionary.

def dic(data):
    return dict(data)

n=int(input("Enter Number Of Tuple:-"))
data=[]
for i in range(n):
    a=[]
    x=int(input("Enter Number Of Tuple Data:-"))
    for d in range(x):
        b=input("Enter Your Value:")
        a.append(b)
        s=tuple(a)
    data.append(s)
print(data)
print(dic(data))
