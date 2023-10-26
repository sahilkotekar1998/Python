#12) print the following pattern:

# *
# * *
# * * *
# * * * *
# * * * * *

for i in range(1,6):
    for j in range(0,i):
        print("*",end=" ")
    print(" ")

num=int(input("enter number of rows"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()





