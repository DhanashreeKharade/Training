#############################################################################
#                    TASK--6                                                #
#############################################################################
#
# 1. Write a program in Python to find out the character in a string which is uppercase using list
# comprehension.
# ************************************************************************************************

# str=input("Enter String: ")
# char=[]
# for i in str:
#     if i.isupper():
#         char.append(i)
#     else:
#         continue
#
# result=tuple(char)
# print("Uppercase characters in given strings: ",result)
#
# output:Enter String: I LikE PyThon
# Uppercase characters in given strings:  ('I', 'L', 'E', 'P', 'T')

#########################################################################################################
# 2. Write a program to construct a dictionary from the two lists containing the names of students and
# their corresponding subjects. The dictionary should map the students with their respective subjects.
# Let’s see how to do this using for loops and dictionary comprehension.
# HINT - Use Zip function also
# Sample input: students = ['Smit', 'Jaya', 'Rayyan'] subjects = ['CSE', 'Networking', 'Operating System']
# Expected output: {‘Smit’ : ’CSE’ , ’Jaya’ : ’Networking’ , ’Rayyan’ : ’Operating System’}
# **********************************************************************************************************
# students = ['Smit', 'Jaya', 'Rayyan']
# subjects = ['CSE', 'Networking', 'Operating System']
#
# D=dict(zip(students,subjects))
# print("dictonary of Students and there Respective subjects is: ",D)
#
# **********************************************************************
# output:
# dictonary of Students and there Respective subjects is:  {'Smit': 'CSE', 'Jaya': 'Networking', 'Rayyan': 'Operating System'}
#########################################################################################################################################
#
# 3. Learn More about Yield, next and Generators
#
# ok

###########################################################################################################################
# 4. Write a program in Python using generators to reverse the string.
# Input String = “Consultadd Training”
# *******************************************************************************
# generator to reverse a string
# def reverse_string(my_str):
#     length = len(my_str)
#     for i in range(length-1, -1, -1):
#         yield my_str[i]
#
# # using for loop to reverse the string
# for char in reverse_string("Python"):
#     print(char)
#**********************************************************************
# output:
#     n
#     o
#     h
#     t
#     y
#     P
#
######################################################################################
# 5. Write an example on decorators.
######################################################################################
#
# Python Decorators are:
# 1.Function can be assign to variable
# 2.Function can be acccess through other variable
# 3.function can be nested within another function
# 4.function can be passed to another function as an argument
#
# Example:here inner_function is nested within outer_function and inner_function is called from outer function.
# #
# def outer_function():
#
#     def inner_function():
#
#         print('I came from the inner function.')
#
#     # Executing the inner function inside the outer function.
#     inner_function()
# outer_function()
#
# # # Output:
# I came from the inner function.
############################################################################################################
#                                                                                                          #
#                   TASK-6 Completed Successfully                                                          #
#                   Author:Dhanashree A Kharade                                                            #
############################################################################################################