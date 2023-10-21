"""
1) define 3 functions "add()","modify()" and "delete()" with just a print message.
now accept input from user as a number. if the number entered is 1, call "add()"
if it is 2, call "modify()" if it is 3, call "delete()" [ hint: use "match... case" ]

"""
def add():
    print("This is add function")

def modify():
    print("this is modify function")

def delete():
    print("this is delete function")

user_input=int(input("enter number 1:add, 2:modify, 3:delete"))

match user_input:
    case 1:
        add()
    case 2:
        modify()
    case 3:
        delete()
    case _:
        print("enter a valid number")


"""

2) define a function which accepts a number and return its square.

"""
def square_number(number):
    return number * number


input_number = float(input("Enter a number: "))  
result = square_number(input_number)
print(f"The square of {input_number} is {result}")




"""
3)define a function which accepts character,int,string and display them.
"""

def display_data(char, integer, string):
    print(f"Character: {char}")
    print(f"Integer: {integer}")
    print(f"String: {string}")

char_input = input("Enter a character (a single letter or symbol): ")
integer_input = int(input("Enter an integer: "))
string_input = input("Enter a string: ")

display_data(char_input, integer_input, string_input)


"""
4) define "myfun1()" with a print statement. now define "myfun2()" which should invoke "myfun1()" function. 
invoke myfun2()
"""

def myfun1():
    print("inside myfun1")

def myfun2():
    print("inside myfun2")
    myfun1()
myfun2()



#5)define a function to accept a number. This function should return 1 if a number passed is more than 0
#return -1 if a number passed is less than 0 , else it should return 0.

def check_number(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0

input_number = float(input("Enter a number: "))
result = check_number(input_number)
print(f"Result: {result}")



#Q6)define a function which accepts a character and return toggle of it.
def toggle_case(char):
    return char.swapcase()


input_char = input("Enter a character: ")


if len(input_char) == 1:
    toggled_char = toggle_case(input_char)
    print(f"The toggled character is: {toggled_char}")
else:
    print("Please enter a single character.")


#Q7)define a function which accepts a string , toggle and return it.

def toggle_case_in_string(input_string):
    return input_string.swapcase()

# Example usage:
input_string = input("Enter a string: ")
toggled_string = toggle_case_in_string(input_string)
print(f"The toggled string is: {toggled_string}")


#Q8) write a function to accept minimum 3 characters and maximum 5 characters. 
 	#[ use default arguments method ]

def validate_string_length(input_string, min_length=3, max_length=5):
    if min_length <= len(input_string) <= max_length:
        return True
    else:
        return False


input_str = input("Enter a string (3 to 5 characters): ")

if validate_string_length(input_str):
    print("Valid input.")
else:
    print("Input doesn't meet the length criteria.")



#Q9)define a function in such a way that it can accept n number of values and print their sum. [ variable number of arguments]


def sum_values(*args):
    total = sum(args)
    return total

# Example usage:
result = sum_values(5, 10, 15, 20)
print(f"The sum is: {result}")
