# Python program to count the number of characters (character frequency) in a string

a="my name is neha"
for i in a:
    frequency=a.count(i)
    print(str(i)+ ":" +str(frequency), end=",")
