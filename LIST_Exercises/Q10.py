#10. Write a Python program to find the list of words that are longer than n from a given list of words.

# Function to find words longer than n
def find_words_longer_than_n(word_list, n):
    result = []
    for word in word_list:
        if len(word) > n:
            result.append(word)
    return result

# Sample list of words
word_list = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']

# Specify the length 'n'
n = 5

# Call the function to find words longer than 'n'
longer_words = find_words_longer_than_n(word_list, n)

# Print the result
print(f"Words longer than {n} characters: {longer_words}")



def find(words_long,n):
    result=[]
    for word in words_long:
        if len(word)>n:
            result.append(word)
    return result
n=5
list=["apple","mango","banana"]
a=find(list,n)
print(n,a)
