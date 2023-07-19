#How Do You Handle Exceptions With Try/Except/Finally In Python?
#Explain with coding snippets. 

#Ans:

#Python exception handling is achieved by three keyword blocks – try, except, and finally.
#The try block contains the code that may raise exceptions or errors.
#The except block is used to catch the exceptions and handle them.
#The finally block code is always executed, whether the program executed properly or it raised an exception.

a=10
b=0
try:
    print(a/b)
except:
    print("Error..")

finally:
    print(a+b)