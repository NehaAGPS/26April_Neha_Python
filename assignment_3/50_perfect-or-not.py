# Write a Python function to check whether a number is perfect or not. 

def perfect(n):
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            print(i)
            sum=sum+i
    return sum

n =int(input("Enter a Number:-"))
s=perfect(n)
if n == s:
    print("Enter Number Is Perfect ...")
else:
    print("Enter Number Is not Perfect......")