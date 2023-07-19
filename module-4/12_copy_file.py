#Write a Python program to copy the contents of a file to another file.

x=open("Q4.txt",'r')
y=open("Q-12.txt",'w')

for i in x:
   y.write(i)
