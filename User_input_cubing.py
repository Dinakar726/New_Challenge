'''
Write a program to prompt the user for a number and print the cube of that number.
# Sample Input
3
# Expected Output
27
'''
def cube(data):
    result=data**3
    print(result)

number=int(input("Enter number:"))
cube(number)