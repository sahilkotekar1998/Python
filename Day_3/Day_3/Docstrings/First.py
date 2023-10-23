# creating and accessing "docstring" for user defined functions

def square(num):
    ''' this function accepts a number and return its square '''
    return num*num

print(square(10))
print(square.__doc__)


def square(num):
    return num*num
user_input=int(input("enter a number"))
result=square(user_input)
print(f"the square is {result}")