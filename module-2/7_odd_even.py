# Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user

a=int(input("Enter Nmuber :"))
if a in range(1,11,2):
    print("it is odd number.")
elif a in range(2,11,2):
    print("it is even number.")
else:
    print("sorry went wrong...!")


