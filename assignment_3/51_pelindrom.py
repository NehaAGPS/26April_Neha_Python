# Write a Python function that checks whether a passed string is 
# palindrome or not.

def str():
    a=input("Enter String:-")
    b=a[-1::-1]
    if(a==b):
        print("Palindrom String")
    else:
        print("Not Palindrom String")

str()