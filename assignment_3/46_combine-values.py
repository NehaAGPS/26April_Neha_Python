"""Write a Python program to combine values in python list of dictionaries. 
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 
300}, o {'item': 'item1', 'amount': 750}] 
Expected 
Output: Counter ({'item1': 1150, 'item2': 300})"""

from collections import Counter
a= [ {'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 
    300},{'item': 'item1', 'amount': 750}]

r = Counter()
for i in a:
    r[i['item']] += i['amount']
print(r)