#Write a Python program to count the number of strings where the string length is 2 or more and the first and last 
#character are same from a given list of strings. 
#Sample List : ['abc', 'xyz', 'aba', '1221']
#Expected Result : 2



# Sample list of strings
string_list = ['abc', 'xyz', 'aba', '1221']

# Initialize a counter for matching strings
count = 0

# Iterate through the list and count matching strings
for string in string_list:
    if len(string) >= 2 and string[0] == string[-1]:
        count += 1

# Print the count of matching strings
print("Number of strings with length >= 2 and the same first and last character:", count)
