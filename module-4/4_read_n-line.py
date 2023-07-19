#Write a Python program to read first n lines of a file.

x=open("Q4.txt",'a')
x.write('''I am Neha.
I am from Amreli.
I'm study in tops tecnology- rajkot.''')
x.close()
x=open("Q4.txt",'r')
print(x.readlines()[:5])
