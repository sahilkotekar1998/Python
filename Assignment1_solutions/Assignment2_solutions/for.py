name = "sahilz"
for words in name:
    print(words)
    if(words=="z"):
        print("thats great")

trees=["mango","banana","lemon","neem"]
for tree in trees:
    print(tree)
    if(tree=="neem"):
        for t in tree:
            print(t)




for i in range(1,11):
    if(i==3 or i==9):
        continue
    print(i)


for i in range(1,21):
    if(i%2!=0):
        continue
    print(i)


for i in range(1,11,2):
    if(i==5):
        continue
    print(i)


#print tables

user_input=(int(input("enter number")))
for i in range(1,11):
    result = i*user_input
    print(f"{user_input}*{i}={result}")

user_no=(int(input("enter number")))
for i in range(1,11):
    result = i*user_no
    print(f"{user_no}*{i}={result}")


for i in range(1,11):
    result=i*6
    print(f"6*{i}={result}")



#print addition of number till user enters number

number = int(input("Enter a number: "))

total = 0
for i in range(1, number+1):
    total=total+i

print(f"The total from 1 to {number} is: {total}")



total = 0
while(True):
    number=int(input("enter a number"))
    if(number==0):
        print("entered 0 you are exited and the total of your numbers is ", total)
        break
    total+=number
    print(f"the total of all numbers entered is: {total}")



