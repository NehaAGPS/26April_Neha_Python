# Write a Python program to add 'ing' at the end of a given string (length 
# should be at least 3). If the given string already ends with 'ing' then add 
# 'ly' instead if the string length of the given string is less than 3, leave it unchanged.

def name(str):
  length=len(str)

  if length > 2:
    if str[-3:]=='ing':
      str+='ing'
    else:
      str+='ly'

  return str    
print(name('ab'))
print(name('abc'))
print(name('quick'))
