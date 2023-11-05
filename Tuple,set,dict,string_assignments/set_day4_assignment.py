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
    


# myset=set()
# for i in range(1,11):
#     num=int(input("enter a number"))
#     myset.add(num)

# print(myset)

# user=int(input("enter a number"))
# myset.discard(user)
# print(myset)


##2 "set()" function to convert a list with duplicate values into set

# list=[1,2,2,1,2,4,5,6,7]
# print(list)

# myset=set(list)
# print(myset)


##3 "set()" function to convert a list with duplicate values into set

# list=[1,2,3,4,4,5]
# print(list)

# myset=set(list)
# print(list)

# myset.add(12)
# myset.add(2)  #it wont add this as it is already present
# print(myset)


##4 "update()" function to add two or more elements into set

# myset={1,2,3,4,5}
# print(myset)

# myset.add((777,777))
# print(myset)


# s={2,3,4,5}
# print(type(s))


# s=set()
# print(type(s))


s1={1,2,3,4,5}
s2={3,6,7}

print(s1.union(s2))

s1.update(s2)
print(s1)


s1.intersection(s2)
print(s1)


cities={"tokyo","madrid"}
cities2={"tokyo","madrid"}

print(cities.isdisjoint(cities2))





