#Write a Python program to count the frequency of words in a file. 
from typing import Counter
x=open("Q4.txt",'r')

y=x.read().split()
print(Counter(y))
x.close()