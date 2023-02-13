#############################################################################
#                    TASK--5                                                #
#############################################################################
# 1. Write a program in Python to allow the error of syntax to be handled using exception handling.
# HINT: Use SyntaxError
#***************************************************************************************************
# try:
#     print eval('six times seven')
# except SyntaxError,err:
#     print 'Syntax error %s (%s-%s): %s' % \
#     (err.filename, err.lineno, err.offset, err.text)
# print err
# try:
#     print(eval('six times seven'))
# except SyntaxError:
#     print("Syntax Error")
# ************************************************
# Output:
# Syntax Error
#################################################################################################
# 2. Write a program in Python to allow the user to open a file by using the argv module. If the
# entered name is incorrect throw an exception and ask them to enter the name again. Make sure
# to use read only mode.
# ***************************************************************************************
# Python program to demonstrate
# opening a file
# ***********************************************
#import idlelib.run
# Python program to demonstrate
# opening a file

# import sys
#
# n = len(sys.argv)
#
# if n > 2:
#     print("Please enter only one file name at a time")
#     exit
# else:
#     file_name = sys.argv[1]
#     print("You have entered file name - ",file_name)
#     try:
#             file1 = open(file_name,"r")
#             # Reading from file
#             print(file1.read())
#             file1.close()
#     except:
#         print("There is exception: Please enter correct file")
#**********************************************************************************
# Output:
# Scenario 1. Valid file argument i.e. Test.txt
# You have entered file name -  Test.txt
# File content is -
#  This is test file.
#**
# Scenario 2. Invalid file argument i.e. Test_1.txt
# You have entered file name -  Test_1.txt
# There is exception: Please enter correct file
#####################################################################################################
#Write a program to handle an error if the user entered a number more than four digits it should
# return “The length is too short/long !!! Please provide only four digits”
# ***************************************************************************************************
# number = input("Please enter the number - ")
#
# number_of_digit = len(number)
# print("User entered ", number_of_digit, " digit number")
#
# if number_of_digit != 4:
#     raise Exception("The length is too short/long !!! Please provide only four digits")
# else:
#     print("You entered correct number - ",number)
#***************************************************************************************************
# Output -
# Please enter the number - 12
# User entered  2  digit number
# Traceback (most recent call last):
#   File "C:\Users\khara\OneDrive\Desktop\ConsultAdd\Training\Task-5.py", line 61, in <module>
#     raise Exception("The length is too short/long !!! Please provide only four digits")
# Exception: The length is too short/long !!! Please provide only four digits
##########################################################################################################
#
# 4. Create a login page backend to ask users to enter the username and password. Make sure to
# ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
# should not be more than 3 times.
# # *********************************************************************************************************
# user_name = input("Enter Username - ")
# count = 0
# while count<3:
#     password = input("Enter Password - ")
#     try:
#         if password != "password123":
#             print("You have entered incorrect password, please enter password again.")
#             count = count + 1
#             print("Attempt number - ",count)
#             continue
#         else:
#             raise Exception("Password attempt exceeded exception")
#     except Exception as e:
#         print(e)
#**********************************************************************************************
# output:Enter Username - dyfyg
# Enter Password - yfhg
# You have entered incorrect password, please enter password again.
# Attempt number -  1
# Enter Password - yfyd
# You have entered incorrect password, please enter password again.
# Attempt number -  2
# Enter Password - rtdyy
# You have entered incorrect password, please enter password again.
# Attempt number -  3
#################################################################################################
# 5. Go through the link provided below to understand finally and raise concept:
# https://www.programiz.com/python-programming/exception-handling
# ***********************************************************************************************
#
# try:
#     numerator = 10
#     denominator = 0
#
#     result = numerator / denominator
#
#     print(result)
# except:
#     print("Error: Denominator cannot be 0.")
#
# finally:
#     print("This is finally block.")
# *****************************************************************
#     output:
#     Error: Denominator cannot be 0.
#     This is finally block.
#
##############################################################################################
#6. Read doc.txt file using Python File handling concept and return only the even length string from
# the file. Consider the content of doc.txt as given below:
# Hello I am a file
# Where you need to return the data string
# Which is of even length
# Make sure you return the content in The same link as it is present.
#******************************************************************************************************
#
# file_name = "test1.txt"
# print("You have entered file name - ",file_name)
# try:
#      file = open(file_name,"r")
#      # Reading from file
#      content = file.read()
#      print("File Content: \n",content)
#      list_of_words = content.split(' ')
#      print(list_of_words)
#      for word in list_of_words:
#           str_len = len(word)
#           if (str_len % 2) == 0:
#               print(word)
#           else:
#               continue
# except:
#      print("There is exception: opening file")
# finally:
#     file.close()
#
# # print()
#
# output:
# You have entered file name -  test1.txt
# File Content:
#  Hello I am a file Where you need to return the data string
# ['Hello', 'I', 'am', 'a', 'file', 'Where', 'you', 'need', 'to', 'return', 'the', 'data', 'string']
# am
# file
# need
# to
# return
# data
# string
#
# Process finished with exit code 0


#************************************************************************************#
#*                                                                                   #
#*                  TASK-5 COMPLETED SUCCESSFULLY                                    #
#*                  Author: Dhanashree Kharade                                       #
#*                                                                                   #
#*************************************************************************************#
