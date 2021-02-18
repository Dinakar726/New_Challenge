'''
Write a Python program to multiply all the items in a list.
# Sample Input
list1 = [1, 2, 3, 4]
# Expected Output
24
'''
list1 = [1, 2, 3, 4]
def mul(list):
    result=1
    for x in list:
        result=result*x
    return result
print(mul(list1))

