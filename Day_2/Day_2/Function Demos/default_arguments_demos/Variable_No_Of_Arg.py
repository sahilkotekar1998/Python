 # variable number of arguments to a function

def disp(*vars):
	if(vars.__len__()==0):
		print("no argument passed")
	else:
		for k in vars:
			print(k)

def fun():
	disp()
	disp(10,20,30)
	disp("abc",200,True,3.4)
fun()


#variable number of argument is a function which can be called by passing zero or more values.