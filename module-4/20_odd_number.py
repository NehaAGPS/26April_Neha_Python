#Write python program that user to enter only odd numbers, 
#else will raise an exception. 

try:
    num=int(input("Enter number:"))
    if num%2==0:
        raise Exception
    else:
        print(num)
except:
    print("Error...")