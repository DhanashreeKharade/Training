###########################################################################
#  Task Two  - OPERATORS AND DECISION MAKING STATEMENT                    #
#  Author    - Dhanashree Kharade                                         #
#  Date      - 02/09/2023                                                 #
#  Log       -                                                            #
###########################################################################

# *************************************
# 1.*****************
# Write a program in Python to perform the following operation:
# If a number is divisible by 3 it should print “Consultadd” as a string
# If a number is divisible by 5 it should print “Python Training” as a string
# If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a
# string.

# x=int(input("Enter any no: "))
# if x%3==0:
#     print("Consultadd")
#     if x%5==0:
#         print("Python Training")
# elif x%3==0 and x%5==0:
#     print("Consultadd - Python Training")
# else:
#     print("No is neither divisible by 3 nor by 5")

# output
# 1.Enter any no: 30
# Consultadd
# Python Training
# 2.Enter any no: 33
# Consultadd
# 3.Enter any no: 70
# No is neither divisible by 3 nor by 5



# 2.**********************************************************************
# 2. Write a program in Python to perform the following operator based task:
# Ask user to choose the following option first:
# If User Enter 1 - Addition
# If User Enter 2 - Subtraction
# If User Enter 3 - Division
# If User Enter 4 - Multiplication
# If User Enter 5 - Average
# Ask user to enter two numbers and keep those numbers in variables num1 and num2
# respectively for the first 4 options mentioned above.
# Ask the user to enter two more numbers as first and second for calculating the average as
# soon as the user chooses an option 5.
# At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
# NOTE: At a time a user can only perform one action.

# n1,n2=input("Enter any two numbers for calculation:").split(",")
# num1 = int(n1)
# num2 = int(n2)
# print("num1 :",num1)
# print("num2 :",num2)
# choice = input("Enter 1 - Addition \n"
#       "Enter 2 - Subtraction \n"
#       "Enter 3 - Division \n"
#       "Enter 4 - Multiplication \n"
#       "Enter 5 - Average\n")
# print("User choice - ",choice)
# match choice:
#     case "1":
#         result = num1 + num2
#         print(result)
#     case "2":
#         result = num1 - num2
#         print(result)
#     case "3":
#         result = num1 / num2
#         print(result)
#     case "4":
#         result = num1 * num2
#         print(result)
#     case "5":
#         result = (num1 + num2)/2
#         print(result)
# if result < 0:
#     print("Result is Negative")

# output:C:\pythonProject1\venv\Scripts\python.exe C:\pythonProject1\venv\PyAssign1.py
# Enter any two numbers for calculation:-4,5
# num1 : -4
# num2 : 5
# Enter 1 - Addition
# Enter 2 - Subtraction
# Enter 3 - Division
# Enter 4 - Multiplication
# Enter 5 - Average
# 4
# User choice -  4
# -20
# Result is Negative
######################################################################################################
#3. Assigment - Write a program in Python to implement the given flowchart
#############################################################################################
# n1 = input("Enter value of a =")
# n2 = input("Enter value of b =")
#
# n3 = input("Enter value of c =")
# a = int(n1)
# b = int(n2)
# c = int(n3)
# avg = (a + b + c)/3
# print("Average is:",avg)
#
# if avg > a and avg > b and avg > c:
#     print("Average is Higher than a,b,c")
# elif avg > a and avg > b:
#     print("Average is Higher than a,b,")
# elif avg > a and avg > c:
#     print("Average is Higher than a,b,c")
# elif avg > b and avg > c:
#     print("Average is Higher than b and c")
# elif avg > a:
#     print("Average is just higher that a")
# elif avg>b:
#     print("Average is just higher that b")
# elif avg > c:
#     print("Average is just higher that c")
#
# output:
# Enter value of a =20
# Enter value of b =40
# Enter value of c =60
# Average is: 40.0
# Average is just higher that a


##################################################################################################
# 4. Write a program in Python to break and continue if the following cases occurs:
# If user enters a negative number just break the loop and print “It’s Over”
# If user enters a positive number just continue in the loop and print “Good Going”
##################################################################################################

# x=int(input("Enter No"))
# if x<0:
#     print("Its Over")
#     exit(0)
# elif x>0:
#     print("Good Going")
#
# output :
# 1.Enter No7
# Good Going
#
# 2.Enter No -7
# Its Over

