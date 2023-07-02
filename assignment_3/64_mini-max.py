# Write a Python program to find the maximum and minimum numbers 
# from the specified decimal numbers. 

from decimal import*
data=list(map(Decimal,'2.45 2.69 2.45 3.45 2.00 0.03 8.25'.split()))
print("Maximum : ",max(data))
print("Minimum : ",min(data))