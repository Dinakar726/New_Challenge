'''
Write a program that asks the user for a number of seconds and
prints out how many minutes and seconds that is. For instance, 200 seconds is 3 minutes and 20 seconds.
'''
total_seconds=int(input("Eneter total seconds:"))
if total_seconds>0:
    minute=total_seconds//60
    sec=total_seconds%60
print(f"{total_seconds} seconds is equal to {minute} minutes and {sec} seconds")