import numpy as np

# arr1=np.array([234,545,678,546,999])
# arr2=np.array([[777,888,222,444,111],[222,333,444,555,666]])
# # print(arr1)
# # print(arr2)

# for i in range(0,arr2.__len__()):
#     print(arr2[i])

# print(type(arr1))
# print(arr1.ndim)
# print(arr1.shape)

# print(arr2)

# print(type(arr2))
# print(arr2.ndim)
# print(arr2.shape)

# for i in range(0,arr2.__len__()):
#     print(arr2[i])

# print(type(arr2))
# print(arr2.shape)
# print(arr2.ndim)

# # arr2[2]=300
# # print(arr2)

# arr1=np.array([100,"hello",3.4,True])
# print(arr1)
# print(arr1.ndim)
# print(arr1.shape)
# print(type(arr1))


# arr2=np.array([1,2,3,4,5])
# print(arr2)
# print(arr2[2])
# print(arr2[0])
# print(arr2[-1])

# for i in range(-1,(arr2.__len__()+1),-1):
#     print(arr2[i])



# mylist=["sahil","pankaj","gaurav"]
# for i in mylist:
#     for j in i:
#         print(j)
#     print(i)




# first=np.array([[10,20,30],[40,50,60]])    #  here we've passed list of list (nested list, 2D array)
# print(first)
# print("\n")
# for i in range(0,first.__len__()):
#     for j in range(0,first[i].__len__()):
#         print(first[i][j],"\t",end="")
#     print("\n")

# print("Type of the array is",type(first))
# print("\n")
# print("dimension of array is\t",first.ndim)
# print("\n")
# print("shape of array is\t",first.shape)


# arr1=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# for i in range(0,arr1.__len__()):
#     for j in range(0,arr1[i].__len__()):
#         print(arr1[i][j],end=" ")
#     print("\n")



# arr1=np.ones((3,4))   #adds 0 in 3 rows and 4 columns
# print(arr1)

# arr2=np.full((3,4),7)  #adds 7 in 3 rows and 4 columns
# print(arr2)


# arr1=np.arange(20,29)    #here 29 will not be printed it will be excluded
# print(arr1)

# arr2=np.arange(10,20,2)   #here 10 to 20  array will be printed with 2 gap excluding 20 
# print(arr2)


# arr1=np.arange(10,91,10).reshape(3,3)    # 3 rows,3 cols ,  10 to 90 values with 10 as a skip value
# print(arr1)

# arr2=np.arange(10,61,10).reshape(3,2)
# print(arr2)



# arr1=np.random.randint(1,100,10)
# print(f"10 random numbers in 1 to 100 are : {arr1}")  

# arr2=np.random.randint(1,20,3)    #return array of 3 random objects from 1 to 20
# print(arr2)


# from numpy import *


# # random.seed(2)    #if we add seed and any number the output of random numbers will come same
# arr1=random.randint(1,50,2)
# print(arr1)


# arr1=np.array([1,2,3,4,5,6])   
# # print(arr1.shape)
# arr1.shape=(2,3)       #changing the shape of array
# print(arr1)
# print(arr1.ndim)

# arr1=np.array([[[1,2,3,4,5],[6,7,8,9,10],[6,7,8,9,10]]])
# print(arr1.ndim)
# arr2=np.array([[11,12,13,14,15],[16,17,18,19,20]])
# print(arr2.ndim)


# arr1=np.array([1,2,3,4,5])
# arr2=np.array([6,7,8,9,10])

# arr3=np.stack((arr1,arr2),axis=0)
# print(arr3)

# # [[ 1  2  3  4  5]
# #  [ 6  7  8  9 10]]

# print("-----------------------")

# arr1=np.array([1,2,3,4,5])
# arr2=np.array([6,7,8,9,10])

# arr3=np.stack((arr1,arr2),axis=1)
# print(arr3)

# # [[ 1  6]
# #  [ 2  7]
# #  [ 3  8]
# #  [ 4  9]
# #  [ 5 10]]

# print("----------------------------")

# arr1=np.array([[1,2,3,4,5],[1,2,3,4,5]])
# arr2=np.array([[6,7,8,9,10],[6,7,8,9,10]])
# arr3=np.stack((arr1,arr2),axis=2)
# print(arr3)

# [[[ 1  6]
#   [ 2  7]
#   [ 3  8]
#   [ 4  9]
#   [ 5 10]]

#  [[ 1  6]
#   [ 2  7]
#   [ 3  8]
#   [ 4  9]
#   [ 5 10]]]

# arr1=np.array([1,2,3,4,5])
# arr2=np.array([6,7,8,9,10])

# arr3=np.sum((arr1,arr2),axis=0)
# print(arr3)

# #[ 7  9 11 13 15]


# arr1=np.array([1,2,3,4,5])
# arr2=np.array([6,7,8,9,10])

# arr3=np.sum((arr1,arr2),axis=1)
# print(arr3)

# #[15 40]



# arr1=np.array([[1,2,3,4,5],[21,22,23,24,25]])
# arr2=np.array([[6,7,8,9,10],[11,12,13,14,15]])

# arr3=np.sum((arr1,arr2),axis=2)
# print(arr3)

# #[[ 15 115]
# #  [ 40  65]]


# arr=np.array([[1,2,3,4],
#              [2,3,4,5],
#              [7,8,9,10]])
# arr1=np.sum(arr,axis=1)   # row-wise total
# # 1+2+3+4   2+3+4+5   7+8+9+10
# print(arr1)
# arr2=np.sum(arr,axis=0)  # column-wise total
# # 1+2+7     2+3+8     3+4+9     4+5+10
# print(arr2)


#output:

# [10 14 34]
# [10 13 16 19]



# print("Let's try with 3 arrays")

# a=np.array([[10,20,30],[40,50,60]])
# b=np.array([[70,80,90],[100,110,120]])
# c=np.array([[5,9,11],[15,17,18]])
# print("output of axis=0")
# print("**************")
# d=np.sum((a,b,c),axis=0)      
# print(d)

# """ [[ 85 109 131]  
#  [155 177 198]] """ 

# print("output of axis=1")
# print("*************")

# e=np.sum((a,b,c),axis=1)
# print(e)
# """ [[ 50  70  90]  
#  [170 190 210]  
#  [ 20  26  29]] """


# print("output of axis=2")
# print("************")
# f=np.sum((a,b,c),axis=2)
# print(f)
# """ [[ 60 150]
#  [240 330]
#  [ 25  50]] """



arr1=np.array([[12,34],[45,67]])
arr2=np.sort(arr1,axis=1)
print(arr2)