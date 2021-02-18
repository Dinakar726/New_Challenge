'''
Write a Python program to find common items from two lists.
# Sample Input
color1 = ["Red", "Green", "Orange", "White"]
color2 = ["Black", "Green", "White", "Pink"]
# Expected Output
['Green', 'White']
'''

color1 = ["Red", "Green", "Orange", "White"]
color2 = ["Black", "Green", "White", "Pink"]
a= set(color1)
b= set(color2)
c= a.intersection(b)
print(list(c))