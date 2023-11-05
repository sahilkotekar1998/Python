# 1) create a list, accept 5 numbers , store them in the list and finally convert that list to numpy array.
import numpy as np
import pandas as pd


# mylist=[]
# for i in range(5):
#     user=int(input("enter a number"))
#     mylist.append(user)
# print(mylist)

# myarr=np.array(mylist)
# print(myarr)





# #2) create numpy array of 5 numbers and print their sum


# myarr=np.array([1,2,3,4,5])

# arr_sum=np.sum(myarr)
# print(arr_sum)





# # 3) create numpy double dimension array of 3*3 to store your initial and display them in a tabular form.


# arr1=np.array([[1,2,3],[5,6,7],[9,10,11]])
# print(arr1)

# df=pd.DataFrame(arr1)
# print(df)
# # or
# for row in arr1:
#     print("\t".join(map(str, row)))






# 4) create one-d numpy array of 12 elements , accept 12 numbers and display them. 
# Now convert this one-d array into (4*3) two-d array and display it in a tabular form.

# arr1=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(arr1)

# new_arr=arr1.reshape(4,3)
# print(new_arr)

# df=pd.DataFrame(new_arr)
# print(df)

# # OR

# # Create a 1D NumPy array with 12 elements
# array_1d = np.empty(12, dtype=int)

# # Accept 12 numbers from the user
# for i in range(12):
#     array_1d[i] = int(input(f"Enter element {i + 1}: "))

# # Convert the 1D array into a 4x3 2D array
# array_2d = array_1d.reshape(4, 3)

# # Display the 1D array
# print("1D NumPy array:")
# print(array_1d)

# # Display the 2D array in a tabular form
# print("2D NumPy array (4x3):")
# for row in array_2d:
#     print("\t".join(map(str, row)))

# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(arr)

# new=arr.reshape(4,3)
# print(new)

# df=pd.DataFrame(new)
# print(df)


# arr1=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(arr1)

# new=arr1.reshape(4,3)
# print(new)


# 5) create two double dimension array and arrange (stack) them using "axis=0" "axis=1" and  "axis=2".

# first=np.array([[1,2,3,4],[5,6,7,8]])
# second=np.array([[10,20,30,40],[50,60,70,80]])

# third=np.stack((first,second),axis=0)
# print(third)

# fourth=np.stack((first,second),axis=1)
# print(fourth)

# fifth=np.stack((first,second),axis=2)
# print(fifth)

# print(first.ndim)







#6) create two one-d arrays and then find out:
	# a) common elements of both the array
	# b) unique elements of first array
	# c) unique elements of second array

# first=np.array([[1,20,3,4],[5,6,7,8]])
# second=np.array([[10,20,30,40],[50,60,70,80]])

# third=np.intersect1d(first,second)
# print(third)

# fourth=np.setdiff1d(first,second)
# print(fourth)

# fifth=np.setdiff1d(second,first)
# print(fifth)







#7) accept no.of rows and no. of cols from the user , create two-d array accordingly. 
# Now calculate the sum as per "axis=0" and "axis=1"


# mylist=[]

# row=int(input("enter number of rows"))
# col=int(input("enter number of columns"))

# elements=row*col
# for i in range(1,(elements)+1):
#     user=int(input("enter values"))
#     mylist.append(user)
#     print(mylist)

# first=np.array(mylist)
# print(first)

# second=np.stack(first.reshape(3,3))
# print(second)

# oo=np.sum(second,axis=0)
# print(oo)

# oo1=np.sum(second,axis=1)
# print(oo1)

# oo2=np.sum(second,axis=2)
# print(oo2)



#8) declare two 2d arrays and calculate the sum as per "axis=0" "axis=1" and "axis=2"

# arr1=np.array([[1,2,4],[4,5,6]])
# arr2=np.array([[1,2,3],[4,5,6]])

# add=np.sum((arr1,arr2),axis=0)
# print(add)

# add1=np.sum((arr1,arr2),axis=1)
# print(add1)

# add2=np.sum((arr1,arr2),axis=2)
# print(add2)


# 9) create two-d array ,display it. Now accept a number from user and perform all arithmetic operations on each and every 
# element of the array using that number.



# arr1=np.array([[1,2,3],[4,5,6]])
# print(arr1)

# user=float(input("enter number"))

# result_arr=arr1+user
# print(result_arr)

# result_arr_substract=arr1-user
# print(result_arr_substract)

# result_arr_multiply=arr1*user
# print(result_arr_multiply)




#10) accept start, end and how many numbers to be generated and then using "linspace" create numpy array.


# start=int(input("enter starting number"))
# end=int(input("enter ending number"))

# lin=int(input("enter line space"))

# first=np.linspace(start,end,num=lin)
# print(first)
    


#11) create one-d array of 8 numbers and then using "slicing" concept,
	# a) print numbers from 1 to 4
	# b) print all the numbers from 3rd position
	# c) print last 3 numbers


# arr1=np.array([1,2,3,4,5,6,7,8])
# print(arr1)

# print(arr1[0:4])

# print(arr1[3:])

# print(arr1[-4:-1])





#12) create 2 d array (4*3) with following values:
# [[10,20,30,40],[50,60,70,80],[90,100,110,120]]

# now using array slicing concept display following values
# 	a) display   50  60  70  80
# 	b) display 100 and 110
# 	c) display 30 70 and 110
# 	d) display 50  60  90 and 100


# arr1=np.array([[10,20,30,40],[50,60,70,80],[90,100,110,120]])
# print(arr1)

# print(arr1[1][:4])

# print(arr1[2][1:3])

# print(arr1[0][2])
# print(arr1[1][2])
# print(arr1[2][2])


# #OR



# # Create a 2D array (4x3) with the given values
# array_2d = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]])

# print("Original 2D Array:")
# print(array_2d)

# result_a = array_2d[1, 0:4]
# print("\na) Display 50 60 70 80:")
# print(result_a)

# result_b = array_2d[2, 1:3]
# print("\nb) Display 100 and 110:")
# print(result_b)

# result_c = array_2d[0:3, 2]
# print("\nc) Display 30 70 and 110:")
# print(result_c)

# result_d = array_2d[1:3, 0:2]
# print("\nd) Display 50 60 90 and 100:")
# print(result_d)









