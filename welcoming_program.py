'''
Write a program that prompts the user for his or her name and print the welcome message
with user's input on the screen (console or shell).
# Sample Input
Charlie
# Expected Output
Welcome Charle
'''
def greeting(name):
    print(f"Welcome {name}")
data=input("Enter name:")
greeting(data)