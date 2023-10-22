# default arguments of the function

def disp(var1=10,var2=20):
	print(var1,"\t",var2)

def fun():
	disp()
	disp(30)
	disp(100,200)
fun()


#these are three ways of calling function

def sahil(age=25,rno=33):
	print(age,rno)

sahil()
sahil(26)
sahil(30,30)
