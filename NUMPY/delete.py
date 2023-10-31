# my_set=set({})
# for i in range(5):
#     user_input=int(input("enter number"))
#     my_set.add(user_input)
#     print(my_set)

# reverse=sorted(my_set)
# print(reverse)

my_list=[]
for i in range(5):
    user=int(input("enter number"))
    my_list.append(user)
    print(set((my_list)))

my_list.remove(4)
print(my_list)


