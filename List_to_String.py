'''
Write a program to convert a list of characters into a single string.
 Sample Input
['a', 'b', 'c', 'd']
 Expected Output
abcd
'''
a = ['a','b','c']
b =''.join(map(str,a))
print(b)
