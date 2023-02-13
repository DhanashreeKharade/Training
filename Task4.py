#############################################################################
#                    TASK--4                                                #
#############################################################################
#1. Write a program to reverse a string.
# Sample input: “1234abcd”
# Expected output: “dcba4321”
# ***************************************************************************

# str=input("Enter String: ")

# print("Reverse string is: ",str[::-1])
#**************
# output:Enter String: I like Python
# Reverse string is:  nohtyP ekil I
#####################################################################################################
# 2.Write a function that accepts a string and prints the number of uppercase letters and lowercase
# letters.
# Sample input: “abcSdefPghijQkl”
# Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12
#****************************************************************************************************
# str=input("Enter any String: ")
# ucase=0
# lcase=0
# for i in str:
#     if i.isupper():
#         ucase=ucase+1
#     elif i.islower():
#         lcase=lcase+1
#     else:
#         pass
#
# print("Uppercase characters",ucase)
# print("Lower case Characters",lcase)
# ********************************************************
# output:
# Enter any String: I Like Python
# Uppercase characters 3
# Lower case Characters 8
########################################################################################################
# 3. Create a function that takes a list and returns a new list with unique elements of the first list.
# ***************************************************************************************
# def unique(list):
#     newList=[]
#     for i in list:
#         if i not in newList:
#             newList.append(i)
#     return newList
#     print(newList)
# nl=unique([3,4,5,7,7,8,9,2,1])
# print("Required list: ",nl)
# # ***********************************************************
# output:Required list:  [3, 4, 5, 7, 8, 9, 2, 1]
#####################################################################################################
#
# 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
# in a hyphen-separated sequence after sorting them alphabetically.
#******************************************************************************************************

# words=[n for n in input("enter string or sequece of words: ").split('-')]
# words.sort()
# print('-'.join(words))

#*******************************
# output:enter string or sequece of words: pratibha-dhanashree-priya-anita-mitanshi
# anita-dhanashree-mitanshi-pratibha-priya
###########################################################################################################
# 5. Write a program that accepts a sequence of lines as input and prints the lines after making all
# characters in the sentence capitalized.
# Sample input: Hello world Practice makes man perfect
# Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT
# *******************************************************************************************************
# lines=[]
# while True:
#     l=input("Enter any words in sequence : ")
#     if l:
#         lines.append(l.upper())
#     else:
#         break;
#
# for l in lines:
#     print(l)
# #**********
# # lines = []
# # while True:
# #     l = input()
# #     if l:
# #         lines.append(l.upper())
# #     else:
# #         break;
# #
# # for l in lines:
# #     print(l)

######################################################################################################
# 6. Define a function that can receive two integral numbers in string form and compute their sum and
# print it in the console.
# *****************************************************************************************************
#
# def add(x,y):
#     # x,y=input("Enter 2 numbers: ").split(',')
#     print("X= ",x ,"\n","Y= ",y)
#     sum=x+y
#     print("Addition of 2 numbers= ",sum)
#
# add(7,9)
# # *****************************************
# output:X=  7
#  Y=  9
# Addition of 2 numbers=  16
# ########################################################################################################
# 7. Define a function that can accept two strings as input and print the string with the maximum length
# in the console. If two strings have the same length, then the function should print both the strings line
# by line.
#***********************************************************************************************************

# def lenght(str1,str2):
#     if len(str1) == len(str2) :
#         print(str1)
#         print("\n")
#         print(str2)
#     elif len(str1) < len(str2) :
#         print("String with max character is: ",str2)
#     else:
#         print("String with max character is: ", str1)
#
# str1=input(str("Enter 1st String: "))
# str2=input(str("Enter 2nd string: "))
# lenght(str1,str2)

# ************************************
# output:Enter 1st String: dhanashree
# Enter 2nd string: Python
# String with max character is:  dhanashree
###################################################################################################
# 8. Define a function which can generate and print a tuple where the values are square of numbers
# between 1 and 20 (both 1 and 20 included).
# **************************************************************************************************
# def square():
#     list=[]
#     for i in range (1,21):
#         list.append(i*i)
#
#     t=tuple(list)
#     print(t)
#
# square()
#
# ******************************************
# output:
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400)

