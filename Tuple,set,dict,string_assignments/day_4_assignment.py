#1) Write a Python program to count the elements in a list until an element is a tuple.

#Sample input : list = [10, 20, 30, (40,50), 60]
#Sample output = 3



#isinstanceReturn whether an object is an instance of a class or of a subclass thereof.

my_list = [10, 20, 30, (40,50), 60]
count=0
for element in my_list:
    if isinstance(element,tuple):
        break
    else:
        count+=1
print(count)



#2) create a tuple to store 5 numbers and then sort it in ascending and descending order.

my_tuple=(3,5,6,4,9)
new_tuple=sorted(my_tuple)
print(new_tuple)

# new1_tuple=sorted(my_tuple,reverse=True)
# print(new1_tuple)



#3) Write a Python program to find the repeated items of a tuple.


my_tuple = (1, 2, 2, 3, 4, 4, 4, 5, 6)

counts = {}

for item in my_tuple:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

repeated_items = {item: count for item, count in counts.items() if count > 1}

print("Repeated Items:")
for item, count in repeated_items.items():
    print(f"{item}: {count} times")



    
    