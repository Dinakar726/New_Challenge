'''
Write a Python program to sum all the items in a list.
# Sample Input
list1 = [1, 2, -8]
# Expected Output
-5
'''
list1 = [1, 2, -8]
print(sum(list1))
# we can use simple inbuilt function "sum" or
# by writing small function with oe argument and by calling that function also we can get the output

def add(items):
    total=0
    for i in items:
        total=total+i
    return total
print(add(list1))