name=input("enter your name")
technology=input("enter technology name")
preference=input("enter 'first' or 'second' as a preference")
message="{} is {}'s {} preference"
print(message.format(technology,name,preference))



print("------------------------")

name = input("enter your name")
age = int(input("enter your age"))
tech = input("enter technology in which you are working")
message = "my name is {} and my age is {} i am currently working on {}"
print(message.format(name,age,tech))