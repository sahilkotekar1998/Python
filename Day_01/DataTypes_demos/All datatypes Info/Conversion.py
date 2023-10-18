"""num1=5.6
print(num1)
print(type(num1))
print(int(5.6))
print(num1)

num2='123'
print(num2)
print(type(num2))

num3=int(num2)
print(num3)
print(type(num3))

num3=int(num2)
print("===========")
print(type(num3))

num111=int(num1)
print("#####################")
print(type(num111))


num4=25
print(num4)
print(type(num4))
num5=float(num4)
print(num5)
print(type(num5))

#  num6="123"+10        #   TypeError: can only concatenate str (not "int") to str
num6=int("123")+10
print(num6)
print(type(num6))

num7="123"+str(10)
print(num7)
print(type(num7))

num8=True
print(num8)
print(type(num8))

num9=int(num8)
print(num9)
print(type(num9))

num10=False
print(num10)
print(type(num10))

num11=float(num10)
print(num11)
print(type(num11))

"""
"""
complex() function
	is used to convert number or string to complex number.

complex() takes two argument
	real
	imaginary

both these arguments are optional, by default value is 0.

these arguments can be int or float or string

But string should have a valid number.
"""




num12=3.4
num13=complex(num12)
print(num13)
print(type(num13))                #OUTPUT - 3.4+0j

num14=5+4j
# num15=int(num14)      #  TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
num15=str(num14)
print(num15)
print(type(num15))

#  num16="458m"         # ValueError: complex() arg is a malformed string
# num16="j349"          # ValueError: complex() arg is a malformed string
num16="349j"            # not a problem
#num16="458"             # not a problem
num17=complex(num16)      
print(num17)
print(type(num17))

num18=True
num19=complex(num18)
print(num19)
print(type(num19))

num20=6+3.4j
num21=bool(num20)
print(num21)
print(type(num21))

num22=0+8j
num23=bool(num22)
print(num23)
print(type(num23))

# num24=4+0j    # True
num24=0+0j
num25=bool(num24)
print(num25)
print(type(num25))


print("-----------------------------------------")

num28=3.14
num29=complex(num28)
print(type(num29))
print(num29)

num30=3.23+0j
print(type(num30))
num31 = str(num30)
print(type(num31))

print("===========")

num32=7.77+0j
num33=bool(num32)
print(type(num33))
print(type(num33))

