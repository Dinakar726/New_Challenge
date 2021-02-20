list1 = [4,10,8,5,2,1,6,3,19,18,17,16,15,14,13,12,11,9,7]
list2=[]
j=0
while j>=0:
    j+=1
    if j==21:
        break
    list2.append(j)
    # print(list2)
def num(list):
    result=0
    for i in list:
        result=result+i
    return result

x = num(list1)
y = sum(list2)
print(x)
print(y)
z=y-x
print(z)