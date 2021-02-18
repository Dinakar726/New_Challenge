# Write a program that uses list and range to create the list [3,6, 9, . . . , 99] .

a = []
for i in range(1,100):
    if i%3==0:
        a.append(i)
print(a)