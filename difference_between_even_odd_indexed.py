'''
Write a program to find difference between sum of even indexed and odd indexed numbers in a list of numbers.
[Note:- Consider 0th index as even indexed]
# Sample Input
list1 = [2, 4, 3, 9, 13, 12, 7, 6, 1, 5]
# Expected Output
-10
'''
list1 = [2, 4, 3, 9, 13, 12, 7, 6, 1, 5]
x = slice(0,len(list1),2)
y = slice(1,len(list1),2)
even =[]
odd =[]
even.append(list1[x])
odd.append(list1[y])
