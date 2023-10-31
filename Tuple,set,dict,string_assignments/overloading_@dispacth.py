# @dispatch is used for overloading, when the method name is same but python calls method by arguments

# from multipliedispatch import dispatch


@dispatch(int,float,str)
def val(num1,num2,num3):
    print(num1,num2,num3)

@dispatch(float,str,int)
def val(num1,num,num3):
    print(num1,num,num3)

val(12,12.2,"sahil")
val(3.4,"gaurav",18)

val("aefcds",34,43.3)


