#1) accept a number and display its table.

a=int(input("enter a number : "))
print("table for  ",a)
sum=0
for i in range(1,11):
    print(a,"x",i,"=",a*i)
    
#2) using switch ….case   display whether accepted character is vowel or not.

a=input("enter char")
match a:
    case'A':
        print("Vowel")
    case'a':
        print("Vowel")
    case 'E':
        print("Vowel")
    case 'e':
        print("Vowel")
    case 'I':
        print("Vowel")
    case 'i':
        print("Vowel")
    case 'O':
        print("Vowel")
    case'o':
        print("Vowel")
    case _:
        print("Not Vowel")


#3) Display numbers  1 to 10 using  While loop

i=1
while(i<11):
    print(i)
    i+=1


#4)Display numbers from 3 to 30 except number 24  using while loop.

i=3
while i<31:
    if i==24:
        i+=1
        continue
    print(i)
    i+=1


#5)accept marks from the user. Using if…….elif….  Else,  display whether result is  fail, pass, second class , first class, Distinction etc.  

marks=int(input("Enter The Marks: "))
if(marks<35):
    print("FAIL")
elif(marks<50):
    print("PASS")
elif(marks<75):
    print("Second Class")
elif(marks<90):
    print("First Class")
else:
    print("DISTINCTION")


#6)print the total of first 10 numbers.

i=1
a=0
while(i<11):
   a=i+a
   i+=1
print(int(a))



#7) accept numbers till user enters 0 and display the total of all the numbers entered.

a=0
while(True):
    i=int(input("Enter The Number: "))
    a=i+a
    if(i==0):
       break
    
print(int(a))



#8) accept a character and display whether it is upper case or lower case or not an alphabet.

ch=ord(input("Enter Any Character :"))
if(ch>=ord('A')):
    if(ch<=ord('Z')):
        print("Upper Case Letter")
    if(ch>=ord('a')):
        if(ch<=ord('z')):
            print("Lower Case Letter")
else:
    print("Not An Alphanate")        

#9)display fibonicii series of 10 numbers


n=10
a , b= 0 , 1
for i in range(0,n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c


#10) display prime numbers from 3 to 30

for i in range(3, 31):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        print(i)
        
#11) accept a number and display whether it is prime or not

num=int(input("Enter The Number: "))
if num < 2:
      print(num, "is not a prime number.")
else:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print(num,"Is Not A Prime Number")
            break
    else:
        print(num,"Is A Prime Number")



#12) print the following pattern:

# *
# * *
# * * *
# * * * *
# * * * * *

for i in range(1,6):
    for j in range(0,i):
        print("*",end=" ")
    print(" ")


#13) print the following pattern:

# * * * * * 

# * * * * 

# * * * 

# * * 

# * 

for i in range(5,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print("  ")

#14) print the following pattern
	# 	*
	#      *  *
    #       *  *  *
    #    *  *  *  *
    # *  *  *  *  *

for i in range(1, 6):
      spaces = 5 - i
      stars = i * "*"

      print(" " * spaces + stars)


#15) print the following pattern

#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 


for i in range(1, 6):
      spaces = 5 - i
      stars = i * " *"

      print(" " * spaces + stars)


#16) print the following pattern

# *   *   *   *   *   

#   *   *   *   *   

#     *   *   *   

#       *   *   

#         *   


for i in range(5,0,-1):
      spaces = 5 - i
      stars = i * " *"

      print(" " * spaces + stars)


#17) print the following

#      * 
#     * * 
#    * * * 
#   * * * * 
#  * * * * * 
# * * * * * * 
#  * * * * * 
#   * * * * 
#    * * * 
#     * * 
#      * 


for i in range(1, 6):
      spaces = 5 - i
      stars = i * " *"

      print(" " * spaces + stars)
for i in range(5,0,-1):
      spaces = 5 - i
      stars = i * " *"

      print(" " * spaces + stars)



