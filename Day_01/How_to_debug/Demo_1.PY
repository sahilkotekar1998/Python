#Given the following code:

x=3
x+=2
x-=3
x*=5
x/=2
x%=3
print(x)

#it will print the final result, but if you want to notice what happens to the variable "x" every time you perform different operation on it.
#one way is to print x every time we perform the action, e.g.


x=3
x+=2
print(x)
x-=3
print(x)
x*=5
print(x)
x/=2
print(x)
x%=3
print(x)

#and then comment all those print statement (except the last one) when you are done.

#Another way is to debug. How will we do that?



x=3
x+=2
x-=3
x*=5
x/=2
x%=3
print(x)

"""place break points at :
x+=2
x-=3
x*=5
x/=2
	statements. In order to do that just click on the left of all these statements. you will see red dot once you click on the left of these statements. These red dots are nothing but breakpoints which will show you the value of x at that particular time.

on the left side of VScode window , you will get
	run and debug option

click that 

"run and debug" button will appear on the left side

click that

from "select a debug configuration"  window , select
	"Python file debug the currently active python file"

wait for some time, it'll start debugging

notice that execution has been paused at first breakpoint statement and on the left side notice the value of x i.e. 3 which has been initialized in the code.

now click on "step over" icon and notice what happens

you'll notice that execution has been paused at next breakpoint and on the left side now the value of "x" is changed.

continue clicking on "step over" and notice the value of "x" in the left side window.

once you are done debugging 
	a) click on "stop" icon
	b) click on "run and debug"

this will bring back the same window in which we normally work.
remove all the breakpoints by just clicking on them.

"""