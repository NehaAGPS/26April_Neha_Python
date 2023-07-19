#Write a Python program to count the number of lines in a text file. 

x=open("Q4.txt","r")
print(len(x.readlines()))
x.close()