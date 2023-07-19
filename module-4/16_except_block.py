#Can one block of except statements handle multiple exception?

#Ans:

#You can also have one except block handle multiple exceptions.

a=0
b=0
try:
    print(a/b)
except:
    print('Error..')
    print("can't divide by 0")