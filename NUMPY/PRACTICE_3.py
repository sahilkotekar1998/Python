from numpy import *

first=array([10,20,30,40])
# indexing from left to right

print(first[0],"\t",first[1],"\t",first[2],"\t",first[3])

# indexing from right to left

print("\n")
print(first[-1],"\t",first[-2],"\t",first[-3],"\t",first[-4])


sum = 0
for i in range(1, 6):
    sum += i
print("Sum of first 5 numbers is", sum)


var=500

def disp():
    print("value of var \t",var)

def myfun():
    var=100
    print("value of var is\t",var)
    disp()
myfun()