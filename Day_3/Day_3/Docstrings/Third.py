# creating and accessing multiline docstring


def myfun():
    """ 
    this is myfun 
    it prints hello message
    it is a special function
    """
    print("Hello")

myfun()
print(myfun.__doc__)

print("-------------------------")


def fun():
    """
    hi this is sahil
    """
    print("hello")
fun()
print(fun.__doc__)

help(int)
print(int.__doc__)