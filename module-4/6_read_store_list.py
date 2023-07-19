#Write a Python program to read a file line by line and store it into a list?

x=open("Q4.txt",'r')
#print(x.readlines())
lines = [line.strip() for line in x]
print(lines)
