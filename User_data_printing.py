'''
Write a program to take name, roll number and branch as input from user and print it.
# Sample Input
name : abc
roll_no : 123
branch : xyz
# Expected Output
Hey, my name is abc and my roll number is 123. My branch is xyz.
'''
def user(*args):
    print(f"Hey, my name is {name} and my roll number is {rollnumber}. My branch is {branch}.")

name=input("Enter your name:")
rollnumber=int(input("Enter your rollnumber:"))
branch=input("Enter your branch:")
user(name,rollnumber,branch)
