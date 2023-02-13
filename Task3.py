#############################################################################################
#                                   TASK-3                                                   #
#############################################################################################
#1. Create a list of 10 elements of four different data types like int, string, complex and float.
# ******************************************************************************************************
# x=7
# y=3.7
# z=3+4j
# w="welcome"
# list=list[x,y,z,w]
# print(list)
#
# output: list[7, 3.7, (3+4j), 'welcome']
############################################################################################
# 2. Create a list of size 5 and execute the slicing structure
# ******************************************************************************************
# list = [2,3,5,7,9]
# print(list[:],list[2:9:],list[2:9:2])
#
# output:[2, 3, 5, 7, 9] [5, 7, 9] [5, 9]
# ###################################################################################
# Write a program to get the sum and multiply of all the items in a given list.
# ***********************************************************************************
# x = [2,3,5,7,9]
# def add():
#     result=0
#     for i in x:
#           result = result+i
#     return result
# def mul():
#     result=1
#     for i in x:
#         result=result*i
#     return result
#
# addition=add()
# print("addition of list items :",addition)
# multi=mul()
# print("Product of list items :",multi)

# output:
# addition of list items : 26
# Product of list items : 1890

#############################################################################
#4 Find the largest and smallest number from a given list.
#*****************************************************************************
# list=[1,3,5,7,9]
# s=min(list)
# l=max(list)
#
# print("Smallest no of given list :",s)
# print("largest no of given list :",l)
#
# output:
# Smallest no of given list : 1
# largest no of given list : 9

#######################################################################################################
#5. Create a new list which contains the specified numbers after removing the even numbers from a
# predefined list.
#******************************************************************************************************
# list=[1,3,4,6,8,7,3,9,27,14,37,54,32,77]
#
# def add():
#     x=[]
#     for i in list:
#         if i%2==0:
#             continue
#         else:
#             x.append(i)
#     return x
# newl=add()
# print("Required list is -",newl)
#
# output:
# Required list is - [1, 3, 7, 3, 9, 27, 37, 77]

########################################################################################
#
# 6. Create a list of elements such that it contains the squares of the first and last 5 elements between
# 1 and30 (both included).*
#***************************************************************************************************
# def square():
#     list=[]
#     for i in range (1,31):
#          list.append(i**2)
#     return list
#
# x=square()
# print("Square of 1st 5 elements: ",x[:5])
# print("Square of last 5 elements:",x[-5:])
#
# output:Square of 1st 5 elements:  [1, 4, 9, 16, 25]
# Square of last 5 elements: [676, 729, 784, 841, 900]
# ###############################################################################################3
# 7. Write a program to replace the last element in a list with another list.
# Sample input: [1,3,5,7,9,10], [2,4,6,8]
# Expected output: [1,3,5,7,9,2,4,6,8]
#*************************************************************************************************
# list=[1,3,5,7,9,10]
# list2=[2,4,6,8]
# list[-1]=list2
# print(list)
#
# output:[1, 3, 5, 7, 9, [2, 4, 6, 8]]

# ###########################################################################################
# 8.Create a new dictionary by concatenating the following two dictionaries:
# Sample input: a={1:10,2:20} b={3:30,4:40}
# Expected output: {1:10,2:20,3:30,4:40}
#********************************************************************************************
# a = {1: 10, 2: 20}
# b = {3: 30, 4: 40}
# # a.update(b)
# dict={}
# dict.update(a)
# dict.update(b)
# print("New Dictonary: ",dict)
#
# output:New Dictonary:  {1: 10, 2: 20, 3: 30, 4: 40}
# #############################################################################################################

# 9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
# and n(both 1 and n included).
# Sample input: n=5
# Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}
#***************************************************************************************************************

# n=int(input("Till what no you want expected values:"))
# dict={}
# for i in range(1,n+1):
#     dict[i]=i*i
# print(dict)
#
# output:Till what no you want expected values:10
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

####################################################################################################
# 10. Write a program which accepts a sequence of comma-separated numbers from console and
# generates a list and a tuple which contains every number in the form of string.
# Sample input: 34,67,55,33,12,98
# Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)
# ************************************************************************* ***************************
# #
# values=input("Enter some numbers separated with ',':").split(',')
# x=int(values)
# # list=[]
# # tuple=()
# for x in values:
#     list=str(values)
#     tuple=str(values)
# print("List: ",list)
# print("Tuple:",tuple)
#
# numbers=[int(x) for x in input("Enter some numbers separated with ',': ").split(',')]
# print("List: ",str(numbers))
# print("Tuple",str(tuple(numbers)))
# ******************************************************************************
# OutPut:Enter some numbers separated with ',': 3,4,5,7,1,21,77
# List:  [3, 4, 5, 7, 1, 21, 77]
# Tuple (3, 4, 5, 7, 1, 21, 77)

###################################################################################################
#************************************************************************************#
#*                                                                                   #
#*                  TASK-4 COMPLETED SUCCESSFULLY                                    #
#*                  Author: Dhanashree Kharade                                       #
#*                                                                                   #
#*************************************************************************************#





