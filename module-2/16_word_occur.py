# Write a Python program to count the occurrences of each word in a given sentence.

a=input("enter string:")
b=input("enter word:")
#x=[]
count=0
x=a.split(" ")
for i in range(0,len(x)):
    if(b==x[i]):
        count+=1
print("count of word is:")
print(count)



    