#########################################################################################################
# 5. Write a program in Python which will find all such numbers which are divisible by 7 but are not a
# multiple of 5, between 2000 and 3200.
##########################################################################################################
#
# startNum = 2000
# endNum = 3200
#
# for number in range(startNum, endNum):
#     result_divisible_7 = number % 7
#     if result_divisible_7 == 0:
#         result_multiple_5 = number % 5
#         if result_multiple_5 != 0:
#              print("Number divisible by 7 and not multiple of 5 is -",number)

##########################################################################################################
# What is the output of the following code examples?

################################################################################################
# x=123
# for i in range(x):
#     print(i)

# output: its will display numbers 1 to 122

###################################################################
#
# i=0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         exit(0)
#     else:
#         print("error")

# output of given program is:
# 0
# error
# 1
# error
# 2
#######################################################################
#
# count=0
# while 1:
#     print(count)
#     count+=1
#     if count>=5:
#         break
#
# output:0
# 1
# 2
# 3
# 4
# (//there should be 1 insted of true)

############################################################################################
# 7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
# Expected output: 0 1 2 4 5
# Note: Use ‘continue’ statement
#
# i = 0
# while i < 6:
#     if i == 3 or i == 6:
#         i = i + 1
#         continue
#     print(i)
#     i = i + 1
#

####################################################################################################
# Write a program that accepts a string as an input from the user and calculate the number of digits
# and letters.
#####################################################################################################33
#
# s=input("Enter Any String")
# letters=numbers=0
# for i in s :
#     if i.isalpha():
#         letters +=1
#     elif i.isdigit():
#         numbers+=1
#     else:
#         pass
# print("Letters: ",letters)
# print("Numbers: ",numbers)
# *****************************************
# output:Enter Any String Dhanashree12345
# Letters:  10
# Numbers:  5

####################################################################################################
# Read the two parts of the question below:
# Write a program such that it asks users to “guess the lucky number”. If the correct number is
# guessed the program stops, otherwise it continues forever.
# Modify the program so that it asks users whether they want to guess again each time. Use two
# variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
# to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
# The program continues as long as a user has not answered “no” and has not guessed the correct
# number)
#####################################################################################################
# import random
#
# while(True):
#     number = int(input("Guess the lucky number -"))
#     luckyNumber = random.randint(0, 100)
#     print("Lucky number is - ", luckyNumber)
#     if number == luckyNumber:
#         print("Hooray! you guessed lucky number")
#         break
#     else:
#         continue

#******************** modified 2nd part**********************
# import random
#
# while(True):
#     number = int(input("Guess the lucky number -"))
#     luckyNumber = random.randint(0, 100)
#     print("Lucky number is - ", luckyNumber)
#     if number == luckyNumber:
#         print("Hooray! you guessed lucky number")
#         break
#     else:
#         choice = input("No luck yet. Do you want to retry?(y/n) -")
#         print("choice -", choice)
#         if choice == "y":
#             continue
#         elif choice == "n":
#             break

#######################################################################################################
# 10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
# such as
#
# While counter <= 5:
# print(“Type in the”, counter, “number”
# counter=counter+1
# The program asks for five guesses (no matter whether the correct number was guessed or not). If the
# correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
# After the fifth guess it stops and prints “Game over!”.
# ########################################################################################################
#
# import random
#
# i=0
# while i < 5:
#     number=int(input("Guess the lucky number -"))
#     luckyNumber = random.randint(0, 100)
#     print("Lucky number is - ", luckyNumber)
#     if number == luckyNumber:
#        print("Hooray! you guessed lucky number")
#        break
#     else:
#        i = i + 1
#        print("Your Attempt Number is -",i)
#        continue
#
# output:
# Guess the lucky number -35
# Lucky number is -  12
# Your Attempt Number is - 1
# Guess the lucky number -54
# Lucky number is -  49
# Your Attempt Number is - 2
# Guess the lucky number -27
# Lucky number is -  81
# Your Attempt Number is - 3
# Guess the lucky number -86
# Lucky number is -  35
# Your Attempt Number is - 4
# Guess the lucky number -77
# Lucky number is -  19
# Your Attempt Number is - 5
