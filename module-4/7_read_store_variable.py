#Write a Python program to read a file line by line store it into a variable. 

x=open("Q4.txt",'r')
count=0

for line in x:
    count+=1
    
    print(f"{count}:{line}")
