"""
In Python, to write an empty class pass statement is used.
 pass is a special statement in Python that does nothing.
It only works as a dummy statement.
However, objects of an empty class can also be created.
"""

class MyClass:
    pass


m1=MyClass()
m2=MyClass()
print(m1 is m2)    #checks whether m1 and m2 refersto same object or not
print(m1 is not m2)

m2=m1
print(m1 is m2)
print(m1 is not m2)
