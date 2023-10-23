"""
1) define 3 functions "add()","modify()" and "delete()" with just a print message.
now accept input from user as a number. if the number entered is 1, call "add()"
if it is 2, call "modify()" if it is 3, call "delete()" [ hint: use "match... case" ]
"""

def add():
    print("add")
def modify():
    print("modify")
def delete():
    print("delete")

user_input=int(input("enter a number"))

match user_input:
    case 1:
        add()
    case 2:
        modify()
    case 3:
        delete()
    case _:
        print("enter a valid number")

#define a function which accepts a number and return its square.

user_in=int(input("enter a number"))
def square_number(num):
    return num*num

result = square_number(user_in)
print(f"the square of number is {result}")
