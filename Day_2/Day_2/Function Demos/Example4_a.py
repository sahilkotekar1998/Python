# global and local variable
var=500

def disp():
    print("value of var is\t",var)

def myfun():
    var=100
    print("value of var is\t",var)
    disp()
myfun()



#global var is defined outside of function, and can be accessed by all the functions, eg var=500
#local variable gets more precedence over global variable



