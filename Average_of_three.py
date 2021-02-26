'''
Write a program to calculate the average of three numbers.
'''
number1=int(input("Enter number1:"))
number2=int(input("Enter number2:"))
number3=int(input("Enter number3:"))
total=int(number1+number2+number3)
avg=total/3
print(avg)
# -----------------------------------------------------------------------------------

number1,number2,number3=int(input("Enter number1:")),int(input("Enter numnber2:")),int(input("Enter number3:"))
total=number1+number2+number3
avg=total/3
print(avg,type(avg))