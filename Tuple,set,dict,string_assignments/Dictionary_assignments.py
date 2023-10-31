my_dict={
    "name":"sahil",
    "age":25,
    "edcuation":"BTECH",
    "phone_number":"9130654768",
    "email_id":"sahil.kotekar@gmail.com",
    "city":"nashik",
    "sex":"male",
    777:"sk",
    "eligible":True
}
print(my_dict[777])

print(my_dict.get("salary"))   #this key is not present in dict so it will print none if we write .get

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

new={"rahul":78,"sachin":90}
my_dict.update(new)
print(my_dict)





# for key,value in my_dict.items():
#         print(f"The value corresponding to the key {key} : {value}")



ep1={1:90,
    2:75,
    3:80,
    4:95
}
ep2={5:30,
     6:65
}
ep1.update(ep2)
print(ep1)

empt={}
empt.update(ep2)
print(empt)



ep1={1:90,
    2:75,
    3:80,
    4:95
}
ep2={5:30,
     6:65,
     7:90,
     8:100
}
ep1.clear()
print(ep1)

ep2.pop(6)
print(ep2)        #removes 6th key elemnt

ep2.popitem()     #removes last element
print(ep2)

del ep2[7]        #deletes specific elemnt
print((ep2))











