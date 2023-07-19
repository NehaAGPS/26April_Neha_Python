#Write a python program to find the longest words.

x=open("Q4.txt",'r')
y=x.read().split()
print(y)
max=len(max(y,key=len))
for i in y:
    if len(i)==max:
        print(i)
x.close()


