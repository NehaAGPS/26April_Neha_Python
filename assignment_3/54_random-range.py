# How can you pick a random item from a range? 

"""We can Use the random.randrange() function(Returns a random number within the 
specified range)to generate a random number within the given range by passing minimum,
and maximum numbers as arguments

"""
import random
d=[]

n=int(input("Enter Number Of List Data:-"))
for i in range(n):
    t=input("Enter List Data:-")
    d.append(t)
print("This Is List Of Data")
print(d)
x=random.choice(d)
print(x)

y="y"
while y!="n":
    t=random.randrange(11111,99999,120)
    print(t)
    y=input("Do you wan't to countinue 'y' for 'yes' 'n' for 'no' :-")
    
    
    