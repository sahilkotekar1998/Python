
#1) create a list , accept a number,name and a float value from user and store it inside the list.
#now accept one more name from user and insert it at 2nd position.
#accept a number and append it at the end of the list.
#print the entire list.


num=int(input("enter number"))
name=(input("enter name"))
fl=float(input("enter float number"))

list=[num,name,fl]
print(list)

num1=int(input("enter number"))
list.append(num1)

name1=(input("enter name"))
list[2]=name1
print(list)


#2) first create list empty. accept numbers till user enters 0 and store them inside the list. Print the list and its length.



list=[]
while True:
    num=int(input("enter number"))
    if num == 0:
        break
    else:
        list.append(num)
    print(list)





#3) accept 5 numbers, store them inside the list and display it. Now add 3 more numbers [hardcoded] at 
# the end of the list using "extend" method.

num1=int(input("enter a number"))
num2=int(input("enter a number"))
num3=int(input("enter a number"))
num4=int(input("enter a number"))
num5=int(input("enter a number"))

mylist=[num1,num2,num3,num4,num5]
print(mylist)
mylist.extend([1,2,3])
print(mylist)


#4) accept a number,string,decimal,boolean value and a character from the user and store it inside the list. 
#First print the list from the beginning and then from the end.

def myfun(fun,*val):
    fun(val)
list=lambda *x:[print(i) for i in x]
myfun(list,"sahil","20","2.4",True)





#5) accept 5 numbers, store them inside the list. now accept a number from user which he would like to remove 
#from the list and  after removing it, display the list.

num1=int(input("enter a number"))
num2=int(input("enter a number"))
num3=int(input("enter a number"))
num4=int(input("enter a number"))
num5=int(input("enter a number"))

list=[num1,num2,num3,num4,num5]
print(list)

user=int(input("enter a number"))
if user in list:
    list.remove(user)
    print(list)
else:
    print("invalid")



#6) accept 5 numbers, store them inside the list. now accept a position from user ,remove the element from that position and  
#after removing it, display the list.



num1=int(input("enter a number"))
num2=int(input("enter a number"))
num3=int(input("enter a number"))
num4=int(input("enter a number"))
num5=int(input("enter a number"))

list=[num1,num2,num3,num4,num5]
print(list)

num=int(input("enter number"))
list.pop[num]
print(list)

#7) create a list and store string,number,character,boolean,decimal values respectively inside it.
#Now slice it in following ways:
#a) display it in reverse order
#b) list all the elements from 2nd position
#c) list the elements from 1st to 3rd position
#d) slice it from 1st to 3rd elements from the end.


list = ["sahil",777,"@",True,4.5]
print(list)
print("reverse order")
print(list[::-1])
print("elemnts from 2nd position")
print(list[1:])
print("elemnts from 1st to 3rd")
print(list[0:3])
print("elements from 1 to 3 from end")
print(list[-1:-4:-1])




#8) Note: use List comprehension
# create a list with the numbers from 1 to 20
# create one more list which should contain only odd numbers from the first list.

orignal_list=list(range(1,21))
print(orignal_list)

odd_list=[i for i in orignal_list if i%2!=0]
print(odd_list)

even_list=[x for x in orignal_list if x%2==0]
print(even_list)





#9) accept 5 names and store them in list. Now sort the list in ascending order display and then in descending order.


names = []

for i in range(5):
    name = input("Enter name")
    i+=1
    names.append(name)

ascending_sorted_names = sorted(names)

descending_sorted_names = sorted(names, reverse=True)

print("List of Names (Ascending Order):", ascending_sorted_names)
print("List of Names (Descending Order):", descending_sorted_names)


