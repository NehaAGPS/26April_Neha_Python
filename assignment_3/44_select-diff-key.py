"""Write a Python program to create and display all combinations of letters, 
selecting each letter from a different key in a dictionary. 
Sample data: {'1': ['a','b'], '2': ['c','d']} 
Expected Output: 
ac ad bc bd """

a={'1': ['a','b'], '2': ['c','d']}

list=list(a.values())

for i in list[0]:
    for j in list[1]:
        print(i+j)