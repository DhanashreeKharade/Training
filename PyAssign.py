# # #1.Create three variables in a single line and assign values to them in such a manner that each one of
# # #them belongs to a different data type.
# # # E.g. :
# # # a = 1,
# # # b = 2.01,
# # # c = 'string'
# #
# a,b,c=1,2.01,'string'
# print(a,b,c)
# print("Datatype of a : ",type(a),
#       "Datatype of b : ", type(b),
#       "Datatype of c : ",type(c))

# output:1 2.01 string
# Datatype of a :  <class 'int'> Datatype of b :  <class 'float'> Datatype of c :  <class 'str'>

# ********************************************************************************************************

# # # 2. Create a variable of type complex and swap it with another variable of type integer.
#
# x=complex(3,4)
# y=7
# x,y=y,x
# print("X = ",x, "  " ,"Y =",y)

# X =  7    Y = (3+4j)

# *************************************************************************************************
# # #3. Swap two numbers using a third variable and do the same task without using any third variable.
# # #------Using Third variable
# x= 3
# y=4
# temp=x
# x=y
# y=temp
# print(" X =",x ," ","Y =",y)

# # output: X = 4   Y = 3

# # #-----------Without using Third variable

# x=3
# y=4
# x,y=y,x
# print(" X =",x ," ","Y =",y)
#
# output:X = 4   Y = 3

# # 4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x
# # Version.
#
# x= input("Enter any number: ")
# print(x)
#
# # 5. Write a program to complete the task given below:
# # Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
# # another variable called z. Add 30 to z and store the output in variable result and print result as the
# # final output.
#
# x,y=input("Enter 2 numbers between 1 to 10(saperated with ','):").split(",")
# print("x:",x)
# print("y:",y)
# # x=input("Enter 1st number between 1 to 10:")
# # y=input("Enter any  number between 1 to 10:")
# z=int(x)+int(y)
# result=z+30
# print("result :",result)

# Output:
# Enter 2 numbers between 1 to 10(saperated with ','):3,4
# x: 3
# y: 4
# result : 37

#***********************************************************************************************
# # 6. Write a program to check the data type of the entered values.
# # HINT: Printed output should say - The data type of the input value is : int/float/string/etc
#
# x= 7
# y=7.5
# z="Welcome"
# w=3+4j
# print(type(x))
# print(type(y))
# print(type(z))
# print(type(w))
#
# Output:
# C:\pythonProject1\venv\Scripts\python.exe C:\pythonProject1\venv\Assign.py
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'complex'>
#####################################################################################################
# Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and UPPERCASE.
# #####################################################################################################
# str = input("Enter String - ")
# str_split = str.split(" ")
# len = len(str_split)
# i = 0
# j = 0
# while i < len:
#     if i == 0:
#         first_str = str_split[i]
#         first_str_len = len(first_str)
#         print(first_str)
#     i = i + 1
# # while i < len:
# #     length_of_first_part = len(str_split[i])
# #     while j < length_of_first_part:
# #         print(str_split[i][j])

##* not getting proper output I wil complete this prog in next assignment.

# #####################################################################################################################################
# 8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
# again. Will it change the value? If Yes then Why?
#Answer:*****************************************************************
#Yes, it is possible in python, to reassign the variable with new value of different datatype than its current value .
#In fact variables can be reassigned to any valid value in Python,regardless of iys current value.
# Variables are essentially like an empty box, that can contain something like a string, number, or other value.
# When you assign it a value, the box will contain that value, and when you reassign it, it will empty out the old value, and the new value will be placed inside of it.

#Example :
# This variable is initially assigned as a string.
# var = "Hi there"
#
# # It can be reassigned to any other value, regardless of the type.
# var = 35
# var = True
# thisVar = "test1"
#
# print(var)

#output: True