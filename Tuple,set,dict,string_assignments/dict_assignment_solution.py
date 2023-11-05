# 1) Write a Python program to create a dictionary of keys x, y, and z 
# where each key has as value a list from 11-20, 21-30, and 31-40 respectively. 
# Access the fifth value of each key from the dictionary. 
# {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# 15
# 25
# 35


mydict={"x":[11, 12, 13, 14, 15, 16, 17, 18, 19],
        "y":[21, 22, 23, 24, 25, 26, 27, 28, 29],
        "z":[31, 32, 33, 34, 35, 36, 37, 38, 39]}

print(mydict["x"][4])
print(mydict["y"][4])
print(mydict["z"][4])



# 2) Write a Python script to add a key to a dictionary. 
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}



mydict={0:10,1:20}
new_dict={2:30}

mydict.update(new_dict)
print(mydict)




# 3) Write a Python script to check whether a given key already exists in a dictionary. 

given=2
mydict={0:10,1:20}
for key in mydict.keys():
    if given in mydict.keys():
        print("present")
    else:
        print("not")

        


# 4) Write a Python program to count the values associated with key in a dictionary. 
# Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
# Expected result: Count of how many dictionaries have success as True




data = [{'id': 1, 'success': True, 'name': 'Lary'},
        {'id': 2, 'success': False, 'name': 'Rabi'},
        {'id': 3, 'success': True, 'name': 'Alex'}]


count=0
for item in data:
    if "success" in item and item['success']==True:
        count+=1
print(count)


# 5) Write a Python program to create a dictionary from two lists without losing duplicate values. 
# Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
# Expected Output: {'Class-VII': {2}, 'Class-VI': {2}, 'Class-VIII': {3}, 'Class-V': {1}}) 

keys = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
values = [1, 2, 2, 3]

# Initialize an empty dictionary
result_dict = {}

# Iterate through both lists simultaneously
for key, value in zip(keys, values):
    # Check if the key already exists in the dictionary
    if key in result_dict:
        # If it exists, append the value to the existing set
        result_dict[key].add(value)
    else:
        # If it doesn't exist, create a new set with the value
        result_dict[key] = {value}

# Convert sets to single values if they have only one element
for key, value in result_dict.items():
    if len(value) == 1:
        result_dict[key] = value.pop()

# Print the resulting dictionary
print(result_dict)




# 6 Write a Python program to check a dictionary is empty or not.

mydict={1:1}
if len(mydict)==0:
    print("empty")
else:
    print("not empty")



# 7) Write a Python program to combine two dictionary adding values for common keys. 
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300}) 

from collections import Counter

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Initialize a Counter object with the first dictionary
result = Counter(d1)

# Update the Counter object with the second dictionary
result.update(d2)

# Print the combined result
print(result)


# 8) Write a Python program to count number of items in a dictionary value that is a list
# sample data:
# mydictionary1={'Names':['Rohit','Ganesh','SRK','Akshay'],'age':40,'addresses':['Mumbai','Delhi','Kolkara','Banglore'],'emails':['actor.gmail.com','movie.gmail.com']}

# output: 10

mydictionary1 = {
    'Names': ['Rohit', 'Ganesh', 'SRK', 'Akshay'],
    'age': 40,
    'addresses': ['Mumbai', 'Delhi', 'Kolkata', 'Bangalore'],
    'emails': ['actor@gmail.com', 'movie@gmail.com']
}

# Initialize a counter
count = 0

# Iterate through the dictionary values
for value in mydictionary1.values():
    # Check if the value is a list
    if isinstance(value, list):
        # Add the count of items in the list to the total count
        count += len(value)

# Print the total count
print(count)

# 9) Write a Python program to create a dictionary from a string. 
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}


sample_string = 'w3resource'

# Initialize an empty dictionary to store letter counts
letter_count = {}

# Iterate through the characters in the string
for char in sample_string:
    # Check if the character is a letter
    if char.isalpha():
        # Update the letter count in the dictionary
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

# Print the letter count dictionary
print(letter_count)


sample_string="sahilkotekar1944"

mydict={}

for char in sample_string:
    if char.isalpha():
        if char in mydict:
            mydict[char]+=1
        else:
            mydict[char]=1

print(mydict)


# 10) Write a Python program to get the key, value and item in a dictionary



my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

total_items = 0

# Print the table header
print("Key\tValue")
print("----------------------------")

# Iterate through the dictionary to get keys and values
for key, value in my_dict.items():
    total_items += 1
    print(f"{key}\t{value}")

# Print the total items
print(f"\nTotal items are {total_items}")



# 11) Write a Python program to get the maximum and minimum value in a dictionary.

mydict={1:12,2:90,3:56,4:34}
print(mydict)

max_value=max((mydict))
print(max_value)



# 12) Write a Python program to map two lists into a dictionary.




keys=[1,2,3,4,5]
values=["a","b","c","d","e"]

resultdict=dict(zip(keys,values))
print(resultdict)


# 13) Write a Python program to match key values in two dictionaries. 
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y


dict1 = {'key1': 1, 'key2': 3, 'key3': 2}
dict2 = {'key1': 1, 'key2': 2}

common_pairs = {key: value for key, value in dict1.items() if key in dict2 and dict2[key] == value}

for key, value in common_pairs.items():
    print(f"{key}: {value} is present in both dictionaries")



# 14) # Write a Python program to print a dictionary line by line. 

data = {
    'Rohit': {'runs': 10000, 'centuries': 15},
    'Virat': {'runs': 12000, 'centuries': 18}
}

for name,centuries in data.items():
    print(name)
    for key,value in centuries.items():
        print(key,":",value)




# 15) Write a Python program to remove a key from a dictionary.

mydict={'a': 1, 'b': 2, 'c': 3}

if "b" in mydict:
    mydict.pop("b")
print(mydict)




# 16) Write a Python program to remove spaces from dictionary keys. 

# Students={'d 01':'Abc','d 0 2':'Xyz','d0 3':'Pqr'}

# output:

# {'d01': 'Abc', 'd02': 'Xyz', 'd03': 'Pqr'}



Students = {'d 01': 'Abc', 'd 0 2': 'Xyz', 'd0 3': 'Pqr'}

new_dict = {key.replace(' ', ''): value for key, value in Students.items()}

print(new_dict)


# 17) Write a Python program to sum all the items in a dictionary.



mydict={"A":1, "b":2,"c":3,"d":4}
total_sum= sum(mydict.values())
print(total_sum)




# 18) Write a Python script to merge two Python dictionaries. 

# mydictionary1={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
# mydictionary2={7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144}

# output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144}

mydictionary1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
mydictionary2 = {7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144}

mydictionary1.update(mydictionary2)

print(mydictionary1)


mydictionary1.update(mydictionary2)
print(mydictionary1)


# 19) Write a Python script to concatenate following dictionaries to create a new one. 
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

merged_dict={}
merged_dict.update(dic1)
merged_dict.update(dic2)
merged_dict.update(dic3)

print(merged_dict)

