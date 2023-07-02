# Write a Python program to map two lists into a dictionary.

data=list()
n=int(input("Enter Number Of Value:-"))
for i in range(n):
    s=int(input("Enter only digit:-"))
    data.append(s)

data1=[]
n=int(input("Enter Number OF list Data:-"))
for i in range(n):
    t=input("Enter Your Name:-")
    data1.append(t)

print(data)
print("~~~~~~~~~~~~~~~~~~~")
print(data1)
print("~~~~~~~~~~~~~~~~~~~")
dic=dict(zip(data,data1))
print(dic)