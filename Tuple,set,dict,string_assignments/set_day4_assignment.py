#1) accept 10 values from user and add them inside the set. now accept one more value from user and if it is present in the set, 
#remove it. Make sure program doesn't give any error if number is not there inside the set.


myset=set()
for i in range(1,11):
    num=int(input("enter a number"))
    myset.add(num)
print(myset)
user=int(input("enter number"))
myset.discard(user)
print(myset)
    

    



