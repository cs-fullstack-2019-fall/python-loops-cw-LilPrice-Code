# Exercise 1:
#
# Print -20 to and including 50. Use any loop you want.

# x=range(-20, 51)
# for n in x:
#     print(n)
#
# Exercise 2:
#
# Create a loop that prints even numbers from 0 to and including 20.Hint: You can find multiples of 2 with (whatever_number % 2 == 0)

# x = 0
# while x < 21:
#     if  x % 2==0:
#         print(x)
#         x += 1
#     else:
#         x += 1

# Exercise 3:
#
# Prompt the user for 3 numbers. Then print the 3 numbers along with their average after the 3rd number is entered. Refer to example below replacing NUMBER1, NUMBER2, NUMBER3, and THEAVERAGE with the actual values.
#
# Ex.Output
# num1 = int(input("Enter a number "))
# num2 = int(input("Enter a number "))
# num3 = int(input("Enter a number "))
#
# ave = (num1 + num2 + num3)  / 3
#
# print("The average of " + str(num1) + ", " + str(num2) +", and " + str(num3) + " is " + str(ave))

#
# The average of NUMBER1, NUMBER2, and NUMBER3 is THEAVERAGE
# Exercise 4:
#
# Use any loop to print all numbers between 0 and 100 that are divisible by 4.
#
# Challenge:
#
# Password Checker - Ask the user to enter a password. Ask them to confirm the password. If it's not equal, keep asking until it's correct or they enter 'Q' to quit.
pas = input("Enter a Password ")

while 0==0:
    fin = input("Reenter password ")
    if fin == pas:
        break