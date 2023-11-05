# 1) store marks of 5 subjects
# 	here use marks as actual data and subject names as indexes.
# accept both marks and subjects from the user.

import pandas as pd
import numpy as np
from pandas import *



marks_dict={}
for i in range(5):
    sub=input("enter subject name")
    marks=int(input("enter marks"))
    marks_dict[sub]=marks

print("subject wise marks: ")
for subject,marks in marks_dict.items():
    print(subject,marks)


# marks_dict={}
# for i in range(5):
#     sub=input("enter subject")
#     marks=int(input("enter marks"))
#     marks_dict[sum]=marks

# for sub,marks in marks_dict.items:
#     print(sub,marks)














# 2) create dictionary to store player name and runs scored of at least 5 players. Display it. 
# Now convert this dictionary ‌into Series object and print it.



mydict={"sachin":89,
        "dravid":78,
        "gavaskar":363,
        "kohli":34,
        "yuvraj":90}

print(mydict)

series=pd.Series(mydict)
print(series)


mydict={"sachin":50,"dravid":90}
print(mydict)

series=pd.Series
print(series)



# 3) accept 10 values and store them in the Series. Now perform following operations:

# a) display the entire Series
# b) extract 3rd element
# c) extract elements from 4 to 7
# d) extract elements from fourth last till the last element
# e) extract first 3 elements
# f) extract elements from the 5th position


myseries=[]
for i in range(10):
    user=int(input("enter a number"))
    myseries.append(user)
    print(myseries)

myseries1=pd.Series(myseries)
print(myseries1)

print(myseries1.iloc[2])
print(myseries1.iloc[4:8])
print(myseries1.iloc[-4:])
print(myseries1[1:4])
print(myseries1.iloc[5])



# 4) accept 5 values in a Series and perform the following operations:
# 	a) display their sum
# 	b) add the value accepted from the user
# 	c) subtract the value accepted from the user
# 	d) multiply the value accepted from the user
# 	e) add the value accepted from the user


series=[]
for i in range(5):
    value=int(input("enter a number"))
    series.append(value)

myseries=pd.Series(series)
print(myseries)

print(myseries.sum())
user=int(input("enter number to add"))
user1=int(input("enter number to substract"))
user2=int(input("enter number to multiply"))


add=myseries.add(user)
print(add)

sub=myseries.sub(user1)
print(sub)

multiply=myseries.multiply(user2)
print(multiply)

    



# 5) accept 5 names,designations and salaries and display them with DataFrame.


names=[]
designation=[]
salary=[]

for i in range(3):
    n=input("enter a name")
    d=input("enter designation")
    s=int(input("enter salary"))

    names.append(n)
    designation.append(d)
    salary.append(s)

data={"n":names,"d":designation,"s":salary}


df=pd.DataFrame(data)
print(df)



# 6) create a csv file (with whatever columns and rows you want) manually and then read using pandas.


myfile=read_csv("friends.csv")
df=pd.DataFrame(myfile)
print(myfile)

f=open("C:/Users/HP/Downloads/Python-Code/PANDAS/friendsss.csv","r")
for content in f:
    print(content)

f.close()
print("done")


myfile=read_csv("friendsss.csv")
df=pd.DataFrame(myfile)
print(df)




# 7) create "Vita.xlsx" using pandas. In this Excel file you have to create 2 sheets "DBDA", and "DAC". 
# in each sheet you have to write name,address and age of all the team leaders.
# make sure Excel file gets created successfully.

# pip install XlsxWriter

import pandas as pd

dbda_data = {
    "Name": ["TeamLeader1", "TeamLeader2", "TeamLeader3"],
    "Address": ["Address1", "Address2", "Address3"],
    "Age": [30, 32, 28],
}

dac_data = {
    "Name": ["LeaderA", "LeaderB", "LeaderC"],
    "Address": ["LocationA", "LocationB", "LocationC"],
    "Age": [35, 40, 29],
}

with pd.ExcelWriter("Vita.xlsx", engine="xlsxwriter") as writer:
    pd.DataFrame(dbda_data).to_excel(writer, sheet_name="DBDA", index=False)
    pd.DataFrame(dac_data).to_excel(writer, sheet_name="DAC", index=False)

print("Excel file 'Vita.xlsx' created successfully with 2 sheets.")










