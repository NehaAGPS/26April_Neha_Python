# Write a Python function to get the largest number, smallest num and sum of all from a list. 

a=[]
b=int(input("how many no. :"))

for i in range(b):
    x=int(input("Enter No. :"))
    a.append(x)
print("largest number is :",max(a))
print("smallest number is :",min(a))
print("sum is :",sum(a))