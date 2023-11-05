import copy

mylist=[1,2,3,4,5,6]
print(mylist.append(777))           #append()
print(mylist)


#you can append dict in list

mylist=[{"name":"sahil","age":25},
        {"name":"gaurav","age":22}]

mydict={"name":"bhavik","age":26}

mylist.append(mydict)
print(mylist)




mylist=[1,2,2,2,3,4,5,6,5,5,5,6,1,2]  #count()
print(mylist.count(2))


mylist=[1,2,3,4,[5,6,7,8]]
mylist1 = copy.copy(mylist)     #copy
print(mylist1)


print("mylist_id",id(mylist))
print("mylist1_id",id(mylist1))


mylist=[1,2,3,4,5,8]
mylist1=copy.deepcopy(mylist)      #deepcopy
print(mylist1)

print("mylist_id",id(mylist))
print("my_list1_id",id(mylist1))


mylist=[1,2,3,4,5,6]
mylist.clear()                    #clear()
print(mylist)


l=[1,2,3]
l.extend([4,5,6])                #extend()- you can add tuple set in a list
print(l)


mylist=[1,2,3,4,5,6]
mylist1=[777,899,(222,333)]
mytuple=(444,555)

mylist.extend(mylist1)
mylist.extend(mytuple)

print(mylist)


# list of items 
list2 = ['cat', 'bat', 'mat', 'cat', 'pet'] 
# Will print the index of 'bat' in list2           #index()
print(list2.index('bat')) 
#1


# list of items 
list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5,8,4] 
# Will print index of '4' in sublist 
# having index from 4 to 8. 
print(list1.index(4, 4, 8)) 




# list of items 
list1 = [5, 8, 5, 6, 1, 2] 

# Will print index of '6' in sublist 
# having index from 1 to end of the list. 
print(list1.index(6, 2)) 
#the first argument is treated as the element to be searched and the second argument is the index from where the searching begins. 



list = ['Sun', 'rises', 'in', 'the', 'east'] 
list.insert(2, "The") 
print(list)

list=[1,2,3,4,5]                                #insert()
list.insert(0,777)
print(list)


list1 = [ 1, 2, 3, 4, 5, 6 ] 

# tuple of numbers 
num_tuple = (4, 5, 6) 
# inserting a tuple to the list  
list1.insert(2, num_tuple) 
print(list1)


list1 = [1, 2, 3, 4, 5, 6]
print(list1.pop(3),list1)                  #pop()
print(list1)


list1 = [1, 2, 3, 4, 5, 6]
print(list1.pop(-3),list1)                  #pop()
print(list1)

list_1=[1,2,3,4]
list_1.pop()
print(list_1)




lis = ['a', 'b', 'c']
lis.remove("b")
print(lis)


# the first occurrence of 1 is removed from the list 
list1 = [ 1, 2, 1, 1, 4, 5 ] 
list1.remove(4)                              #remove()
print(list1) 

# removes 'a' from list2 
list2 = [ 'a', 'b', 'c', 'd' ] 
list2.remove('a') 
print(list2)



list=[1,2,3,4,5]
rev=list[::-1]
print("rev:",rev)                      #reverse()




# Python3 program to demonstrate the 
# use of reverse method 

# a list of numbers

list1 = [1, 2, 3, 4, 1, 2, 6] 
list1.reverse() 
print(list1) 

# a list of characters
list2 = ['a', 'b', 'c', 'd', 'z'] 
list2.reverse() 
print(list2)






numbers = [1, 3, 4, 2] 

# Sorting list of Integers in ascending        #sort()
print(numbers.sort()) 
print(numbers)			


# sorting numbers in descending Order 
# Creating List of Numbers 
numbers = [1, 3, 4, 2] 
numbers.sort(reverse=True) 
print(numbers) 


def sortSecond(val): 
	return val[1] 

list1 = [(1, 2), (3, 3), (1, 1)] 

list1.sort(key=sortSecond) 
print(list1) 

list1.sort(key=sortSecond, reverse=True) 
print(list1) 


print(min([1,2,3]))                 #min()

# minimum item in list 
print(min([1, 2, 3])) 

# minimum item in dict 
print(min({'a': 1, 'b': 2, 'c': 3})) 

# minimum item in tuple 
print(min((7, 9, 11)))






var1 = 4
var2 = 8                                       #max()
var3 = 2

max_val = max(var1, var2, var3)
print(max_val)


var1 = "geeks"
var2 = "for"
var3 = "geek"

max_val = max(var1, var2, var3)
print(max_val)





#find min number from list without using min()
my_list = [10, 5, 7, 3, 12, 1, 8]

minimum_number = my_list[0]

for num in my_list:
    if num < minimum_number:
        minimum_number = num

print("The minimum number in the list is:", minimum_number)






