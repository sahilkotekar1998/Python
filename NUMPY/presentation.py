
my_list = [1,2,2,3,4,4,4,5,6]

element_counts = {}

for element in my_list:
    if element in element_counts:
        element_counts[element]+= 1
    else:
        element_counts[element]= 1

for element, count in element_counts.items():
    print(f"{element}: {count} times")


# 3) accept 10 values and store them in the Series. Now perform following operations:

# a) display the entire Series
# b) extract 3rd element
# c) extract elements from 4 to 7
# d) extract elements from fourth last till the last element
# e) extract first 3 elements
# f) extract elements from the 5th position



import pandas as pd

values = []
for i in range(10):
    value = int(input(f"Enter value {i + 1}: "))
    values.append(value)

series = pd.Series(values)

print("a) Entire Series:")
print(series)

third_element = series[2]
print("\nb) 3rd Element:", third_element)

elements_4_to_7 = series[3:7]
print("\nc) Elements from 4 to 7:")
print(elements_4_to_7)

last_4_elements = series[-4:]
print("\nd) Elements from the fourth last till the last:")
print(last_4_elements)

first_3_elements = series[:3]
print("\ne) First 3 Elements:")
print(first_3_elements)

from_5th_position = series[4:]
print("\nf) Elements from the 5th position:")
print(from_5th_position)




# find the factorial






