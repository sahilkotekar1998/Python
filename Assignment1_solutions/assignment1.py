#1)	accept a number and display its table.   

num = int(input("Enter a number: "))

for i in range(1,11):
    result= num*i
    print(f"{num}*{i}={result}")



    
#2)	using switch ….case display whether accepted character is vowel or not.

vowel = (input("enter character to check it is vowel or not"))

ch = vowel

match ch:
    case "A":
        print("VOWEL")
    case "E":
        print("VOWEL")
    case "I":
        print("VOWEL")
    case "O":
        print("VOWEL")
    case "U":
        print("VOWEL")
    case _:
        print("NOT VOWEL")


#3)	Display numbers  1 to 10 using  While loop

i=1
while(i<11):
    print(i)
    i+=1

#4)	Display numbers from 3 to 30 except number 24  using while loop.

number = 3

while(number<=30):
    if (number!=24):
        print(number, end=' ')
    number+=1




#5) accept marks from the user. Using if…….elif…. Else,  
# display whether result is  fail, pass, second class , first class, Distinction etc.  

marks=int(input("enter marks"))
if(marks<40):
    print("FAIL")
elif(marks>=40 and marks<60):
    print("PASS AND SCORED SECOND CLASS")
elif(marks>=60 and marks<75):
    print("PASS AND FIRST CLASS")
elif(marks>=75 and marks<=100):
    print("PASS AND DISTINCTION")
else:
    print("invalid marks\n")


#6) print the total of first 10 numbers.

sum=0
for i in range(1,10):
    sum+=i
print("sum of first 10 numbers is :", sum)


#7) accept numbers till user enters 0 and display the total of all the numbers entered.

total = 0
while(True):
    number=int(input("enter a number"))
    if(number==0):
        break
    total+=number
    print(f"the total of all numbers entered is: {total}")


#8) accept a charac ter and display whether it is upper case or lower case or not an alphabet. 
char = input("Enter a character: ")

if len(char) == 1 and char.isalpha():
    if char.islower():
        print(f"{char} is a lowercase letter.")
    elif char.isupper():
        print(f"{char} is an uppercase letter.")
else:
    print(f"{char} is not an alphabet character.")


print("hello")