# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
# a,b=true / a+b=5 = true / a-b=5 = true 
a=int(input("Enter number :"))
b=int(input("Enter number :"))

if a==b or a-b==5 or a+b==5:
    print("True...")
else:
    print("False...!")
