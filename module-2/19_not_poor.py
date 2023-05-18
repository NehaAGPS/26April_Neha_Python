# Write a Python program to find the first appearance of the substring 
# 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the 
# whole 'not'...'poor' substring with 'good'. Return the resulting string.

a=input("Enter String:")
if len(a):
    x=(a.replace('not','good')+a.replace('poor','good'))
print(x)
