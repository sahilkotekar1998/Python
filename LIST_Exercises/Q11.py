#11. Write a Python function that takes two lists and returns True if they have at least one common member.

list1=[1,2,3,4,5,6]
list2=[7,8,9,0,1]

def common(list1,list2):
    set1=set(list1)
    set2=set(list2)
    checkd=(set1.intersection(set2))
    print(checkd)
    #return bool(set1.intersection(set2))
result = common(list1, list2)
print(result)
