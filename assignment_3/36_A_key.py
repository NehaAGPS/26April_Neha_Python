# How Do You Check The Presence Of A Key In A Dictionary? 

d1={}
n=int(input("Enter Number Of Pairs:-"))
for i in range(n):
    key=input("Enter Number Of Key's:-")
    value=input("Enter Number Of Value:- ")
    d1[key]=value
if 'sub' in d1.keys():
    print("Yes.....")
else:
    print("No.....")