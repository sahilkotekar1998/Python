# Global Variable and Local variable
var=500  # global variable

print("Value of global var is\t",var)
def myfun():
    global var    #  try commenting this line
    var=300  # changing global variable
    print("var inside main\t",var) # by default local is given precedence
myfun()
print("Value of global var is\t",var)







#refering to global variable by using Global keyword, global var keyword use karke jo value assign karenge voh value save hogi.