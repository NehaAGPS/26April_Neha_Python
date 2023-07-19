#Write a Python program to write a list to a file.

x=open("Q4.txt",'a')

list=['My Father name is Gorakhbhai.','My Brother name is Maish.','My Mother name is Naynaben.']
x.write('\n')
for i in list:
    x.write(f'{i}\n')
