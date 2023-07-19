# Write a Python program to append text to a file and display the text.

from fileinput import close


x=open("neha.txt",'a')
x.write("\nI am a student.")
x.close()

y=open("neha.txt",'r')
print(y.read())