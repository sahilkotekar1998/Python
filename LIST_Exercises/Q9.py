#9. Write a Python program to clone or copy a list. 
'''
Shallow copy- It references the nested objects inside the new object. 
This means that changes made to nested objects in the original structure will affect the copied structure and vice versa

Deep copy - Changes made to the original object or its nested objects do not affect the deep copy, and vice versa.
'''



import copy

my_list=[1,2,3,4]
copy_my_list=copy.copy(my_list)
print(copy_my_list)

print(id(my_list))
print(id(copy_my_list))



mylist=[1,2,3,4]

copy_mylist=copy.copy(mylist)
print(copy_mylist)

print(id(copy_mylist))
print(id(mylist))
