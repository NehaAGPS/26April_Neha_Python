#Write a Python function that takes a list and returns a new list with unique 
#elements of the first list. 

data=list()
n=int(input("Enter number of value:"))

for i in range(n):
    x=int(input("Enter your data:"))
    data.append(x)

print(data)
num=[]
for a in data:
    if a not in num:
        num.append(a)
        print(num)
