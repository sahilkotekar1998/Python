#2. Write a Python program to multiplies all the items in a list

mylist=[1,2,3,4,5]

result=1
for i in range(len(mylist)):
    result*=mylist[i]
print(result)