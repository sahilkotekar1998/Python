import numpy as np

# arr1=np.array([5,4,3,2,1])
# arr1.sort()
# print(arr1)

# arr2=np.array([200,900,500,100])
# arr2.sort()
# print(arr2)

# arr3=np.array([34,67,12,16,9,99])
# arr3.sort()
# print(arr3)


arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.sort(arr1,axis=None)
print(arr2)

# [1 2 3 4 5 6]

print("--------------------")

arr1=np.array([[5,2,3],[4,5,6]])
arr2=np.sort(arr1,axis=0)
print(arr2)


# [[4 2 3]
#  [5 5 6]]
print("--------------------")


arr1=np.array([[12,34],[45,67]])
arr2=np.sort(arr1,axis=1)
print(arr2)

#[[12 34]
#  [45 67]]

print("============================")
print("Reverse order column-wise\n")
arr1=np.array([[12,34],[45,67]])

arr2=np.sort(-arr1,axis=0)
print(arr2)

#[[-45 -67]
#  [-12 -34]]


print("-----------------------------")
print("Reverse order row-wise\n")
arr1=np.array([[12,34],[45,67]])

arr2=np.sort(-arr1,axis=1)
print(arr2)


print("===========================================================")


myar=np.array([[[10,20,30],[4,5,6]],[[70,8,90],[3,110,12]]])
print(myar)
print("Ascending order 3d array column-wise")
"""
10 will be compared with 70, 20 will be with 8, 30 will be with 90
4 will be with 65, 50 will be with 110, 6 will be with 12
"""
arr1=np.sort(myar,axis=0)
print(arr1)

print("Ascending order 3d array row-wise")
""" 10 will be compared with 4, 20 will be with 50, 30 will be compared with 6
70 will be compared with 65, 8 will be compared with 110, 90 will be compared with 12"""
arr1=np.sort(myar,axis=1)
print(arr1)
print("Reverse order 3d array column-wise\n")
arr1=-np.sort(-myar,axis=0)
print(arr1)
print("Reverse order 3d array row-wise\n")
"""
10 will be compared with 4, 20 with 50, 30 with 6
70 with 65, 8 with 110,  90 with 12
"""
arr1=-np.sort(-myar,axis=1)
print(arr1)





