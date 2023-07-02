# Write a Python program to unzip a list of tuples into individual lists. 

n=int(input("enter number:"))
data=[]
for i in range(n):
    st=[]
    x=int(input("enter number of tuple:-"))
    for a in range(x):
        m=input("enter your value:")
        st.append(m)
        b=tuple(st)
    data.append(b)
print(data)
#print(list(zip(*data))) 

