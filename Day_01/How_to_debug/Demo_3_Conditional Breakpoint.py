#Given:

expense_list=[1230,2240,1500,1678,2020,1580,2240,1450,'1500',1245,2300]
total_expense=0

for expense in expense_list:
    total_expense+=expense

print("total expense is \t",total_expense)

"""when you run the above code, it will give you:

total_expense+=expense
TypeError: unsupported operand type(s) for +=: 'int' and 'str'

This happened because one of the values inside the list is "string"

now you need to find out exactly where in the list that string value appears.
one way is to debug the way you do it normally , i.e.

place the breakpoint at "total_expense+=expense" statement 
and debug

on click of "step over" when values reaches to '1500' you can see exception. But for that you have to continuously click on "step over" option.

now say you have thousands of values in the list and you want to find out where exactly that first string appears because of which you get the exception and the worst part of it is that string value if it is available at the end of the list. Are you going to click on "step over" so many times?

certainly no. you don't want to waste time. 
for that you will go for "conditional breakpoint"

right click on the left of "total_expense+=expense" 
	select "conditional breakpoint"
in the expression window type following condition:
	type(expense)==str


click on "run and debug" option from the left window.
click on "run and debug" button and what you will observe is , you can see the exception right away with the value '1500'. This saves your time. You don't have to click on "step over" continuously and waste your time.

"""