################################################################################################
# 9. Write a function called showNumbers that takes a parameter called limit. It should print all the
# numbers between 0 and limit with a label to identify the even and odd numbers.
# Sample input: show Numbers(3) (where limit=3)
# Expected output:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD
# *****************************************************************************************
# x=input("Limit: ")
# limit=int(x)
# def shownumbers(limit):
#     for i in range(0,limit+1):
#         if i%2==0:
#             print(i,"EVEN")
#         else:
#             print(i,"ODD")
#
# shownumbers(limit)
#
#*************************************************
# output:  Limit: 20
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD
# 4 EVEN
# 5 ODD
# 6 EVEN
# 7 ODD
# 8 EVEN
# 9 ODD
# 10 EVEN
# 11 ODD
# 12 EVEN
# 13 ODD
# 14 EVEN
# 15 ODD
# 16 EVEN
# 17 ODD
# 18 EVEN
# 19 ODD
# 20 EVEN

#####################################################################################################
# 10. Write a program which uses filter() to make a list whose elements are even numbers between 1
# and 20 (both included)
#
# def even(x):
#     return x%2==0
#
# y=[3,5,6,76,54,23,77,55,88,22,67,90]
# print("List: ",y)
# z = filter(even, y)
# print("List of even numbers: ",list(z))
#
# *****************************************************
# output:
# List:  [3, 5, 6, 76, 54, 23, 77, 55, 88, 22, 67, 90]
# List of even numbers:  [6, 76, 54, 88, 22, 90]

##############################################################################################################
#
# 11. Write a program which uses map() and filter() to make a list whose elements are squares of even
# numbers in [1,2,3,4,5,6,7,8,9,10].
# Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the
# numbers in the filtered list. Use lambda() to define anonymous functions.
# ***************************************************************************************************************
#
# def even(x):
#     return x%2==0
#
# y=[1,2,3,4,5,6,7,8,9,10]
# print("List: ",y)
#
# z = filter(even, y)
# a=list[z]
# print("List of even numbers: ",a)
#
# list_square=[]
# for i in z:
#     list_square.append(i*i)
# print(list_square)
# ***************************************************
# output:
# List:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# List of even numbers:  list[<filter object at 0x000002ABB49B9900>]
# [4, 16, 36, 64, 100]
#
#######################################################################################
# 12. Write a function to compute 5/0 and use try/except to catch the exceptions
#**************************************************************************************
#
# def div(x,y):
#     try:
#         result=x//y
#         print("Result: ",result)
#
#     except ZeroDivisionError:
#         print("We can't divide any no by 0")
#
# div(5,0)
# **********************************************************
# output:We can't divide any no by 0

################################################################################################
# 13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
# ****************************************************************************
#
# list=[1,2,3,4,5,6,7]
# # list.__add__,(list)
# int("".join(map(str,(list))))
# print(str(list))
# ************************************************************************
# output:
# [1, 2, 3, 4, 5, 6, 7]
# //list is flatten.(how 1234567 is flatte.?I not understand but result came flatten list)
# #################################################################################################
# 14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
# Make sure to use only higher order functions.
# ********************************************************************************
#
# def cal(x):
#     if x%3!=0 and x%7==0:
#         print(x,"is not divisible by 3 but is multiple of 7")
#
#
# result=cal                                         #sent function as a parameter
# result(28)
# ****************************************************
# output:28 is not divisible by 3 but is multiple of 7

# ##########################################################################################################
# 15. Write a program in Python to multiply the elements of a list by itself using a traditional function
# and pass the function to map() to complete the operation.
# *************************************************************************************************************
#
# def square(i):
#     return  i*i
#
# x=[1,2,3,4,5,6,7,8,9]
# result = map(square,x)
# print("Required List: ",list(result))
#
# ****************************************************
# output:
# x=[1,2,3,4,5,6,7,8,9]
# ################################################################################################################

# What is the output of the following codes:
# *******************************************
# # (i)
# def foo():
#     try:
#         return 1
#     finally:
#         return 2
# k = foo()
# print(k)
# **********************************************
# output:
#         2
#
# ################################################################################################
# # (ii)
# def a():
#     try:
#         f(x, 4)
#     finally:
#         print("after f")
#         print("after f?")
# a()
#
# answer:
# This program has name error
#
# Error:NameError: name 'f' is not defined


#************************************************************************************#
#*                                                                                   #
#*                  TASK-4 COMPLETED SUCCESSFULLY                                    #
#*                  Author: Dhanashree Kharade                                       #
#*                                                                                   #
#*************************************************************************************#


























