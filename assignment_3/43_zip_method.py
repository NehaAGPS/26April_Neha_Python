# Why Do You Use the Zip () Method in Python? 

l1=[1,2,3,4]
l2=[5,6,7,8]
final=list(zip(l1,l2))
print(final)

# the zip() function returns a zip object, 
# which is an iterator of lists where the first item in each
# passed iterator is paired together, and then the second item 
# in each passed iterator are paired together etc... 