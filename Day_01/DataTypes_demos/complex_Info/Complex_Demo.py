num1= 5+3j
print(num1)
print(type(num1))

num2= 3.4 -5.6j
print(num2)
print(type(num2))




"""
num4= "hello"+4j
print(num4)
print(type(num4))
"""
# can only concatenate str (not "complex") to str

#  How to access "real" and "imaginary" part of the object
#IMPORTANT

num3 = 5+7.8j
print(num3)
print(type(num3))

print(num3)             # Complex number                           Output - (5+7.8j)
print(num3.real)        # real part of the complex number          Output - 5.0
print(num3.imag)        # imaginary part of the complex number     Output - 7.8

# How to generate complex number using "complex()" function

num5 = complex(4,5.6)   # Output - 4+5.6j
print(num5)
print(type(num5))    

num6=complex()     # What if we don't pass any number?   Output- 0j
print(num6)
print(type(num6))

num7=complex(5.6)  # what if we pass only one argument?  Output - 5.6+0j
print(num7)
print(type(num7))

num8=complex(0,5.6)  # what if we pass first argument as 0 ?  Output- 5.6j
print(num8)
print(type(num8))



num9=complex("123")
print(num9)
print(type(num9))

# num10=complex("A123")    ValueError: complex() arg is a malformed string   


# num10=complex("23"+8)      # TypeError: can only concatenate str (not "int") to str

# num10=complex(5,"34")     # TypeError: complex() second arg can't be a string

# num10=complex("123","6.8")  # TypeError: complex() can't take second arg if first is a string



